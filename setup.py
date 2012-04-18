# -*- coding: utf-8 -*-
##############################################################################
#
#    netrpclib
#    Copyright (C) 2012 SYLEAM (<http://syleam.fr>)
#                  Christophe CHAUVET <christophe.chauvet@syleam.fr>
#
#    This file is a part of netrpclib
#
#    netrpclib is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    netrpclib is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from distutils.core import setup
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(name = "jsonrpc",
      version = "1.0.0",
      description = "NETRPC Library for OpenERP",
      keywords = "netrpc openerp",
      author = "Christophe CHAUVET",
      author_email='christophe.chauvet@gmail.com',
      url = "https://github.com/kryskool/netrpclib",
      license = "AGPLv3",
      long_description = readme,
      packages = ['netrpclib']
)
