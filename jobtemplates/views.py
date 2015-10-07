import os
import yaml
from ansible.inventory import Inventory, Host, Group
from ansible.playbook import PlayBook
from ansible import callbacks
from ansible import utils, constants as C
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from .models import JobTemplates, Projects
from .forms import CreateJobTemplateForm
from inventories.models import Hosts


class JobTemplatesIndex(generic.ListView):
    model = JobTemplates
    template_name = 'jobtemplates/jobTemplatesIndex.html'
    paginate_by = 5


class createJobTemplate(generic.CreateView):
    form_class = CreateJobTemplateForm
    template_name = 'jobtemplates/createJobTemplate.html'
    success_url = '/jobtemplates'


class editJobTemplate(generic.UpdateView):
    form_class = CreateJobTemplateForm
    model = JobTemplates
    template_name = 'jobtemplates/editJobTemplate.html'
    success_url = '/jobtemplates'


class deleteJobTemplate(generic.DeleteView):
    model = JobTemplates
    template_name = 'jobtemplates/deleteJobTemplate.html'
    success_url = '/jobtemplates'

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        return JsonResponse({})


def runTest(request, **kwargs):
    if request.method == 'GET':
        template = JobTemplates.objects.get(pk=kwargs['pk'])
        directory = template.project.directory
        playbook = template.playbook
        playbookPath = os.path.join(directory, playbook)
        stream = file(playbookPath, 'r')
        yamlObj = yaml.load(stream)
        print yamlObj
        return HttpResponseRedirect('/jobtemplates')


def runInv(request, **kwargs):
    template = JobTemplates.objects.get(pk=kwargs['pk'])
    hostobj = Hosts.objects.get(inventory=template.inventory.pk)
    inventoryName = template.inventory.name
    hostname = hostobj.name
    port = hostobj.port
    ip = hostobj.ipAddress

    # Constants
    C.HOST_KEY_CHECKING = False

    # Callbacks
    utils.VERBOSITY = 3
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    stats = callbacks.AggregateStats()
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    # Inventory gathering
    inventory = Inventory()
    host = Host(hostname)
    # TODO: implement host group
    group = Group('mygroup')
    if ip:
        host.set_variable('ansible_ssh_host', ip)
    elif port:
        host.set_variable('ansible_ssh_port', port)
    group.add_host(host)
    inventory.add_group(group)
    # Playbook gathering
    playbookPath = os.path.join(template.project.directory, template.playbook)

    # Playbook run
    pb = PlayBook(
        playbook=playbookPath,
        host_list=None,
        inventory=inventory,     # Our hosts, the rendered inventory file
        remote_user='root',
        remote_pass='qwer1234',
        callbacks=playbook_cb,
        runner_callbacks=runner_cb,
        stats=stats,
        #extra_vars=extraVars,
        #private_key_file='/path/to/key.pem'
    )
    pb.run()

    return HttpResponseRedirect(reverse('jobtemplates:index'))




def getJSONDirectory(request, **kwargs):
    if request.method == 'GET':
        proj = Projects.objects.get(pk=kwargs['pk'])
        result = {}
        i = 0
        try:
            for filename in os.listdir(proj.directory):
                if filename[-3:] == 'yml':
                    i += 1
                    result[i] = filename
        except OSError, e:
            print str(e)
        return JsonResponse(result)
