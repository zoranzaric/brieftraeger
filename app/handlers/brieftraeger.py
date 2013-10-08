import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay
from lamson import view
from webapp.brieftraeger.models import Email, List


@route("(address)@(host)", address=".+")
def START(message, address=None, host=None):
    incoming_list = "%s@%s" % (address, host)
    logging.debug("incoming list: %s" % incoming_list)
    list = List.objects.get(name=address, site=host)

    message_id = message.get('Message-Id')
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

