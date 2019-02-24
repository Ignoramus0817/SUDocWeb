import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'SUDoc.settings'; import django
if django.VERSION <= (1, 5):
    from django.core import management
    import SUDoc.settings as settings
    management.setup_environ(settings)
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
make migration
syncdb
clear
cls
manage.py makemigration
