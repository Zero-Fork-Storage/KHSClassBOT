#!/usr/bin/env bash

set -e
set -x

flake8 run.py app cogs
