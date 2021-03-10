#!/usr/bin/env bash

set -e
set -x

isort run.py app cogs --check-only