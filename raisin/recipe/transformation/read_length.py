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
        raise AttributeError("Read length parsing of 'readType' failed: %s" % read_length)
    return read_length


def get_accessions(data):
    accessions = {}
    for accession in data['accessions.csv']:
        key = (accession['project_id'],
               accession['accession_id'])
        accessions[key] = accession
    return accessions

def get_runs(data):
    runs = {}
    for run in data['runs.csv']:
        key = (run['project_id'],
               run['run_id'])
        runs[key] = run
    return runs


def main(data, workspace):
    path = os.path.join(workspace, "read_length.csv")
    file = open(path, "w")
    headers = ["project_id",
               "accession_id",
               "run_id",
               "read_length"]
    file.write("\t".join(headers))
    file.write("\n")

    accessions = get_accessions(data)
    runs = get_runs(data)

    # Update run_id when going through the accessions
    for key, accession in accessions.items():
        project_id, accession_id = key
        if key in runs:
            accession['run_id'] = accession_id

    # Update accession_id when going through the runs
    for key, run in runs.items():
        project_id, run_id = key
        if key in accessions:
            run['accession_id'] = run_id

    results = set()
    for accession in accessions.values():
        results.add((accession['project_id'],
                     accession['accession_id'],
                     accession.get('run_id', ''),
                     read_length(accession)))
    for run in runs.values():
        results.add((run['project_id'],
                     run.get('accession_id', ''),
                     run['run_id'],
                     run['read_length']))

    results = list(results)
    results.sort()

    for result in results:
        if result[1] and result[2] and result[1] != result[2]:
            print result
        file.write("%s\t%s\t%s\t%s\n" % result)

    file.close()
