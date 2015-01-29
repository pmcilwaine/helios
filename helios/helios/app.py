#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
from admin.views import admin


__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    admin,
)


def create_app(config=None, app_name=None, blueprints=None):
    """

    :type config: object | None
    :param config:
    :param app_name:
    :type blueprints: tuple | None
    :param blueprints:
    :return: A flask object
    :rtype: Flask
    """

    if not app_name:
        app_name = __name__

    if not isinstance(blueprints, tuple):
        blueprints = (blueprints, )

    blueprints += DEFAULT_BLUEPRINTS

    app = Flask(app_name)
    configure_app(app, config)
    configure_blueprints(app, blueprints)

    return app


def configure_app(app, config):
    """

    :type app: Flask
    :param app:
    :type config: object | None
    :param config:
    :return:
    """

    if config:
        app.config.from_object(config)


def configure_blueprints(app, blueprints):
    """

    :type app: Flask
    :type blueprints: tuple
    :param app:
    :param blueprints:
    :return:
    """

    for blueprint in blueprints:
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)
