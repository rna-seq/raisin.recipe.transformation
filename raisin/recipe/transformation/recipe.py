import os
import shutil

import accessions
import annotations
import files
import genomes
import profiles
import experiments

import csv

SOURCE_PATH = "../extract/workspace/%s"

def read_csv(file_name):
    return csv.DictReader(open(file_name, 'r'), 
                               delimiter='\t', 
                               skipinitialspace=True)

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

    def install(self):
        workspace = self.options['workspace']
        data = {}
        for file in ['accessions.csv',
                     'profiles.csv',
                     'annotations.csv',
                     'files.csv',
                     'genomes.csv']:
            target = os.path.join(workspace, file)
            shutil.copyfile(SOURCE_PATH % file, target)
            data[file] = read_csv(target)

        accessions.main(data, workspace)
        annotations.main(data, workspace)
        files.main(data, workspace)
        genomes.main(data, workspace)
        profiles.main(data, workspace)
        experiments.main(data, workspace)
        
    def update(self):
        return self.install()