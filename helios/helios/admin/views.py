#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.after_request
def handle_response(response):
    return response
