Sahana Eden - Humanitarian platform
===================================

`Sahana Eden`_ is an Emergency Development ENvironment platform for
rapid deployment of humanitarian response management. Its rich feature
set can be rapidly customized to adapt to existing processes and
integrate with existing systems to provide effective solutions for
critical humanitarian needs management either prior to or during a
crisis.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Sahana Eden configurations:
   
   - Installed from upstream source code to /var/www/sahana-eden
   - Serve web2py applications with WSGI on Apache.
   - Force admin console to be served via SSL.

   **Security note**: Updates to Sahana-Eden may require supervision so
   they **ARE NOT** configured to install automatically. See below for
   updating Sahana-Eden.

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, MySQL and Postfix.

Supervised Manual Sahana-Eden Update
------------------------------------

Always ensure that you have a tested working backup before you start.
To upgrade to the latest version of Sahana-Eden from the command line::

    cd /var/www/web2py/applications/eden
    git pull origin

Database updates may also be required, see `Sahana-Eden docs`_ for 
further details.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**
-  Web2Py: username **admin**
-  Sahana Eden: email set at firstboot


.. _Sahana Eden: http://sahanafoundation.org/products/eden/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Sahana-Eden docs: http://eden.sahanafoundation.org/wiki/UserGuidelines/Admin/Upgrade
