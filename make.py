#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011 Benoît HERVIER <khertan@khertan.net>
# Licenced under GPLv3

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published
## by the Free Software Foundation; version 3 only.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

import os
import sys
from glob import glob

import pypackager
sys.path.append('wleux')

from wleux import __version__

__build__ = '1'
__author__ = "Benoît HERVIER (khertan)"
__mail__ = "khertan@khertan.net"
__upgrade__ = '''1.0: First public release
'''

if __name__ == "__main__":
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    p=pypackager.PyPackager("wleux")
    p.display_name = 'Wleux'
    p.version = __version__+'.0'
    p.buildversion = __build__
    p.description="Setup a wallpaper from the desktoppr.co service."
    p.upgrade_description=__upgrade__
    p.author=__author__
    p.maintainer=__author__
    p.email=__mail__
    p.depends = "python, python-pyside.qtgui, python-pyside.qtdeclarative, python-pyside.qtcore, python-pyside.qtopengl"
    p.suggests = ""
    p.section="user/office"
    p.arch="armel"
    p.urgency="low"
    p.icon='wleux.png'
    p.distribution="harmattan"
    p.repository="Khertan Repository"
    p.bugtracker = 'http://github.com/khertan/Wleux/issues'
    p.changelog =  p.upgrade_description
    p.maemo_flags = 'visible'
    p.meego_desktop_entry_filename = '/usr/share/applications/wleux.desktop'
    p.createDigsigsums = True
    files = []
    p.postinst = '''#!/bin/sh
chmod +x /opt/khtnotes/__init__.py
pycompile -O /opt/khtnotes/*.py
pycompile -O /opt/khtnotes/webdav/*.py'''
    p.createDigsigsums = True

    #Remove pyc and pyo
    for filepath in glob(os.path.join(os.path.dirname(__file__), p.name, '*.pyc')):
        os.remove(filepath)
    #Remove pyc and pyo
    for filepath in glob(os.path.join(os.path.dirname(__file__), p.name, '*.pyo')):
        os.remove(filepath)

    #Src
    for root, dirs, fs in os.walk(os.path.join(os.path.dirname(__file__), p.name)):
      for f in fs:
        files.append(os.path.join(root, f))

    p['/usr/share/dbus-1/services'] = ['wleux.service',]
    p['/usr/share/icons/blanco/80x80/apps'] = ['wleux.png',]
    p['/usr/share/applications'] = ['wleux.desktop',]
    p["/opt"] = files

    print p.generate(build_binary=True,build_src=True)
    if not os.path.exists('dists'):
        os.mkdir('dists')
    for filepath in glob(p.name+'_'+p.version+'-'+p.buildversion+'*'):
        os.rename(filepath, os.path.join(os.path.dirname(filepath), 'dists', os.path.basename(filepath)))



