Video striming
==============
    
1.
==

url: webrtc/cameraOn

.. automodule:: webrtc.views.CameraOnView

2.
==

url: webrtc/cameraOff

.. automodule:: webrtc.views.CameraOffView

3.
==

url: webrtc/cameraShow

CameraShowView
==============

.. automodule:: webrtc.views.CameraShowView

webrtc.views.OfferView
======================

.. automodule:: webrtc.views.OfferView

webrtc.models.Connection.set_offer
==================================

.. automodule:: webrtc.models.Connection.set_offer

webrtc.views.AnswerView
=======================

url: /webrtc/answer

.. automodule:: webrtc.views.AnswerView

webrtc.views.IceView
=======================

url: /webrtc/ice

.. automodule:: webrtc.views.IceView


.. uml::

   actor Man
   actor Woman
   collections Django
   collections Socket


   group 1. Woman turn cam ON
	   Woman -> Django: Click cam btn
	   Django -> Socket: Broadcast {update_user}
	   Socket -> Man: Broadcast {update_user}
   end

   group 2. Woman turn cam OFF
	   Woman -> Django: Click cam btn OFF
	   Django -> Socket: Broadcast {update_user}
	   Socket -> Man: Broadcast {update_user}
   end

   group 3. Man click Show video
	   Man -> Django: Click show btn
	   Django -> Socket: Broadcast {'action': 'server-action:show_cam'}
	   Socket -> Woman: {'action': 'server-action:show_cam'}
       Woman -> Django: webrtc.sendOffer {user_id, offer}
       Django -> Socket: 'action': 'server-action:put_offer'
       Socket -> Man: 'action': 'server-action:put_offer'
       Man -> Django: webrtc.sendAnswer{room_id, answer}
       Django -> Socket: action: 'server-action:put_answer'
       Socket -> Woman: action: 'server-action:put_answer'

       Woman -> Django: webrtc.sendIce({room_id,ice,dest=abonent})
       Django -> Socket: action': 'server-action:put_ice'
       Socket -> Man: action': 'server-action:put_ice'

       Man -> Django: webrtc.sendIce({room_id,ice,dest=owner})
       Django -> Socket: action': 'server-action:put_ice'
       Socket -> Woman: action': 'server-action:put_ice'

       
   end 