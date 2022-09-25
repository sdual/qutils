from qutils.log import get_logger

logger = get_logger(__name__)

def main():
    raise ValueError('hoge')


if __name__ == '__main__':
    try:
        main()
    except:
        logger.exception('batch error.')
