import os


def main(data, workspace):

    views = {}
    
    for file in data['files.csv']:
    
        key = (file['project_id'], file['accession_id'])
        
        if views.has_key(key):
            views[key].append(file)
        else:
            views[key] = [file]

    for key, files in views.items():
        if len(files) == 1:
            file = files[0]
            if file['type'] in ['fasta', 'fastq']:
                file['view'] = "RawData"
            elif file['type'] == 'bam':
                file['view'] = "Alignments"
            else:
                raise AttributeError
        else:
            number = 1
            for file in files:
                if file['type'] == 'fastq':
                    file['view'] = 'FastqRd%d' % number
                elif file['type'] == 'fasta':
                    file['view'] = 'FastqRd%d' % number
                elif file['type'] == 'bam':
                    file['view'] = 'Alignment%d' % number
                else:
                    raise AttributeError
                number += 1

    path = os.path.join(workspace, "view.csv")
    view = open(path, "w")
    view.write("project_id\taccession_id\tfile_location\tview\n")

    for key, files in views.items():
        for file in files:
            view.write("%s\t%s\t%s\t%s\n" % (file['project_id'],
                                             file['accession_id'],
                                             file['file_location'],
                                             file['view']))
    view.close()