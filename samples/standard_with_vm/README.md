# Standard sample with VM

This sample is based on the standard sample app, but adds one more module which is a [Managed VM](https://cloud.google.com/appengine/docs/managed-vms/).

## Set up checklist

Follow the instructions for the [standard](https://github.com/zugaldia/appython/blob/master/samples/standard/README.md) sample. Before adding all files to GitHub (step 6), do the following:

1. Add the content of the `Makefile` in this folder to the standard sample `Makefile`.

2. Copy the `module_vm` folder to the `app` folder.

3. Replace the mentions to `module_vm` to the name you want (e.g. `module_native`) in `Makefile` and `vm.yaml`.

## Configuration

* You can install Debian packages via the `Dockerfile`.

* You can install Python packages (with PIP) also via `Dockerfile`.
