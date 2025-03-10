#!/usr/bin/env python3

"""Render the jinja template given as the first command line argument."""

from jinja2 import Environment, FileSystemLoader
import os
import sys

varnames = [
    'BINDIR',
    'CONFDIR',
    'GROUP',
    'NAME',
    'USER',
]

envvars = {x: os.environ[x] for x in varnames}

if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader("."), autoescape=False)
    template = env.get_template(sys.argv[1])
    print(template.render(**envvars))
