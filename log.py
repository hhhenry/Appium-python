import logging

class Log():

    def sgLog(self,msg):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        #create handler,write log
        filename = "/Users/henry/test/autoTest/sgLog.log"
        fh = logging.FileHandler(filename)
        #Define the output format of formatter handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.info(msg)
        self.logger.removeHandler(fh)
