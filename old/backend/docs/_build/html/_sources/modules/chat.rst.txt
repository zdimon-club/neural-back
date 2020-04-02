Chat logic
==========

Adding/creating chat room
-------------------------

Angular, calling the user to chat by caller id and callee id.

.. code:: javascript

  callToChat(user_id: number) {
    const data = {
      owner: this.current_user.id,
      abonent: user_id,
    };
    this.chat_service.addRoom(data).subscribe((res: any) => {
      this.router.navigate(['chat/room', res.id]);
    });
  }


HTTP POST request.

return this.http.post(`${environment.apiUrl}/room/add`,data);

Input data.

.. code:: javascript

    {owner:int, abonent:int}


Django view.

.. automodule:: chat.views.room.AddRoomView


.. code:: python

    def post(self, request, format=None):
        owner = UserProfile.objects.get(id=request.data['owner'])
        abonent = UserProfile.objects.get(id=request.data['abonent'])
        room = ChatRoom.get_room_or_create(owner,abonent)
        return Response(detail_room(room,request.user.userprofile))

Chat initialization
-------------------

**chat.components.base**

Constructor.

.. code::

  constructor(
    private router: Router,
    private user_store: Store<UserState>,
    private session_store: Store<SessionState>,
    private room_store: Store<RoomState>,
    private room_service: ChatService,
    private socket_service: SocketService,
    private media_service: MediaService,
    private session_service: SessionService,

  ) {

    this._unsubscribeAll = new Subject();

    // Set current user from store
    this.session_store.select(selectUser).subscribe(user => {
      this.current_user = user;
    });

    // select rooms (contacts from the store)
    this.rooms = this.room_store.select(getRoomList);

    this.media_service._publisher$.subscribe((publisher: StreamManager) => {
      this.publisher = publisher;
    });
    this.media_service._isloading$.subscribe((data: boolean) => {
      this.is_loading = data;
    });

    this.room_store.dispatch(new roomActions.GetRoomList());
    this.room_store.dispatch(new roomActions.RequestFavoriteUsers());
    this.room_store.dispatch(new roomActions.RequestOnlineUsers());


  }

**GetRoomList action**

Effect.

.. code::

      @Effect()
      roomList$ = this.actions$.pipe(
        ofType(roomActions.ActionTypes.GetRoomList),
        switchMap((action: any) => {
          return this.service.getRoomList().pipe(
            tap((payload: any) => this.userStore.dispatch(new UpdateUsers(payload.contact_users))),
            map((payload: any) => new roomActions.GetRoomListLoaded(payload))
          );
        })
      )

**RequestFavoriteUsers action**

Effect

Check if user not exists call RequestUser(userIds) whith array of ids.

.. code::

  @Effect()
  loadFavoriteUsers$ = this.actions$.pipe(
    ofType(roomActions.ActionTypes.RequestFavoriteUsers),
    switchMap((action: any) => {
      return this.service
        .getFavorites().pipe(
          withLatestFrom(this.userStore.select(selectUsersIds), (payload: any, store: any) => {
            const userIds = [];
            payload.forEach(key => {
                if (store.indexOf(key) === -1 ) {
                  userIds.push(key);
                }
            });
            if ( userIds.length > 0) {
              this.userStore.dispatch(new RequestUser(userIds));
            }
            return new roomActions.FavoriteUsersLoaded(payload);
          })
        );
    })
  );

**ngOnInit**

.. code::

   ngOnInit() {

    // this.users_online = this.room_store.select(getOnlineUserList);
    this.users_contact = this.room_store.select(getAllUserList);


    this.socket_service.update_contacts$
     .pipe(takeUntil(this._unsubscribeAll))
     .subscribe(data => {
      this.room_store.dispatch(new roomActions.GetRoomList());
     });
     // console.log(this.room_store);
  }

**GetRoomList action**

Effect

