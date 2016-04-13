sentry-sso-google
=================

Google SSO support for Sentry 7.5 and above.

Usage
-----

Add ``sentry_sso_google`` to your Sentry config's ``INSTALLED_APPS``.

The following settings are required to be in your Sentry configuration.
You can create a new project in the `Developers
Console <https://console.developers.google.com>`__. From there, go to
APIs & Auth, Credentials and get the credentials for a web application.
You will also need to enable 'Google+ API' in the APIs section.

-  ``GOOGLE_OAUTH2_CLIENT_ID``
-  ``GOOGLE_OAUTH2_CLIENT_SECRET``

You can limit who can sign into Sentry using this provider by setting
the ``GOOGLE_WHITE_LISTED_DOMAINS`` to a list of allowed domains. For
example, to limit to ``educreations.com`` users, one could do:

.. code:: python

    GOOGLE_WHITE_LISTED_DOMAINS = ['educreations.com']

Instead, or, in addition, you can limit only certain emails to log in
using the ``GOOGLE_WHITE_LISTED_EMAILS`` setting. The setting should be
a list of emails that are checked. For example, to limit to a few users,
one could do:

.. code:: python

    GOOGLE_WHITE_LISTED_EMAILS = [
        'chris.streeter@educreations.com',
        'corey.farwell@educreations.com',
    ]

Once deployed, go to the 'Auth' section of your organization's sentry
settings. Click the 'Configure' next to 'Google'.

Copyright
---------

Copyright © 2015, Educreations, Inc under the MIT software license. See
LICENSE for more information.
