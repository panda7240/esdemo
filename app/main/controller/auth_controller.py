# -*- coding:utf-8 -*-
import logging
from config import Config
from flask import render_template, session, redirect, url_for, current_app, request, Blueprint

auth_blueprint = Blueprint('auth_blueprint', __name__)

logger = logging.getLogger('auth_controller')

@auth_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')






