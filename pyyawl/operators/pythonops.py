__all__ = ['call_echo']

import subprocess
from ..namedregistry import export


@export(name='python')
def call_echo(value, verbose=False):
    subprocess.run(['python', value])
