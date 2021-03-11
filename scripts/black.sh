#!/usr/bin/env bash

set -e
set -x

black run.py app cogs --check --exclude=app/controller/__init__.py