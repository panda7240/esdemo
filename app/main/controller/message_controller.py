# -*- coding:utf-8 -*-
import json
import time
import app
from elasticsearch.client import IndicesClient
from flask import render_template, session, redirect, url_for, current_app, request, Blueprint

message_blueprint = Blueprint('message_blueprint', __name__)



@message_blueprint.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('message/index.html')

