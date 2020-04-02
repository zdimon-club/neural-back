Architecture
=============


Graph
=====

.. image:: images/server.png


Authorization
=============

Authorization form auth/login/login.component.ts


.. code:: javascript

  login(){
    this.login_service.login({'username': this.user.username, 'password': this.user.password});
  }



