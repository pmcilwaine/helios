#!/bin/bash

ROOT_DIR=$(dirname $0)../

cd helios

tox -r -c tox.ini
