import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay
from lamson import view
from webapp.brieftraeger.models import Email, List
from django.contrib.sites.models import Site


@route("(address)@(host)", address=".+", host=".+")
def START(message, address=None, host=None):
    incoming_list = "%s@%s" % (address, host)
    logging.debug("incoming list: %s" % incoming_list)

    try:
        site = Site.objects.get(name=host)
        list = List.objects.get(name=address, site=site)
    except List.DoesNotExist:
        return FORWARD

    message_id = message.get('Message-Id')
    logging.debug("Message-Id: %s" % message_id)
    email = Email(message=message,
                  message_id=message_id,
                  list=list)
    email.save()

    return NEW_USER


@route_like(START)
def NEW_USER(message, address=None, host=None):
    return NEW_USER


@route_like(START)
def END(message, address=None, host=None):
    return NEW_USER(message, address, host)


@route_like(START)
@stateless
def FORWARD(message, address=None, host=None):
    relay.deliver(message)

