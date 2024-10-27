import logging.config

logConfiguration = {
    'version': 1,
    'loggers': {
        'debugLog': {
            'level': 'DEBUG',
            'handlers': ['debugHandler']
        },
        'errorLog': {
            'level': 'ERROR',
            'handlers': ['errorHandler']
        },
        'infoLog': {
            'level': 'INFO',
            'handlers': ['infoHandler']
        },
        'userLog': {
            'level': 'INFO',
            'handlers': ['userHandler']
        }
    },
    'handlers': {
        'debugHandler' : {
            'class': 'logging.FileHandler',
            'filename': 'logs/systemLogs.txt',
            'level': 'DEBUG',
            'formatter': 'completeFormat'
        },
        'errorHandler' : {
            'class': 'logging.FileHandler',
            'filename': 'logs/systemLogs.txt',
            'level': 'ERROR',
            'formatter' : 'logFormat'
        },
        'infoHandler' : {
            'class': 'logging.FileHandler',
            'filename': 'logs/systemLogs.txt',
            'level': 'INFO',
            'formatter' : 'logFormat'
        },
        'userHandler' : {
            'class': 'logging.FileHandler',
            'filename': 'logs/modificationsList.txt',
            'level': 'INFO',
            'formatter' : 'userFormat'
        }
    },
    'formatters': {
        'logFormat': {
            'format' : "%(asctime)s - %(levelname)s - %(message)s"
        },
        'userFormat': {
            'format' : "%(message)s"
        },
        'completeFormat': {
            'format' : "%(asctime)s - %(levelname)s - %(message)s - %(pathname)s - %(module)s - %(lineno)d - %(process)d - %(thread)d"
        }
    }
}

logging.config.dictConfig(logConfiguration)
sysLog = logging.getLogger('infoLog')