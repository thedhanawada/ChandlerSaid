#--------------------------------------------------------------------------------
# These tokens are needed for user authentication.
# Credentials can be generated via Twitter's Application Management:
#	https://developer.twitter.com/en/apps
#--------------------------------------------------------------------------------
import os
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_key = os.environ.get("access_key")
access_secret = os.environ.get("access_secret")
