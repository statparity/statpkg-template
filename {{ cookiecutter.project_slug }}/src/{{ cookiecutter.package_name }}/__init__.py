"""{{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"

from {{ cookiecutter.package_name }}.core import example_function

__all__ = ["example_function"]
