from base import *

DEBUG = True
 
# For Development uncomment below
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'staticfiles'),
) 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'