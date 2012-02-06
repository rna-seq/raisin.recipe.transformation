import os

def view():
    file_locations = accession['file_location'].split('\n')
    if len(file_locations) == 1:
        if accession['type'] in ['fasta', 'fastq']:
            accession['view'] = "RawData"
        elif accession['type'] == 'bam':
            accession['view'] = "Alignments"
    else:
        if accession['type'] == 'fastq':
            accession['view'] = '\n'.join(['FastqRd%d' % number for number in range(1, len(file_locations)+1)])
        elif accession['type'] == 'fasta':
            accession['view'] = '\n'.join(['FastqRd%d' % number for number in range(1, len(file_locations)+1)])
        elif accession['type'] == 'bam':
            accession['view'] = '\n'.join(['Alignment%d' % number for number in range(1, len(file_locations)+1)])

def main(data, workspace):
    pass
    
         
