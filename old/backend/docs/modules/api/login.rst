Login and logout
================

Login.
------

.. autoclass:: account.views.auth.CustomAuthToken

METHOD: POST

URL: api-token-auth/

Input:

.. code::

    {   username: "wdw", 
        password: "dwdw", 
        socket_id: "c8b7ae71791b46339084945a94768c96"
    }


Output:

.. code::

   {"non_field_errors":["Unable to log in with provided credentials."]}

   {
        agent: "Mozilla/5.0..."
        sid: "1ba7263c206249648dd0bd5e7f92c556"
        token: "4473de9c59149d7f12682332e5bef50b5d515e8f"
        user: {id: 6, account: "0"...}
   }   

Logout.
-------


.. autoclass:: account.views.auth.LogoutView

METHOD: GET

URL: /logout

Output:

.. code::

    {'status': 0, 'message': 'Ok'}