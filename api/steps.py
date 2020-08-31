import logging


class Steps(object):
    def __init__(self, docstr):
        self.num = 1
        logging.info("\033[1;33;40m%s\033[0m" % docstr)

    def step(self, desc):
        logging.info("\033[1;33;40mStep %s: %s\033[0m" % (self.num, desc))
        self.num += 1

    def info(self, desc):
        logging.info("\033[1;37mINFO: %s\033[0m" % desc)