import os
from ruamel.yaml import YAML
import fileinput
import re
import sys


def replace_os_sep(filepath):
    with open(filepath) as file:
        data = file.read()

    if os.sep == "\\":
        data = data.replace("/", os.sep)
    else:
        data = data.replace("\\", os.sep)

    with open(filepath, "w") as file:
        file.write(data)


yaml = YAML()
project_folder = os.path.abspath("setup_prev.py")[:-13]
etc_folder = project_folder + "etc" + os.sep
venv_bin = project_folder + "venv" + os.sep + "bin" + os.sep


# Replace etc path in config.yaml
with open(project_folder + "config.yaml") as f:
    conf = yaml.load(f)

conf['etc']['path'] = project_folder + "etc" + os.sep

with open(project_folder + "config.yaml", "w") as f:
    yaml.dump(conf, f)

if len(sys.argv) == 1:
    # Fix Virtual Env path in activate script
    with fileinput.FileInput(project_folder + "venv/bin/activate", inplace=True, backup=".bak") as file:
        for line in file:
            print(re.sub(r'VIRTUAL_ENV=(.*)', "VIRTUAL_ENV=\"" + project_folder + "venv\"", line), end="")

    # Check if symlinks are OK
    if not os.path.islink(venv_bin + "python3.7"):
        os.remove(venv_bin + "python3.7")
        os.symlink("/usr/local/bin/python3.7", venv_bin + "python3.7")

    if not os.path.islink(venv_bin + "python3"):
        os.remove(venv_bin + "python3")
        os.symlink(venv_bin + "python3.7", venv_bin + "python3")

    if not os.path.islink(venv_bin + "python"):
        os.remove(venv_bin + "python")
        os.symlink(venv_bin + "python3.7", venv_bin + "python")