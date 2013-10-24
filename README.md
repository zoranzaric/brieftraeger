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

    # start
    $ source .virtualenv/bin/activate
    $ lamson start

    # in a different shell
    $ python webapp/manage.py runserver 0.0.0.0:8888


    # send mail
    $ lamson send -sender "sender@example.com" -to "recipient@example.com" -subject “My test.” -body “Hi there.” -port 8823 -attach "False"

    # or with mutt
    mutt -F muttrc


    # stop
    $ lamson stop

