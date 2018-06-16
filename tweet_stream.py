#!/usr/bin/env python
#-*-coding:utf-8-*-

import tweepy
import socket
import sys
import locale
import string
from unicode_tr import unicode_tr
from elasticsearch import Elasticsearch

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class CustomStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		try:
			print status.text
		except Exception, e:
			print >> sys.stderr, 'Encountered Exception:', e
			pass

	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True # Don't kill the stream

streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

print >> sys.stderr, 'Filtering the public timeline for "%s"' % (' '.join('love'),)

streaming_api.filter(follow=None, track=['iyi'])