.. code::

  @Effect()
  roomList$ = this.actions$.pipe(
    ofType(roomActions.ActionTypes.GetRoomList),
    switchMap((action: any) => {
      return this.service.getRoomList().pipe(
        tap((payload: any) => this.userStore.dispatch(new UpdateUsers(payload.contact_users))),
        map((payload: any) => new roomActions.GetRoomListLoaded(payload))
      );
    })
  );

Reducer

.. code::

  case Actions.ActionTypes.GetRoomListLoaded:

    const rooms = {
      ...state,
      rooms_ids: action.payload.room_ids,
      rooms: action.payload.rooms,
      current_room: action.payload.current_room
    };
    return rooms;


TODO(front):(3) Update contacts without GetRoomList and getting all rooms from the server.

TODO(front):(3) Swith between chat rooms without SetCurrentRoom if this room exists in the store.

TODO(front):(2) Add a new message in the store before sending to the server.

Subscribing on the new message comming
--------------------------------------

**chat.components.room.onInit**

.. code::

    this.$_update_room = this.socket_service.update_room$.subscribe(data => {
      this.room_store.dispatch(new roomActions.UpdateRoom(data.data.data));
    });

TODO(front): (3) Subscribe on getting one message istead of the all messages in the room.

TODO(back): (3) Send one new message to the recipient instead of all messages when a new message comming.

TODO(back): Send the socket notification (message_delivered) to the sender about his message was sent to the destination.

TODO(front): Mark the message as readed after the notification (message_delivered).

TODO(front): (1) Block sending next message until current is not delivered.

TODO(front): (1) Block sending empty message.

Sending the message.
--------------------

Frontend

.. code:: javascript

  send(){
    let msg = {
      author: this.current_user,
      message: this.message,
      created: new Date(),
      room_id: this.room.id
    }

    //
    this.chat_service.sendMessage(msg).subscribe(data => {
      
    });
    this.message = '';
    setTimeout(this.scrollToBottom,500);
  }

**Server processing**
**chat.views.message.SendMessageView**

.. automodule:: chat.views.message.SendMessageView

  

Input data

{'author':obj, 'message':str, 'created':str, 'room_id':int}


.. code:: python

    def post(self, request, format=None):
        user = UserProfile.objects.get(id=request.data['author']['id'])
        room = ChatRoom.objects.get(pk=request.data['room_id'])

        # chek man empty account
        if user.account == 0 and user.gender == 'male':
            print('empty!!!!!')
            send_notify_about_low_account(user)
            return True

        m = ChatMessage()
        m.message = request.data['message']
        m.room = room
        m.user = user
        m.save()

        # check room activity to avoid loose money
        room.check_is_active_by_message(m)
        if room.check_first_message():
            send_update_contacts(room.get_abonent(user))

        # mark messages as readed forcurrent rooms
        if room.is_current(room.get_abonent(user)):
            m.mark_as_readed()

        sent_chat_message(room)
        return Response(detail_room(room,request.user.userprofile)


Updating chat contacts
----------------------

Server.

**chat.tasks**

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

Processing in the frontend side.

.. code:: 

  update_contacts$: Observable<any> = this.socket.fromEvent<string>(
    'server-action:update_contacts',
  );


.. uml::

   actor Man
   actor Woman
   collections System
   group First message from Man
	   Man -> System: First message
	   System -> Woman: Create a new contact at the first place
	   System -> Man: Taking credits
	   Woman -> System: Answer
	   System -> Man: Move the contact to the first place
   end

   group First message from Woman
	   Woman -> System: First message
	   System -> Man: Create a new contact at the first place
	   Man -> System: Answer
	   System -> Man: Taking credits
	   System -> Man: Move the contact to the first place
   end

   group 2 min Man idle
	   System -> Man: Stop taking credits
   end

   group Click stop button
   	System -> Man: Stop taking credits
   end
	
   group Send sticker
   	System -> Man: Take credits by sticker price
   end
	
   group Send pic
   	System -> Man: Take credits by pic price
   end

   group Camera
   	Woman -> System: Turn the cam on
	System -> Man: Take credits by cam price
	Man -> System: Turn the cam on
        System -> Man: Continue taking credits by the same cam price
   end
