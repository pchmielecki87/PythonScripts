import azure.cli.core

from azure.cli.core import get_default_cli
get_default_cli().invoke(['vm', 'list', '-g', 'groupname'])