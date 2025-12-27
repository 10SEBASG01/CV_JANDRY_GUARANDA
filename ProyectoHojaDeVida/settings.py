import os
import dj_database_url
from pathlib import Path

# Directorio Base
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-ww9j7_=ac%06&-rvo27ci!8f)0^2)+o-m8@1+i^bxys)=%l0@2')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Render Hostnames
ALLOWED_HOSTS = ['*']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', 
    'django.contrib.staticfiles',
    'cloudinary_storage', # Librería de Cloudinary
    'cloudinary',          # Librería de Cloudinary
    'Perfil',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProyectoHojaDeVida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoHojaDeVida.wsgi.application'

# BASE DE DATOS
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS (CSS, JS)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# CONFIGURACIÓN DE ALMACENAMIENTO (Cloudinary para Media, Whitenoise para Static)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('dtec003kq'),
    'API_KEY': os.environ.get('183879747524985'),
    'API_SECRET': os.environ.get('p_rDwIgxZLMDphK9eEp__Z7kJbk'),
}

# Si están configuradas las credenciales de Cloudinary, las usamos
if all([CLOUDINARY_STORAGE['CLOUD_NAME'], CLOUDINARY_STORAGE['API_KEY'], CLOUDINARY_STORAGE['API_SECRET']]):
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    MEDIA_URL = '/media/' # Cloudinary maneja esto automáticamente
else:
    # Local si no hay variables configuradas
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

# Whitenoise siempre para Static
STORAGES = {
    "default": {
        "BACKEND": DEFAULT_FILE_STORAGE if 'DEFAULT_FILE_STORAGE' in locals() else "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Idioma y Hora
LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil' 
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Permite cargar PDFs en iframes
X_FRAME_OPTIONS = 'SAMEORIGIN'