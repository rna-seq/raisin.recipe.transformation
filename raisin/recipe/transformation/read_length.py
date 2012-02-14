import os


def read_length(accession):
    """
    Given a readType, parse the read length

    readType can be for example:

    2x50, 75D, 2x76D, 1x70D, 2x75, 1x80, 1x40, 1x75D, 2x100
    2x96, 2x53, 2x76, 2x46, 2x35, 2x34, 100, 2x40, 2x50, 2x51
    2x54, 2x49, 2x36, 1x36, 2x37, 50, 75
    """
    read_length = accession['readType']
    if 'D' in read_length:
        read_length = read_length.split('D')[0]
    if  'x' in read_length:
        # Extract the read length taking the value after the x
        read_length = read_length.split('x')[1]
    if read_length.isdigit():
        return read_length
    else:
        print accession
        raise AttributeError
    return read_length


def main(data, workspace):
    path = os.path.join(workspace, "read_length.csv")
    file = open(path, "w")
    file.write("project_id\taccession_id\tread_length\n")

    for accession in data['accessions.csv']:
        file.write("%s\t%s\t%s\n" % (accession['project_id'],
                                     accession['accession_id'],
                                     read_length(accession)))
    file.close()
