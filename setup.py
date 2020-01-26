#!/usr/bin/env python

import os
from setuptools import setup

with open('pyriodic_aflow/version.py') as version_file:
    exec(version_file.read())

setup(name='pyriodic-aflow',
      author='Matthew Spellings',
      author_email='matthew.p.spellings@gmail.com',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3',
      ],
      description='Pyriodic adapter to the AFLOW project crystal prototype database',
      entry_points={
          'pyriodic_sources': ['aflow = pyriodic_aflow.unit_cells:load_standard'],
      },
      extras_require={},
      install_requires=[
          'pyriodic-structures',
      ],
      license='GPL3',
      packages=[
          'pyriodic_aflow',
      ],
      python_requires='>=3',
      version=__version__
      )
