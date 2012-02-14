import os
import shutil

import accessions
import annotations
import files
import genomes
import profiles
import experiments
import read_length
import view

import csv

def read_csv(file_name):
    return [line for line in csv.DictReader(open(file_name, 'r'), 
                                            delimiter='\t', 
                                            skipinitialspace=True)]

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

    def install(self):
        workspace = self.buildout['extract']['workspace']
        staging = self.options['staging']
        data = {}
        for file in ['accessions.csv',
                     'annotations.csv',
                     'experiments.csv',
                     'files.csv',
                     'genomes.csv',
                     'profiles.csv',
                     'read_length.csv',
                     'view.csv']:
            source = os.path.join(workspace, file)
            target = os.path.join(staging, file)
            shutil.copyfile(source, target)
            data[file] = read_csv(target)

        accessions.main(data, workspace)
        annotations.main(data, workspace)
        files.main(data, workspace)
        genomes.main(data, workspace)
        profiles.main(data, workspace)
        experiments.main(data, workspace)
        read_length.main(data, workspace)
        view.main(data, workspace)

    def update(self):
        return self.install()