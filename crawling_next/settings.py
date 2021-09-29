# import os
# from decouple import config
# from split_settings.tools import include, optional


from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/auth.py',
    'components/common.py',
    'components/database.py',
    'components/email.py',
    'components/logging.py',
    'components/static.py',
    'components/templates.py',


    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    'environments/%s.py' % ENV,


    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)




# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ENV = config('DJANGO_ENV', 'local')
# ADD_CORS = ENV in ["development", 'local']

# base_settings = [
#     'components/auth.py',
#     'components/common.py',
#     'components/database.py',
#     'components/email.py',
#     'components/logging.py',
#     'components/static.py',
#     'components/templates.py',

#     # Select the right env:
#     'environments/%s.py' % ENV,
# ]

# if True:
#     base_settings += ['components/cors.py']

# # Include settings:
# include(*base_settings)