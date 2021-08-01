Bot Valley
==========

![image](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter%0A%20%20:target:%20https://github.com/pydanny/cookiecutter-django/%0A%20%20:alt:%20Built%20with%20Cookiecutter%20Django)


Runs on Python 3.9.x and Django 3.1.13.

Purpose of the project
----------------------

This project is a test task of @BotValley. Techincal specification is
[here](https://telegra.ph/Testovoe-zadanie-BotValley-07-26).

Results
-------

Telegram bot at production. Link is
[here](https://t.me/valley_test_task_bot).

Link to the Django admin panel is
[here](https://alena-kono.space/zrhsMcJeJNXUnXuKKPCSSoAFkxLm2DcS/).

Test task checklist
-------------------

✅ Telegram bot

- ✅ Production - webhook, development - long polling
- ✅ /start command
- ✅ ReplyKeyboardMarkup with 3 buttons - BTC, ETH, DOGE
- ✅ Getting current exchange rate (to USD) when push the corresponding button
- ✅ Error messages
- ✅ Cryptocurrency API integration (CryptoCompare as a provider)

✅ Django admin panel

- ✅ List of telegram bot users (fields - First launch of the
    bot, User ID, @Username, Last Name)
- ✅ Configured search bar and filters
- ✅ Editable bot messages and buttons
    (django-dynamic-preferences)
- ✅ No unnecessary links, buttons, sections, etc.
- ⬜️ Custom design (CSS)

⬜️ Tests

Settings
--------

To run your project for both development and production you should have
the following files that contain all the settings:

    $ cd .envs

    $ tree -a

      $ ├── .local
      $ │   ├── .django
      $ │   ├── .postgres
      $ │   └── .telegram
      $ └── .production
      $     ├── .django
      $     ├── .postgres
      $     └── .telegram

Installation and running locally (development)
----------------------------------------------

1.  Check whether PostgreSQL, Docker, Docker-compose, Git are installed
    and set up on your machine.
2.  Within your virtual env:

        $ pip install -r requirements/local.txt

3.  Run migrations within docker container:

        $ docker-compose -f local.yml run --rm django python manage.py migrate

4.  Create superuser to get an access to the admin panel:

        $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Installation and running globally (production)
----------------------------------------------

1.  Check whether PostgreSQL, Docker, Docker-compose, Git are installed
    and set up on your machine.
2.  Run migrations within docker container:

        $ docker-compose -f production.yml run --rm django python manage.py migrate

3.  Create superuser to get an access to the admin panel:

        $ docker-compose -f production.yml run --rm django python manage.py createsuperuser
