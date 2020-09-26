#! usr/bin/python3
# -*-coding:utf-8 -*
from csv import DictReader
from json import load
from random import shuffle
from collections import deque
from time import sleep
def read_projects(filename):
    with open(file=filename) as csvfile:
        projects = [p for p in DictReader(csvfile)]

    return projects

def read_candidats(filename):
    with open(file=filename) as f:
        candidats=load(f)

    return candidats

projects = read_projects("data/projects.csv")

candidats = list(read_candidats("data/candidats.json"))



projects_queue = deque(projects)



for project in projects_queue:
    project["n_slots"] = int(project["n_slots"])
    project["id"] = int(project["id"])

affects = {project['id']: set() for project in projects}

shuffle(projects)
shuffle(candidats)
change = True
while change:
    change = False
    project = projects_queue.popleft()

    for c in candidats:


        if project["id"] in c["choices"]:

            affects[project["id"]].add(c["name"])
            #print("{} est affecté au projet {}".format(c["name"], project["id"]),'\n',"{",project["id"],"}=",affects[project["id"]])
            change=True
            candidats.remove(c)

    if project["n_slots"] != len(affects[project["id"]]):
        projects_queue.append(project)


for p_id, chosens in affects.items():
    print(p_id, chosens)
