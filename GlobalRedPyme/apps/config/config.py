# environ init
import os
import environ

env = environ.Env()

# Establecer el directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tomar variables de entorno del archivo .env
environ.Env.read_env(os.path.join(BASE_DIR, '../GlobalRedPyme/.env'))

PRODUCTION=False

#VARIABLES GLOBALES
endpointEmailAsignacionPassword="/grp/asignacionPassword/"
endpointEmailReseteoPassword="/grp/reseteoPassword/"

#VARIABLES VARIAN DE ACUERDO A PRODUCCION O DESARROLLO
if PRODUCTION:
    # URL BACK END
    # API_BACK_END = '209.145.61.41:8002/'
    API_BACK_END = 'https://api.bigpuntos.com/'
    #URL FRONT END
    API_FRONT_END="https://center.bigpuntos.com/#"
    API_FRONT_END_CENTRAL="https://bigpuntos.com/#"
    API_FRONT_END_CREDIT="https://credit.bigpuntos.com/#"
    #TIEMPO DE EXPIRACION DE TOKEN (EN SEGUNDOS)
    TOKEN_EXPIRED_AFTER_SECONDS = 86400
    #NOMBRE KEYWORK TOKEN
    TOKEN_KEYWORD= 'Bearer'
    # This will display email in Console.
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = ''
    # CONFIGURACION DE TWILIO
    TWILIO_ACCOUNT_SID = ''
    TWILIO_AUTH_TOKEN = ''

    # CONFIGURACION DE AMAZON S3
    DEFAULT_FILE_STORAGE = ''
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_STORAGE_BUCKET_NAME = ''
    #CORS
    CORS_ALLOWED_ORIGINS = tuple(env.list('CORS_ALLOWED_ORIGINS'))
    #databases
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'grp_central',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_personas_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_core_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_core',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_pymes_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_pymes',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_corp_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_corp',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_mdm_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_mdm',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_mdp_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_mdp',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_mdo_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_mdo',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_gdo_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_gdo',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_gde_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_gde',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
    }
else:
    # URL BACK END
    API_BACK_END = 'http://127.0.0.1:8000/'
    #URL FRONT END
    API_FRONT_END="http://localhost:4203"
    API_FRONT_END_CENTRAL="http://localhost:4201"
    API_FRONT_END_CREDIT="http://localhost:4205"
    #TIEMPO DE EXPIRACION DE TOKEN (EN SEGUNDOS)
    TOKEN_EXPIRED_AFTER_SECONDS = 86400
    #NOMBRE KEYWORK TOKEN
    TOKEN_KEYWORD= 'Bearer'
    # This will display email in Console.
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = ''
    # CONFIGURACION DE TWILIO
    TWILIO_ACCOUNT_SID = ''
    TWILIO_AUTH_TOKEN = ''

    # CONFIGURACION DE AMAZON S3
    DEFAULT_FILE_STORAGE = ''
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_STORAGE_BUCKET_NAME = ''
    #CORS
    CORS_ALLOWED_ORIGINS = tuple(env.list('CORS_ALLOWED_ORIGINS'))
    #databases
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_central',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_personas_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_personas',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_core_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_core',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_pymes_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_pymes',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_corp_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_corp',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_mdm_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_mdm',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_mdp_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_mdp',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_mdo_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_mdo',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_gdo_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_gdo',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_gde_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas_gde',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
    }
