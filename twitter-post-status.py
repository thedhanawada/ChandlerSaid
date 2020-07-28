#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-post-status
#  - posts a status message to your timeline
#-----------------------------------------------------------------------
import json
import urllib3
from random import randrange
from twitter import *

#-----------------------------------------------------------------------
# what should our new status be?
#-----------------------------------------------------------------------
#new_status = "Testing 44"

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config
import time
#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

#-----------------------------------------------------------------------
# post a new status
# twitter API docs: https://dev.twitter.com/rest/reference/post/statuses/update
#-----------------------------------------------------------------------
http = urllib3.PoolManager()
heroes = http.request('GET', 'https://v2-api.sheety.co/fa7d3aeaa9bd9ff88dfc5d7b867b3fc1/myChaandyApi/chandler')
heroes_dict = json.loads(heroes.data.decode('UTF-8'))

new_status = (heroes_dict['chandler'][randrange(16300)]["chandlerSays"])
results = twitter.statuses.update(status = new_status+"#FRIENDS"+ " #ChandlerSaid" )
print("updated status: %s" % new_status)
#number+=1
