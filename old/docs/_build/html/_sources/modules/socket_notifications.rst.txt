Socket messaging
-----------------

Sending message from Django to Redis.


**Message about someone gets online to the notifications channel**

.. code::

    redis_client = redis.Redis(host='localhost', port=6379, db=4)

    data = {
    'task': 'user_online',
    'user': {...}
    }
    redis_client.publish('notifications',json.dumps(data))




Processing this message inside soxket server to broadcust the message to all online users.

.. code::

        if data['task'] == 'user_offline' or data['task'] == 'user_online' or data['task'] == 'update_user':
            await sio.emit('server-action:update_user_online',data

TODO(back): create the dispacher for different types of actions with loggining.


**Notification from the server to the defenite SIDs**

.. code::

    man = room.get_payer()
    sids = UserOnline.get_sids_by_user(man)
    data = {
        'task': 'send_chat_message_to_sids',
        'sids': sids,
        'data': detail_room(room,man)
    }
    redis_client.publish('notifications',json.dumps(data))

**Processing this messages in the socket server**


.. code::

        if data['task'] == 'send_chat_message_to_sids':
            print('send_chat_message_to_sids')
            for sid in data['sids']:
                print('send_chat_message_to_sids: %s ' % sid)
                payload = {
                    'data': data
                    }
                await sio.emit('server-action:chat_message',payload, room=sid)

**Sending message to the one SID**

.. code::

    def send_update_contacts(user):
        '''
           Updating contact list of users after first message.

           @Input: user object.
        '''
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

**Processing in the socket server**

.. code::

        if data['task'] == 'put_to_socket':
            payload = {
                'data': data['data']
            }
            print('sending to %s' % data['data']['socket_id'])
            await sio.emit(data['data']['action'], payload, room=data['data']['socket_id'])



Recieving notification from angular.

.. code::

    user_online$: Observable<any> = this.socket.fromEvent<string>('server-action:update_user_online');


  ....

  this.service.user_online$.subscribe(data => {...})




