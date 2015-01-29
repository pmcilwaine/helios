#!/bin/bash

ROOT_DIR=$(dirname $0)../

pylint --rcfile=${ROOT_DIR}/ci/pylintrc
