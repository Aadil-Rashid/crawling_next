import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
