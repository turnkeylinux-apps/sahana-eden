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

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**
-  Web2Py: username **admin**
-  Sahana Eden: first registered user will become the
   administrative user account


.. _Sahana Eden: http://sahanafoundation.org/products/eden/
.. _TurnKey Core: https://www.turnkeylinux.org/core
