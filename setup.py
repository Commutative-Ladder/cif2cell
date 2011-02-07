# Copyright 2010 Torbjorn Bjorkman
# This file is part of cif2cell
#
# cif2cell is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cif2cell is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cif2cell.  If not, see <http://www.gnu.org/licenses/>.
#
from distutils.core import setup
from subprocess import *

# Get list of the cif example files
tmp = Popen(['ls','cifs'], stdout=PIPE).communicate()[0]
filelist = tmp.split()
ciffiles = []
for f in filelist:
    ciffiles.append('cifs/'+f)

setup(name='cif2cell',
      version='0.2.0',
      description='Construct a unit cell from CIF data',
      long_description='A command-line tool to generate the geometrical setup for various electronic structure codes from a CIF format file.',
      author='Torbjorn Bjorkman',
      author_email='torbjornb@gmail.com',
      url='http://cif2cell.sourceforge.net/',
      py_modules=['uctools','spacegroupdata'],
      scripts=['cif2cell'],
      requires=['CifFile'],
      data_files=[('./', ['LICENSE']),
                  ('lib/cif2cell/sample_cifs', ciffiles)],
      license='GNU General Public License version 3'
      )