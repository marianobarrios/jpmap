#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.distutils")

name = "jpmap"
default_task = "publish"


@init
def set_properties(project):
    project.set_property('flake8_break_build', True)
