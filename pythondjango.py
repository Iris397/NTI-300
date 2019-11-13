#!/usr/bin/python
import os
import re
import subprocess
def setup_install():
    print('installing pip and virtualenv so we can give django its own version of python')
    os.system('yum -y install python-pip && pip install --upgrade pip')
    os.system('pip install virtualenv')
    os.chdir('/opt')
    os.mkdir('/opt/django')
    os.chdir('/opt/django')
    os.system('virtualenv django-env')
    os.system('chow -R yalixue /opt/django')    # we're useing shell, because the python builtin chown doesn't work as well
def django_install():
    print('ativating virtualenv and installing django after pre-requirements have been met')
                                                # you must activate the virtualenv shell every time  you perform a command in order for it to work from python.
    os.system('souce /opt/django/django-env/bin/activate '+ \
              '&& django-admin --version ' + \
              '&& django-admin startproject project1') 
def django_start():
    print('starting django')
    os.system('chown -R yalixue /opt/django')
    os.chdir('/opt/django/project1')
    os.system('source /opt/django/django-env/bin/activate '+ \
              '&& python  manage.py migrate')
    os.system('source /opt/django/django-env/bin/activate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(\'admin\',\'admin@newproject.com\',\NTI300NTI300\')" | python manage.py shell')
    outputwithnewline = subprocess.check_output('curl -s checkip.dyndns.org | sed -e \'s/.*Current IP Address: //\' -e \'s/<.*$//\'',shell=True)
    print outputwithnewline
    output = outputwithnewline.replace("\n","")
    old_string = "ALLOWED_HOSTS = []"
    new_string = 'ALLOWED_HOSTS = [\'{}\'}'.format(output)
    print (new_string)
    print (old_string)
    with open('project1/settings.py') as f:
      newText=f.read().replace(old_string, new_string)
      f.write(newText)
    os.system('sudo -u yalixue sh -c "source/opt/django/django-env/bin/activate && python manage.py runserver 0.0.0.0:8000&" ')
setup_install()
django_install()
django_start()
