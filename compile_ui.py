#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import subprocess

resource_file = "./widgets/ui/resources.qrc"
out_name = "./resources_rc.py" 
cmd = f"pyrcc5 -o {out_name} {resource_file}".split(" ")
subprocess.run(cmd)

files = glob.glob("widgets/ui/*.ui")
for file in files:
    out_name = file.replace(".ui", ".py").replace("/ui", "/py_files")
    cmd = f"pyuic5 -x {file} -o {out_name}".split(" ")
    subprocess.run(cmd)