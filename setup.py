#!/usr/bin/env python

import os
from setuptools import setup

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

version_fname = os.path.join(THIS_DIR, 'pyriodic_aflow', 'version.py')
with open(version_fname) as version_file:
    exec(version_file.read())

readme_fname = os.path.join(THIS_DIR, 'README.md')
with open(readme_fname) as readme_file:
    long_description = readme_file.read()

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
      include_package_data=True,
      install_requires=[
          'pyriodic-structures',
      ],
      license='GPL3',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=[
          'pyriodic_aflow',
          'pyriodic_aflow.unit_cells',
      ],
      project_urls={
          'Documentation': 'http://pyriodic.readthedocs.io/',
          'Source': 'https://github.com/klarh/pyriodic-aflow'
          },
      python_requires='>=3',
      url='http://github.com/klarh/pyriodic-aflow',
      version=__version__
      )
