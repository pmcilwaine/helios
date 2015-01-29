#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helios.admin import views
from flask import Flask, url_for, Response
import pytest


@views.admin.route('/poll')
def poll():
    return Response(response=dict(msg='Hello World'))


@pytest.fixture
def app():
    my_app = Flask('test')
    my_app.register_blueprint(views.admin)
    return my_app


def test_blueprint_name():
    assert views.admin.name == 'admin'


def test_after_response(client):
    print client.get(url_for('admin.poll')).__dict__
    assert False
