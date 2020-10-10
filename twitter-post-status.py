#!/usr/bin/env python

import json
import urllib3
from random import randrange
from twitter import *

import sys
sys.path.append(".")
import config
import time
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

http = urllib3.PoolManager()
heroes = http.request('GET', 'https://api.sheety.co/98b7e023de93d9f9c9e690887491f1d4/chandler/chandler')
heroes_dict = json.loads(heroes.data.decode('UTF-8'))

new_status = (heroes_dict['chandler'][randrange(16300)]["chandlerSays"])
results = twitter.statuses.update(status = new_status+"#FRIENDS"+ " #ChandlerSaid" )
print("updated status: %s" % new_status)
