#!/usr/bin/env python
"""Pre-generation hook for cookiecutter."""
import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug }}'
package_name = '{{ cookiecutter.package_name }}'

if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: {module_name} is not a valid Python module name!')
    sys.exit(1)

if not re.match(MODULE_REGEX, package_name):
    print(f'ERROR: {package_name} is not a valid Python module name!')
    sys.exit(1)
