__author__ = 'dborysenko'
import requests
import json


def getRepos():
    req = requests.get('https://api.github.com/users/borisensx/repos')
    repoList = []
    if (req.ok):
        repoItems = json.loads(req.text or req.content)
        for repoItem in repoItems:
            print repoItem['name']
            repoList.append(repoItem['name'])
    return repoList



if __name__ == "__main__":
    getRepos()