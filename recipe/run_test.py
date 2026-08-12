#!/usr/bin/env python

from shutil import which
from sys import exit

if which('docker'):
    import docker
    try:
        docker.DockerClient.from_env(version='auto')
        print("INFO :: docker.DockerClient.from_env(version='auto') :: PASSED")
    except docker.errors.DockerException as e:
        print(f"WARNING :: docker.DockerClient.from_env(version='auto') :: no Docker daemon reachable ({e}) :: SKIPPED")
    try:
        import importlib.metadata
        importlib.metadata.version('docker')
        print("INFO :: importlib.metadata.version('docker') :: PASSED")
    except:
        print("INFO :: importlib.metadata.version('docker') :: FAILED")
        exit(1)
else:
    print("WARNING :: which('docker') failed")
    print("WARNING :: docker.DockerClient.from_env() and")
    print("WARNING :: importlib.metadata.version('docker') tests skipped")
exit(0)
