Start chat
==========

room.tasks.send_update_contacts
===============================

.. code:: python

    sids = UserOnline.get_sids_by_user(user)
    for s in sids:
        data = {
                'task': 'put_to_socket',
                'data': {
                    'socket_id': s,
                    'action': 'server-action:update_contacts'
                }
        }
        redis_client.publish('notifications',json.dumps(data))


chat.models.ChatRoom.check_is_active_by_message
===============================================

.. automodule:: chat.models.ChatRoom.check_is_active_by_message
    :members: 

chat.tasks.sent_chat_message
============================

.. automodule:: chat.tasks.sent_chat_message

.. code:: python

    man = room.get_payer()
    sids = UserOnline.get_sids_by_user(man)
    data = {
        'task': 'send_chat_message_to_sids',
        'sids': sids,
        'data': detail_room(room,man)
    }
    redis_client.publish('notifications',json.dumps(data))

    ######send to woman

    woman = room.get_woman()
    sids = UserOnline.get_sids_by_user(woman)
    data = {
        'task': 'send_chat_message_to_sids',
        'sids': sids,
        'data': detail_room(room,woman)
    }
    redis_client.publish('notifications',json.dumps(data))

