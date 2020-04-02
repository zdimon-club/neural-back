Registartion.
=============

Man registration.
------------------

.. autoclass:: account.views.registration.RegisterMan

METHOD: POST

URL: account/register/man

Input:

.. code::

   {email: "email@gmail.com"}


Output:

.. code::

   {"status":0,"message":"Ok"}

  
Woman registartion.
-------------------

.. autoclass:: account.views.registration.RegisterWoman

METHOD: POST

URL: account/register/woman

Input:

.. code::

    {
        about_me: "csdcsdc"
        alkohol: 22
        birthday: "2019-12-09T22:00:00.000Z"
        children: 29
        city: "dcsdcsd"
        constitution: 18
        email: "cewc@ddd.dd"
        eye_color: 9
        goal: "sdc sdcsd"
        hair_color: 6
        height: 41
        hobby: 35
        images: [,…]
        job: "sdcsdc sdc"
        language: [false, false, false]
        lookingfor: "csdcsdc"
        marital: 15
        name: "ewcwe"
        photo: "C:\fakepath\Main.jpg"
        race: 33
        religion: 38
        smoking: 25
        weight: 12
        images: [
        0: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
        ]
    }

Output:

.. code::

    {"status":0,"message":"Ok", "id": 2}


Agency registartion.
--------------------

.. autoclass:: account.views.registration.RegisterAgencyView

METHOD: POST

URL: account/register/agency

Input:

.. code::

    {
        address: ".."
        city: ".."
        count_woman: "...."
        country: "..."
        email: "ddsds@xxs.dd"
        images: [
        0: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
        ]
        login: "..."
        name: "..."
        name_boss: "..."
        password: "..."
        phone1: "..."
        phone2: "...."
        photo: "C:\fakepath\AP_16274338441108.jpg"
        skype: "sacas"
        working_time: "412412"
    }

Output.

.. code::

    {"status":0,"message":"Ok", "id": 2}