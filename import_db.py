"""Note: This file exists only to aid in rebuilding the
database. Users of the database do not need to use this script.
"""
import argparse
import collections
import json
import io
import os

import garnett
import requests

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TARGET = os.path.join(
    THIS_DIR, 'pyriodic_aflow', 'unit_cells', 'aflow_db.json')

parser = argparse.ArgumentParser(
    description='Import data from the AFLOW web database')
parser.add_argument('-o', '--output', default=DEFAULT_TARGET,
    help='Output file target')

def get_short_name(description):
    prototype = description['Prototype']
    prototype = prototype.replace('</sub>', '').replace('<sub>', '')
    prototype = prototype.replace('&ndash;', '-')

    result = '{}-{}'.format(description['Pearson Symbol'], prototype)
    return result

def get_structure(description):
    filename = description['href'].replace('./', '').replace('.html', '.cif')
    rcif = requests.get(
        'http://aflowlib.org/CrystalDatabase/CIF/{}'.format(filename))
    handle = io.StringIO(rcif.content.decode())
    handle.name = 'test.cif'

    short_name = get_short_name(description)
    type_map = collections.defaultdict(lambda: len(type_map))

    with garnett.read(handle, fmt='cif') as traj:
        frame = traj[-1]
        types = [type_map[t] for t in frame.types]

        return dict(name=short_name,
                    positions=frame.positions.tolist(),
                    types=types,
                    space_group=description['Space Group Number'],
                    box=frame.box.get_box_array())

def main(output):
    req = requests.get('http://aflowlib.org/CrystalDatabase/js/table_sort.js')
    contents = req.content.decode()
    begin = contents.index('[')
    end = contents.index('];') + 1

    structure_list = json.loads(contents[begin:end])
    structure_list.sort(key=lambda x: x['AFLOW Prototype'])
    print('Found {} structures'.format(len(structure_list)))

    all_structures, bad_structures = [], []
    for description in structure_list:
        try:
            all_structures.append(get_structure(description))
        except:
            bad_structures.append(description)

    print('Bad structures ({})'.format(len(bad_structures)))
    print(json.dumps(bad_structures, sort_keys=True, indent=2))

    with open(output, 'w') as outfile:
        json.dump(all_structures, outfile, sort_keys=True, indent=2)

if __name__ == '__main__': main(**vars(parser.parse_args()))
