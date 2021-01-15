import os


class base_config(object):
    """Default configuration options."""

    SITE_NAME = os.environ.get('APP_NAME', 'OT Glossary')
    SITE_VERSION = '1.0'
    SITE_DATABASE = 'CSV data source'

    SUPPORTED_LOCALES = ['en']
    ABS_PREFIX = '/ottoli'

    FORMAT_DATE = '%Y-%m-%d'
    FORMAT_DATETIME = '%Y-%m-%d %H:%M'
class dev_config(base_config):
    """Development configuration options."""
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
