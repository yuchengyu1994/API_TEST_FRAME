#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/26 0026 19:40
from nb_log import LogManager

logger=LogManager('Yu').get_logger_and_add_handlers()

logger.info('通知')
logger.warning('警告')
logger.error('错误')