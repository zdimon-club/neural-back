Chat video streaming
====================

Publish video
-------------

**chat/components/base**

Turning your camera on/off.

.. code::

  doTurn(data: boolean) {
    if (data) {
      this.is_video = true;
      this.media_service.getMedia();
    } else {
      this.is_video = false;
      this.media_service.disconect();
    }
  }
  // media  service
  public disconect() {
    if (this.session) {
      this.session.disconnect();
      this.cameraOff().subscribe(() => {});
    }
  }

TODO(front):(3) Not always camera and streaming get disabled by this.session.disconnect()



