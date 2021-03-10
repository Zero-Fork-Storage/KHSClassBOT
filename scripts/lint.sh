#!/usr/bin/env bash

set -e
set -x

./flake8.sh && ./black.sh && ./isort.sh && exit 0

exit 1