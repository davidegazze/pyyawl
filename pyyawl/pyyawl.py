"""Main module."""
from pyyawl.namedregistry import registry
from tqdm import tqdm
from omegaconf import OmegaConf
from pathlib import Path


def execute(file_or_content, verbose):
    """Console script for pyyawl."""
    file_or_content = Path(file_or_content)
    if file_or_content.exists():
        workflow = OmegaConf.load(file_or_content)
    else:
        workflow = OmegaConf.create(str(file_or_content))
    return execute_pipeline(workflow, verbose)


def execute_pipeline(workflow, verbose):
    from pyyawl import operators

    assert len(registry) > 0, 'empty function registry'

    if 'steps' not in workflow:
        raise Exception('missing steps definition')

    for step in workflow.steps:
        assert step.name in registry, f'missing operator {step.name}'

    print('starting workflow', workflow.name)
    results = dict()
    for step in tqdm(workflow.steps):
        results[step.name] = registry[step.name](verbose=verbose,
                                                 **step.arguments)
    return results


def show_registry(names=False):
    from pyyawl import operators

    if names:
        return list(registry.keys())
    else:
        return registry


def generate():
    return """
name: test
description: test description

steps:
  - name: echo
    arguments:
      value: yawl
  - name: echo
    arguments:
      value: world
  - name: papermill
    arguments:
      input_path: tests/notebooks/sum_test.ipynb
      output_path: tests/notebooks/sum_test_out.ipynb
      parameters:
        a: 8
        b: 4
  - name: python
    arguments:
      value: tests/scripts/script1.py
"""
