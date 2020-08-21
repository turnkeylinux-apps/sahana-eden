#!/usr/bin/python3
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
import subprocess

from dialog_wrapper import Dialog


def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
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

    update_script = 'db(db.auth_user.id == 1).update(email="%s",password=db.auth_user.password.validate("%s")[0]);db.commit();' % (email, password)
    subprocess.run(["python3", "web2py.py", "-S", "eden", "-M", "-P"], cwd='/var/www/web2py', input=update_script.encode('utf-8'))

if __name__ == "__main__":
    main()
