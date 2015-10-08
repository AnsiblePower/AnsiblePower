import sys
#from ansible.callbacks import PlaybookRunnerCallbacks
#from ansible.callbacks import log_flock, log_unflock, stringc, logger
from ansible.callbacks import *
from ansible import utils
from ansible import constants
from ansible.module_utils import basic
from ansible.utils.unicode import to_bytes


def display(msg, templateid, color=None, stderr=False, screen_only=False, log_only=False, runner=None):
    log_flock(runner)
    msg2 = msg
    if color:
        msg2 = stringc(msg, color)
    if not log_only:
        if not stderr:
            try:
                print msg2
            except UnicodeEncodeError:
                print msg2.encode('utf-8')
        else:
            try:
                print >>sys.stderr, msg2
            except UnicodeEncodeError:
                print >>sys.stderr, msg2.encode('utf-8')
    if constants.DEFAULT_LOG_PATH != '':
        while msg.startswith("\n"):
            msg = msg.replace("\n","")
        if not screen_only:
            if color == 'red':
                logger.error(msg)
            else:
                logger.info(msg)
    log_unflock(runner)

class myCustCallback(PlaybookRunnerCallbacks):

    def __init__(self, stats, templateid, verbose=None):
        super(myCustCallback, self).__init__(stats, verbose)
        self.jobTemplateID = templateid

    def on_unreachable(self, host, results):
        if self.runner.delegate_to:
            host = '%s -> %s' % (host, self.runner.delegate_to)

        item = None
        if type(results) == dict:
            item = results.get('item', None)
            if isinstance(item, unicode):
                item = utils.unicode.to_bytes(item)
            results = basic.json_dict_unicode_to_bytes(results)
        else:
            results = utils.unicode.to_bytes(results)
        host = utils.unicode.to_bytes(host)
        if item:
            msg = "fatal: [%s] => (item=%s) => %s" % (host, item, results)
        else:
            msg = "fatal: [%s] => %s" % (host, results)
        display(msg, color='red', runner=self.runner)
        super(myCustCallback, self).on_unreachable(host, results)

    def on_failed(self, host, results, ignore_errors=False):
        if self.runner.delegate_to:
            host = '%s -> %s' % (host, self.runner.delegate_to)

        results2 = results.copy()
        results2.pop('invocation', None)

        item = results2.get('item', None)
        parsed = results2.get('parsed', True)
        module_msg = ''
        if not parsed:
            module_msg  = results2.pop('msg', None)
        stderr = results2.pop('stderr', None)
        stdout = results2.pop('stdout', None)
        returned_msg = results2.pop('msg', None)

        if item:
            msg = "failed: [%s] => (item=%s) => %s" % (host, item, utils.jsonify(results2))
        else:
            msg = "failed: [%s] => %s" % (host, utils.jsonify(results2))
        display(msg, color='red', runner=self.runner)

        if stderr:
            display("stderr: %s" % stderr, color='red', runner=self.runner)
        if stdout:
            display("stdout: %s" % stdout, color='red', runner=self.runner)
        if returned_msg:
            display("msg: %s" % returned_msg, color='red', runner=self.runner)
        if not parsed and module_msg:
            display(module_msg, color='red', runner=self.runner)
        if ignore_errors:
            display("...ignoring", color='cyan', runner=self.runner)
        super(myCustCallback, self).on_failed(host, results, ignore_errors=ignore_errors)

    def on_ok(self, host, host_result):
        if self.runner.delegate_to:
            host = '%s -> %s' % (host, self.runner.delegate_to)

        item = host_result.get('item', None)

        host_result2 = host_result.copy()
        host_result2.pop('invocation', None)
        verbose_always = host_result2.pop('verbose_always', False)
        changed = host_result.get('changed', False)
        ok_or_changed = 'ok'
        if changed:
            ok_or_changed = 'changed'

        # show verbose output for non-setup module results if --verbose is used
        msg = ''
        if (not self.verbose or host_result2.get("verbose_override",None) is not
                None) and not verbose_always:
            if item:
                msg = "%s: [%s] => (item=%s)" % (ok_or_changed, host, item)
            else:
                if 'ansible_job_id' not in host_result or 'finished' in host_result:
                    msg = "%s: [%s]" % (ok_or_changed, host)
        else:
            # verbose ...
            if item:
                msg = "%s: [%s] => (item=%s) => %s" % (ok_or_changed, host, item, utils.jsonify(host_result2, format=verbose_always))
            else:
                if 'ansible_job_id' not in host_result or 'finished' in host_result2:
                    msg = "%s: [%s] => %s" % (ok_or_changed, host, utils.jsonify(host_result2, format=verbose_always))

        if msg != '':
            if not changed:
                display(msg, color='green', runner=self.runner)
            else:
                display(msg, color='yellow', runner=self.runner)
        if constants.COMMAND_WARNINGS and 'warnings' in host_result2 and host_result2['warnings']:
            for warning in host_result2['warnings']:
                display("warning: %s" % warning, color='purple', runner=self.runner)
        super(myCustCallback, self).on_ok(host, host_result)

    def on_skipped(self, host, item=None):
        if self.runner.delegate_to:
            host = '%s -> %s' % (host, self.runner.delegate_to)

        if constants.DISPLAY_SKIPPED_HOSTS:
            msg = ''
            if item:
                msg = "skipping: [%s] => (item=%s)" % (host, item)
            else:
                msg = "skipping: [%s]" % host
            display(msg, color='cyan', runner=self.runner)
            super(myCustCallback, self).on_skipped(host, item)

    def on_no_hosts(self):
        display("FATAL: no hosts matched or all hosts have already failed -- aborting\n", color='red', runner=self.runner)
        super(myCustCallback, self).on_no_hosts()

    def on_async_poll(self, host, res, jid, clock):
        if jid not in self._async_notified:
            self._async_notified[jid] = clock + 1
        if self._async_notified[jid] > clock:
            self._async_notified[jid] = clock
            msg = "<job %s> polling, %ss remaining"%(jid, clock)
            display(msg, color='cyan', runner=self.runner)
        super(myCustCallback, self).on_async_poll(host,res,jid,clock)

    def on_async_ok(self, host, res, jid):
        if jid:
            msg = "<job %s> finished on %s"%(jid, host)
            display(msg, color='cyan', runner=self.runner)
        super(myCustCallback, self).on_async_ok(host, res, jid)

    def on_async_failed(self, host, res, jid):
        msg = "<job %s> FAILED on %s" % (jid, host)
        display(msg, color='red', stderr=True, runner=self.runner)
        super(myCustCallback, self).on_async_failed(host,res,jid)

    def on_file_diff(self, host, diff):
        display(utils.get_diff(diff), runner=self.runner)
        super(myCustCallback, self).on_file_diff(host, diff)

