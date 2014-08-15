# -*- coding: utf-8 -*-

"""
traceview.annotation

This module contains the objects associated with Annotation API resources.

http://dev.appneta.com/docs/api-v2/annotations.html

"""

from .resource import Resource


class Annotate(Resource):

    PATH = "log_message"

class Annotations(Resource):

    PATH = "annotations"
