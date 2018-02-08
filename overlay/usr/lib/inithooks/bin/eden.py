#!/usr/bin/python
"""Set Sahana Eden admin email and password

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively
"""

import os
import re
import sys
import getopt
import inithooks_cache
import time
import hashlib

from dialog_wrapper import Dialog
from executil import system


def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    domain = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val
    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Sahana Eden Password",
            "Enter new password for the Sahana Eden 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Sahana Eden Email",
            "Enter email address for the Sahana Eden 'admin' account.",
            "admin@example.com")
    inithooks_cache.write('APP_EMAIL', email)

    update_script = "db(db.auth_user.id == 1).update(email=\"%s\",password=db.auth_user.password.validate(\"%s\")[0]);db.commit();" % (email, password)
    system("cd /var/www/web2py && echo '%s' | python web2py.py -S eden -M -P" % update_script)

if __name__ == "__main__":
    main()

