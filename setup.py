# -*- coding: utf-8 -*-

# #############################################################################
# Copyright (C) 2013  raven700
#
# https://github.com/raven700/SWatcher
#
# This file is part of SWatcher.
#
# SWatcher is a tool for watching and managing Windows certain services.
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# #############################################################################

from distutils.core import setup
import py2exe, sys, os

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = "2013.08.12"
        self.company_name = "raven700"
        self.copyright = "raven700 (https://github.com/raven700/SWatcher)"
        self.name = u"SWatcher"


SWatcher = Target(
    description = u"Program sprawdzający aktywność usług systemowych Windows.",
    script = "main.py",
    #icon_resources = [(1, "icon.ico")],
    dest_base = "SWatcher")

setup(
    options = {"py2exe": {"includes":["sip"],
                          "compressed": True,
                          "optimize": 2,
                          "bundle_files": 1}},
    zipfile = None,
    windows = [SWatcher]
    )