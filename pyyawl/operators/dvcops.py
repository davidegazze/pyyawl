__all__ = ['call_dvc_add', 'call_dvc_push', 'call_dvc_pull']

from pathlib import Path
from ..namedregistry import export
from .baseops import subprocess_run


@export(name='dvc_add')
def call_dvc_add(path, verbose=False):
    result = subprocess_run(['dvc', 'add', path])
    if verbose:
        print('called dvc_add', path, result)
    return result


@export(name='dvc_push')
def call_dvc_push(verbose=False):
    result = subprocess_run(['dvc', 'push'])
    if verbose:
        print('called dvc_push', result)
    return result


@export(name='dvc_pull')
def call_dvc_pull(verbose=False):
    result = subprocess_run(['dvc', 'pull'])
    if verbose:
        print('called dvc_pull', result)
    return result