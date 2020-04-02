Архитектура.

Авторизация.

При логине диспичиться два акшина.

        this.session_store.dispatch(new sessionActions.LogIn(data));

        this.session_store.dispatch(new sessionActions.SetSid({
          token: data.token,
          socket_id: user.socket_id,
        }));
