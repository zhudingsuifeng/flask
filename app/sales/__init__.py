# coding = utf-8

__author__ = 'fly'

from flask import Blueprint

sales = Blueprint('sales', __name__)

from . import views