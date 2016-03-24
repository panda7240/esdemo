# -*- coding:utf-8 -*-

from flask import Flask
from flask.ext.bootstrap import Bootstrap

from config import config
from elasticsearch import Elasticsearch

bootstrap = Bootstrap()

es = None


def create_app(config_name):
    app = Flask(__name__)
    bootstrap.init_app(app)

    global es
    es = Elasticsearch(config[config_name].ES_HOSTS, sniff_on_start=True, sniff_on_connection_fail=True,
                       sniffer_timeout=60)

    from app.main.controller.auth_controller import auth_blueprint

    app.register_blueprint(auth_blueprint)

    from app.main.controller.message_controller import message_blueprint

    app.register_blueprint(message_blueprint, url_prefix='/message')

    return app
