Users online.
=============

List of users online
--------------------

.. autoclass:: online.views.UserOnlineListView


Output:

.. code::

   {
    "users_ids": [
        24,
        25
    ],
    "users": {
        "24": {
            "id": 24,
            "url": "http://localhost:8085/profiles/24/",
            "account": 0,
            "username": "woman4",
            "email": "woman4@gmail.com",
            "groups": [],
            "is_superuser": false,
            "is_edit": false,
            "main_photo": "http://localhost:8085/media/user_photo/24_Ba9PyMS.jpeg.100x100_q95_box-138%2C0%2C962%2C825_crop-smart_upscale.jpg",
            "is_online": true
        },
        "25": {
            "id": 25,
            "url": "http://localhost:8085/profiles/25/",
            "account": 0,
            "username": "woman5",
            "email": "woman5@gmail.com",
            "groups": [],
            "is_superuser": false,
            "is_edit": false,
            "main_photo": "http://localhost:8085/media/user_photo/25_YCAHUqA.jpeg.100x100_q95_box-115%2C0%2C805%2C690_crop-smart_upscale.jpg",
            "is_online": true
        }
    },
    "users_list": [
        {
            "id": 24,
            "url": "http://localhost:8085/profiles/24/",
            "account": 0,
            "username": "woman4",
            "email": "woman4@gmail.com",
            "groups": [],
            "is_superuser": false,
            "is_edit": false,
            "main_photo": "http://localhost:8085/media/user_photo/24_Ba9PyMS.jpeg.100x100_q95_box-138%2C0%2C962%2C825_crop-smart_upscale.jpg",
            "is_online": true
        },
        {
            "id": 25,
            "url": "http://localhost:8085/profiles/25/",
            "account": 0,
            "username": "woman5",
            "email": "woman5@gmail.com",
            "groups": [],
            "is_superuser": false,
            "is_edit": false,
            "main_photo": "http://localhost:8085/media/user_photo/25_YCAHUqA.jpeg.100x100_q95_box-115%2C0%2C805%2C690_crop-smart_upscale.jpg",
            "is_online": true
        }
    ]
    }

Update socket id
----------------


.. autoclass:: online.views.UpdateSocketIdView


Output:

.. code::

    {'status': 1, 'message': 'not authenticated'}

    or 

    {'status': 0, 'message': 'OK'}