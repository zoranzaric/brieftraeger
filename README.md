brieftraeger
============

brieftraeger is a tool to manage mailinglists.  "Briefträger" is German for
postman.


Installation
-----------

    # create virtualenv
    $ virtualenv --no-site-packages .virtualenv
    # activate virtualenv
    $ source .virtualenv/bin/activate
    # install dependencies
    $ pip install -r requirements.txt
    # create webapp database
    $ python webapp/manage.py syncdb


Usage
-----

    $ source .virtualenv/bin/activate
    $ lamson start
    $ python webapp/manage.py runserver 0.0.0.0:8888

    $ lamson send -sender "sender@example.com" -to "recipient@example.com" -subject “My test.” -body “Hi there.” -port 8823 -attach "False"

    $ lamson stop

