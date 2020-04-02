Chat API.
=========

Adding room.
------------

.. autoclass:: chat.views.room.AddRoomView

METHOD: POST

URL: room/add 

INPUT: json

.. code::

    {owner: int, abonent: int}

OUTPUT:


.. code::

    {
        "abonent_id":26,
        "id":14,
        "is_current":true,
        "is_active":false,
        "is_low_account":false,
        "activity":1575295588.831875,
        "messages":{ "90":
                      {
                        "id":90,
                        "message":"...",
                        "author_id":7,
                        "created":"",
                        "is_readed":false
                        } ... 
                    }
    }


List of rooms.
--------------

.. autoclass:: chat.views.room.RoomList

METHOD: GET

URL: room/list

Input: None

Output:

.. code::

    {
    contact_users: {
    7: { id: 7, 
         account: "0", 
         language: "en", 
         gender: "male", 
         username: "man6", 
         email: "man6@gmail.com",…}
    }
    contacts_ids: [23, ...]
    current_room: 14
    online_ids: [2,...]
    room_ids: [12,...]
    rooms: { 
             12: {
                abonent_id: 23
                activity: 1575202813
                id: 12
                is_active: false
                is_current: false
                is_low_account: false
                messages: {
                    14: {
                        abonent_id: 26, 
                        id: 14, 
                        is_current: true, 
                        is_active: false, 
                        is_low_account: false,…}
                }
             }

Sending the message.
--------------------

.. autoclass:: chat.views.message.SendMessageView

METHOD: POST

URL: room/list

Input: 

.. code::

    {
        author: {
            account: "0"
            email: "man6@gmail.com"
            gender: "male"
            groups: []
            id: 7
            is_camera: false
            is_online: true
            is_superuser: false
            language: "en"
            last_feed: {
                id: 35, 
                title: "Test feed of man6 5", 
                main_media: { id: 173, 
                                type_media: "photo", orient: "port",…
                            }
                }

            main_photo: "...jpg"
            middle_photo: "....jpg"
            token: "28e3ba29c14d059c625492747cad7a27d6a3b9d4"
            username: "man6"
        }
            created: "2019-12-02T14:19:34.569Z"
            message: "vdsvdsvsd"
            room_id: 14
    }

Output:

.. code::

    {
        abonent_id: 26
        activity: 1575296374.5969613
        id: 14
        is_active: false
        is_current: true
        is_low_account: false
        messages: {
            90: {
                id: 90, 
                message: "cqwcwcw", 
                author_id: 7, 
                created: "2019-12-02 14:08:13.574211+00:00",…}
            ,…}
       
    }


Selecting room.
---------------

.. autoclass:: chat.views.room.SelectRoomView

METHOD: GET

URL: room/select/id:int

Output: 

.. code::

    {
        contact_users: {23:{}…}
        contacts_ids: [23, 26, 7]
        current_room: 12
        online_ids: [45,..]
        room_ids: [12, 14]
        rooms: {12: {}...} 
    }



Suspending room.
-----------------

.. autoclass:: chat.views.room.StopRoomView

METHOD: GET

URL: room/stop/id:int

Output: 

.. code::

    {status: 0, message 'Ok'}


Turning streamer video ON.
--------------------------

.. autoclass:: webrtc.views.CameraOnView

METHOD: GET

URL: webrtc/cameraOn

Input: None

Output: 

.. code::

    {"camera_on":"ok"}


Turning streamer video OFF.
---------------------------

.. autoclass:: webrtc.views.CameraOffView

METHOD: GET

URL: webrtc/cameraOff

Input: None

Output: 

.. code::

    {"camera_off":"ok"}

