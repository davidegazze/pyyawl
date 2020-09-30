__all__ = ['call_echo', 'call_mkdir', 'call_rmdir', 'call_ls']

from pathlib import Path
import shutil
from ..namedregistry import export
from .baseops import subprocess_run


@export(name='echo')
def call_echo(value, verbose=False):
    result = subprocess_run(['echo', 'hello', value])
    if verbose:
        print(result)
    return result


@export(name='mkdir')
def call_mkdir(path, verbose=False):
    path = Path(path)
    return path.mkdir(parents=True, exist_ok=True)


@export(name='rmdir')
def call_rmdir(path, force=False, verbose=False):
    return shutil.rmtree(path, True, None)


@export(name='ls')
def call_ls(path, verbose=False):
    path = Path(path)
    result = list(path.iterdir())
    print(result)
    return result
