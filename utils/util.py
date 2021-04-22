import logging

logs = set()

def init_logging(name,level,filename,rank=0):
    """init logging
    Args:
        name: 'global' or 'local' ...
        level: logging.INFO
        filename: log file name
        rank: process id 
    Return:
    Example:
        init_logging('global',logging.INFO,'./test_env.log')
        logger = logging.getLogger('global')
        logger.info('test the log script!')
    """
    if (name,level) in logs:
        return
    log_format = '%(asctime)s [%(pathname)s line:%(lineno)d] %(levelname)s: %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO,)

    file_handler = logging.FileHandler(filename,'a+')
    file_handler.setFormatter(logging.Formatter(fmt=log_format))
    file_handler.setLevel(logging.INFO)
    logging.getLogger('global').addHandler(file_handler)
    logging.getLogger('global').addFilter(lambda record: rank == 0)

if __name__ == "__main__":
    init_logging('global',logging.INFO,'./test_env.log',0)
    logger = logging.getLogger('global')
    logger.info('test the log script!')