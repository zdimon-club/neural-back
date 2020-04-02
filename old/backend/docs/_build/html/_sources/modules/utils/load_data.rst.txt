Loading data
============

Command for seeding DB.

.. code::

    ./bin/seeddb

Order of seeding

.. code::

    . ./venv/bin/activate
    cd backend
    rm db.sqlite3
    ./manage.py migrate
    ./manage.py load_users
    ./manage.py load_media
    ./manage.py load_feed
    ./manage.py convert_video
    ./manage.py load_payment
    ./manage.py load_props
    ./manage.py load_messages
    ./manage.py load_settings
    ./manage.py load_stickers
    ./manage.py load_agency
    ./manage.py load_category
    ./manage.py load_product    

Loading users
-------------

.. autoclass:: account.management.commands.load_users.Command

.. automodule:: account.management.commands.load_users
   :members: load_photo, users_fabric

Loading user`s media content
----------------------------

.. autoclass:: usermedia.management.commands.load_media.Command

.. automodule:: usermedia.management.commands.load_media
   :members: load_public_photo, load_private_photo, load_buffer_photo, load_video

Loading user`s feed content
----------------------------

.. autoclass:: feed.management.commands.load_feed.Command

.. automodule:: feed.management.commands.load_feed
   :members: load_comments, load_feed


Loading agencies
----------------

.. autoclass:: agency.management.commands.load_agency.Command

.. automodule:: agency.management.commands.load_agency
   :members: load_photo, users_fabric, add_w