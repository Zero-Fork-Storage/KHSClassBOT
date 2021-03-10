#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place run.py app cogs --exclude=__init__.py
black run.py app cogs
isort run.py app cogs