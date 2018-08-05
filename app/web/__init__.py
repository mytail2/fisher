#!/usr/bin/env python
from flask import Blueprint


web = Blueprint('web', __name__)

from . import book


