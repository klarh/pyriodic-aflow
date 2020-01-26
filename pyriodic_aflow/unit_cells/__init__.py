import json
import os
import re

import pyriodic

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_DB_TARGET = os.path.join(_THIS_DIR, 'aflow_db.json')

def load_standard(db):
    with db.connection as conn, open(_DB_TARGET, 'r') as json_file:
        all_structures = json.load(json_file)

        for description in all_structures:
            name = description['name']
            spg = description['space_group']
            structure = pyriodic.Structure(
                description['positions'],
                description['types'],
                description['box'])

            db.insert_unit_cell(name, spg, structure, conn)

            safe_name = name.replace('-', '_')
            safe_name = re.sub(r'[\[\],\(\)]', '__', safe_name)
            globals()[safe_name] = structure
