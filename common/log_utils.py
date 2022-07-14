import os
import time
import logging
from common.config_utils import read_config

current_path=os.path.dirname(__file__)
log_path= os.path.join(current_path, '..',read_config.get_log_path)
class LogUtils:
    def __init__(self,logger=None):
        self.logfile_name=os.path.join(log_path,'ApiTest_%s.log'% time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger(logger)
        # self.logger.handlers.clear()
        self.logger.setLevel(read_config.get_log_level)
        self.file_log = logging.FileHandler(self.logfile_name,'a',encoding='utf-8')
        self.file_log.setLevel(read_config.get_log_level)
        self.log_console = logging.StreamHandler()
        self.log_console.setLevel(read_config.get_log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.file_log.setFormatter(formatter)
        self.log_console.setFormatter(formatter)
        self.logger.addHandler(self.file_log)
        self.logger.addHandler(self.log_console)
        self.file_log.close()
        self.log_console.close()

    def get_log(self):
        return self.logger

    # def info(self,info_msg):
    #     self.logger.info(info_msg)
    #
    # def error(self,error_msg):
    #     self.logger.error(error_msg)

log_pri = LogUtils().get_log()
if __name__=='__main__':
    log_pri.warning('newdream123')
    log_pri.info('123')
    log_pri.error('321')
    # log1.error('1234')


