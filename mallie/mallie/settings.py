import os

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR,"public","static")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"public","media")
ADMIN_MEDIA_PREFIX = '/media/'
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, "templates"))

SECRET_KEY = 'nf*w4m45bkx+p^f-)u7ca82rj40!2$g05x2+f5#u$%4^pk@&kc'
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'tinymce',
    'about',
    'contact',
    'home',
    'investment',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mallie.urls'
WSGI_APPLICATION = 'mallie.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TINYMCE_JS_ROOT = '/media/tinymce/'
TINYMCE_JS_URL = os.path.join(MEDIA_URL, "tinymce/tinymce.min.js")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "advlist autolink lists link image charmap preview hr anchor pagebreak searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime nonbreaking save table contextmenu directionality paste textcolor",
    'menubar': 'false',
    'toolbar': "preview | undo redo | styleselect | bold italic underline | alignleft aligncenter alignright alignjustify | link image | forecolor backcolor | bullist numlist | outdent indent | table",
}
TINYMCE_SPELLCHECKER = True

try:
    from local_settings import *
except ImportError:
    pass
