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
        import pkg_resources
        pkg_resources.require('docker')
        print("INFO :: pkg_resources.require('docker') :: PASSED")
    except:
        print("INFO :: pkg_resources.require('docker') :: FAILED")
        exit(1)
else:
    print("WARNING :: which('docker') failed")
    print("WARNING :: docker.DockerClient.from_env() and")
    print("WARNING :: pkg_resources.require('docker') tests skipped")
exit(0)
