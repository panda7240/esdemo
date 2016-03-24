# -*- coding:utf-8 -*-
import logging

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    ES_CLUSTER_NAME = 'es_test'

    LOG_LEVEL = 'INFO'
    LOG_FILE_PATH = 'esdemo.log'

    # 创建一个root logger
    logger = logging.getLogger('')
    # 创建一个handler，用于写入日志文件
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    # 再创建一个handler，用于输出到控制台
    console_handler = logging.StreamHandler()
    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    estracer = logging.getLogger('elasticsearch.trace')
    estracer.setLevel(logging.INFO)
    estracer.addHandler(logging.FileHandler('es_trace.log'))

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    Config.logger.setLevel(logging.DEBUG)
    ES_HOSTS = [{"host": "127.0.0.1", "port": 9201}, {"host": "127.0.0.1", "port": 9202}]


class TestingConfig(Config):
    TESTING = True
    Config.logger.setLevel(logging.DEBUG)
    ES_HOSTS = [{"host": "127.0.0.1", "port": 9201}, {"host": "127.0.0.1", "port": 9202}]


class ProductionConfig(Config):
    Config.logger.setLevel(logging.INFO)
    ES_HOSTS = [{"host": "127.0.0.1", "port": 9201}, {"host": "127.0.0.1", "port": 9202}]


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}


