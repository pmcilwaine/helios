#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helios import app
from flask import Blueprint


def test_create_no_defined_blueprints():
    my_app = app.create_app()
    assert my_app.blueprints.keys() == ['admin']


def test_create_app_with_defined_blueprints():
    test_blueprint = Blueprint('test_blueprint', __name__)

    my_app = app.create_app(blueprints=(
        test_blueprint,
    ))

    assert set(my_app.blueprints.keys()) == {'test_blueprint', 'admin'}


def test_create_app_configure():

    class CONFIG(object):
        MY_CONFIG = False

    my_app = app.create_app(config=CONFIG)
    assert my_app.config['MY_CONFIG'] is False
