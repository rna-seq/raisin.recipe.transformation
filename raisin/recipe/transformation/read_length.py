import os

def read_length(accession):
    if not 'readType' in accession:
        read_length = ''
    elif accession['readType'] == '2x76D':
        read_length = 76
    elif accession['readType'] == '1x70D':
        read_length = 70
    elif accession['readType'] == '2x75':
        read_length = 75
    elif accession['readType'] == '1x80':
        read_length = 80
    elif accession['readType'] == '1x40':
        read_length = 40
    elif accession['readType'] == '1x75D':
        read_length = 75
    elif accession['readType'] == '2x100':
        read_length = 100
    elif accession['readType'] == '2x96':
        read_length = 96
    elif accession['readType'] == '2x53':
        read_length = 53
    elif accession['readType'] == '2x76':
        read_length = 76
    elif accession['readType'] == '2x46':
        read_length = 46
    elif accession['readType'] == '2x35':
        read_length = 35
    elif accession['readType'] == '2x34':
        read_length = 34
    elif accession['readType'] == '100':
        read_length = 100
    elif accession['readType'] == '2x40':
        read_length = 40
    elif accession['readType'] == '2x50':
        read_length = 50
    elif accession['readType'] == '2x51':
        read_length = 51
    elif accession['readType'] == '2x54':
        read_length = 54
    elif accession['readType'] == '2x49':
        read_length = 49
    elif accession['readType'] in ['2x36', '1x36']:
        read_length = 36
    elif accession['readType'] == '2x37':
        read_length = 37
    elif accession['readType'] == '36':
        read_length = 36
    elif accession['readType'] == '50':
        read_length = 50
    elif accession['readType'] == '1x50':
        read_length = 50
    elif accession['readType'] == '75':
        read_length = 75
    elif accession['readType'] == '76':
        read_length = 76
    elif accession['readType'] == '1x76':
        read_length = 76
    else:
        print accession
        raise AttributeError
    return read_length

def main(data, workspace):

    views = {}

    file = open("workspace/read_length.csv", "w")
    file.write("project_id\taccession_id\tread_length\n")
    
    for accession in data['accessions.csv']:
        file.write("%s\t%s\t%s\n" % (accession['project_id'],
                                     accession['accession_id'],
                                     read_length(accession)))
    file.close()

