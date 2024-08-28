TORTOISE_ORM = {
        "connections": {
            'default':{
                # "db_url": "mysql://user:password@host:3306/database",
                'engine': 'tortoise.backends.mysql',
                'credentials': {
                    'host': 'localhost',
                    'port': 3306,
                    'user': 'root',
                    'password': 'admin@123',
                    'database': 'fastapi_test',
                }
            }
        },
        "apps": {
            "models": {
                "models": ["models", "aerich.models"],
                "default_connection_name": "default",
            }
        },
        'use_tz': False,
        'timezone': 'Asia/Shanghai',
    }