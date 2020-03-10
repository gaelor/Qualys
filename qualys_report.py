import sys
import logging

import qualysapi

a = qualysapi.connect(username='metsy5tc', password='63accPGklm@', hostname='qualysapi.qg2.apps.qualys.eu')

print a()