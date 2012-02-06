import os

def read_length():
    if not 'readType' in file:
        file['readType'] = 'NA'
        read_length = 'NA'
    elif file['readType'] == '2x76D':
        read_length = 76
    elif file['readType'] == '1x70D':
        read_length = 70
    elif file['readType'] == '2x75':
        read_length = 75
    elif file['readType'] == '1x80':
        read_length = 80
    elif file['readType'] == '1x40':
        read_length = 40
    elif file['readType'] == '1x75D':
        read_length = 75
    elif file['readType'] == '2x100':
        read_length = 100
    elif file['readType'] == '2x96':
        read_length = 96
    elif file['readType'] == '2x53':
        read_length = 53
    elif file['readType'] == '2x76':
        read_length = 76
    elif file['readType'] == '2x46':
        read_length = 46
    elif file['readType'] == '2x35':
        read_length = 35
    elif file['readType'] == '2x34':
        read_length = 34
    elif file['readType'] == '100':
        read_length = 100
    elif file['readType'] == '2x40':
        read_length = 40
    elif file['readType'] == '2x50':
        read_length = 50
    elif file['readType'] == '2x51':
        read_length = 51
    elif file['readType'] == '2x54':
        read_length = 54
    elif file['readType'] == '2x49':
        read_length = 49
    elif file['readType'] in ['2x36', '1x36']:
        read_length = 36
    elif file['readType'] == '2x37':
        read_length = 37
    elif file['readType'] == '50':
        read_length = 50
    elif file['readType'] == '75':
        read_length = 75
    else:
        raise AttributeError


def main(data, workspace):
    pass
    
         
