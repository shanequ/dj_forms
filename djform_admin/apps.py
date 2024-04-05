
from django.contrib.admin.apps import AdminConfig


class DjFormAdminConfig(AdminConfig):
    """This class is referred in INSTALLED_APP of settings.py

    It is used to define which admin site is the default admin site for apps,
    which also replaces 'django.contrib.admin'.

    For all other apps, admin.py can still refer 'django.contrib.admin' as
    the default admin site has been substituted.
    """
    default_site = 'djform_admin.admin.DjFormAdmin'
