#! usr/bin/python3
# -*-coding:utf-8 -*
from csv import DictReader

def read_projects(filename):
    with open(file=filename) as csvfile:
        projects = DictReader.reader(csvfile)
        print(projects)
    return projects

read_projects("data/projects.csv")


    