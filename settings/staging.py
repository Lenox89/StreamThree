from base import *

DEBUG = False

# For Production uncomment below
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

STATIC_URL = '/staticfiles/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'staticfiles'),
) 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'