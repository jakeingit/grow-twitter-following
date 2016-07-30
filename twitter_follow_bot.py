# -*- coding: utf-8 -*-

"""
Copyright 2014 Randal S. Olson, Jake Goss-Kuehn

This file is part of the Twitter Follow Bot library.

The Twitter Follow Bot library is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option) any
later version.

The Twitter Follow Bot library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with the Twitter
Follow Bot library. If not, see http://www.gnu.org/licenses/.

Code only slightly modified by Programming for Marketers to allow for separate variable 
storage.
"""

from twitter import Twitter, OAuth, TwitterHTTPError
import os
import time, threading, datetime
import random
random_secondwait = random.randint(60 * 60 * 11, 60 * 60 * 13)
next_call_mutual = time.time() + random.randint(60 * 60 * 3, 60 * 60 * 5)
next_call_fav = time.time() + random_secondwait
next_call_auto = time.time() + random_secondwait
from random import randint
from twitter_info import *

# put the full path and file name of the file you want to store your "already followed"
# list in
#sleep = random.random() * 7 # 0 to 7 seconds
#Good to mimic the 3 twitter followers that you get on the side
#Every 3rd have a PAUSE... hmmm

def newSleep():
	sleeptime = random.randint(15,  21)
	print("Sleeping for "+str(sleeptime)+" minutes before the thread continues.");
	time.sleep(60* sleeptime)
	print("woke up");
	
def setGlobals():
	global thirdcount
	thirdcount = 0
	global sessionfollows
	sessionfollows = 0
	global sessionunfollows
	sessionunfollows = 0


ALREADY_FOLLOWED_FILE = "already-followed.csv"

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY, CONSUMER_SECRET))


def search_tweets(q, count=100, result_type="recent"):
	'''
		Returns a list of tweets matching a certain phrase (hashtag, word, etc.)
	'''
	return t.search.tweets(q=q, result_type=result_type, count=count)

#After this auto_fav follows just ONE favorite, it breaks out of the method's for loop and moves on with its life. Maybe it finds a nice cottage out in the mountains, maybe it just finds a nice suburb to raise a middle class family. Whatever it does, it stops what it is doing to continue on. It does this once if anything, and stops.
def auto_fav(q, count=100, result_type="recent"):
	"""
		Favorites tweets that match a certain phrase (hashtag, word, etc.)
	"""
	newSleep();
	result = search_tweets(q, count, result_type)



	for tweet in result["statuses"]:
		try:
			# don't favorite your own tweets
			if tweet["user"]["screen_name"] == TWITTER_HANDLE:
				continue
			time.sleep(randint(5,13))
			result = t.favorites.create(_id=tweet["id"])
			print("favorited on %s : %s " % (q, result["text"].encode("utf-8")))
			break
		# when you have already favorited a tweet, this error is thrown
		except TwitterHTTPError as e:
			print("error: %s" % (str(e)))
	#fav = threading.Thread(target=auto_fav, args=(next_call_fav,)).start()
	

def randintWithHalfRandomness():
	if randint(0,1) == 1:
		return randint(3,9)
	else:
		return 0;
	
def auto_follow_others_thread():
	newSleep();
	auto_fav("socialmediamarketing", count=randint(0,1))
	auto_follow("socialmediamarketing", count=randintWithHalfRandomness())
	auto_fav("softwaredevelopment", count=randint(0,1))
	auto_follow("softwaredevelopment", count=randintWithHalfRandomness())
	auto_fav("startup", count=randint(0,1))
	auto_follow("startup", count=randintWithHalfRandomness())
	Thread.sleep(randint(60*15,60*19))
	auto_fav("smm", count=randint(0,1))
	auto_follow("smm", count=randintWithHalfRandomness())
	auto_fav("homebrew", count=randint(0,1))
	auto_follow("homebrew", count=randintWithHalfRandomness())
	auto_fav("nomad", count=randint(0,1))
	auto_follow("nomad", count=randintWithHalfRandomness())
	Thread.sleep(randint(60*15,60*19))
	#t = threading.Thread(target=auto_follow_others_thread, args=(next_call_mutual,)).start()
	#t.join()		
def auto_rt(q, count=100, result_type="recent"):
	"""
		Retweets tweets that match a certain phrase (hashtag, word, etc.)
	"""

	result = search_tweets(q, count, result_type)

	for tweet in result["statuses"]:
		sleep(random.random() * 10 + 3)
		try:
			# don't retweet your own tweets
			if tweet["user"]["screen_name"] == TWITTER_HANDLE:
				continue

			result = t.statuses.retweet(id=tweet["id"])
			print("retweeted: %s" % (result["text"].encode("utf-8")))

		# when you have already retweeted a tweet, this error is thrown
		except TwitterHTTPError as e:
			print("error: %s" % (str(e)))


def get_do_not_follow_list():
	"""
		Returns list of users the bot has already followed.
	"""

	# make sure the "already followed" file exists
	if not os.path.isfile(ALREADY_FOLLOWED_FILE):
		with open(ALREADY_FOLLOWED_FILE, "w") as out_file:
			out_file.write("")

		# read in the list of user IDs that the bot has already followed in the
		# past
	do_not_follow = set()
	dnf_list = []
	with open(ALREADY_FOLLOWED_FILE) as in_file:
		for line in in_file:
			dnf_list.append(int(line))

	do_not_follow.update(set(dnf_list))
	del dnf_list

	return do_not_follow


def auto_follow(q, count=100, result_type="recent"):
	"""
		Follows anyone who tweets about a specific phrase (hashtag, word, etc.)
		Sleeps in intervals of THREES to play against twitter
	"""

	global sessionfollows
	sessionfollows = 0
	global thirdcount
	thirdcount = 0
	global followlimit
	#followlimit = random.random() * 75 + 150
	followlimit = random.random() * 15 + 10
	
	result = search_tweets(q, count, result_type)
	following = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])
	do_not_follow = get_do_not_follow_list()

	for tweet in result["statuses"]:
		sessionfollows = sessionfollows + 1
		if sessionfollows > followlimit:
			continue
		elif thirdcount == 3:
			thirdcount = 0
			time.sleep(random.random() * 12 + 3)
		
		try:
			
			thirdcount = thirdcount + 1
			if (tweet["user"]["screen_name"] != TWITTER_HANDLE and 
			tweet["user"]["id"] not in following and 
			tweet["user"]["id"] not in do_not_follow):
				time.sleep(3)
				t.friendships.create(user_id=tweet["user"]["id"], follow=False)
				following.update(set([tweet["user"]["id"]]))

				print("followed %s on %s (%d out of %d for this session)" % (tweet["user"]["screen_name"], q, sessionfollows, followlimit))

		except TwitterHTTPError as e:
			print("error: %s" % (str(e)))

			# quit on error unless it's because someone blocked me
			if "blocked" not in str(e).lower():
				quit()


def auto_follow_followers_for_user(user_screen_name, count=100):
	"""
		Follows the followers of a user
	"""
	newSleep();
	global sum
	sum = 0
	global sessionfollows
	sessionfollows = 0
	following = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])
	followers_for_user = set(t.followers.ids(screen_name=user_screen_name)["ids"][:count]);
	do_not_follow = get_do_not_follow_list()

	for user_id in followers_for_user:
		sum = sum + 1
		sessionfollows = sessionfollows + 1
		if sessionfollows > random.random() * 25 + 75:
			break

		try:
			if (user_id not in following and 
				user_id not in do_not_follow):
				time.sleep(random.random() * 16 + 6)
				t.friendships.create(user_id=user_id, follow=False)
				print("mutually followed %s (%d out of %d for this session)" % (user_id, sum, len(followers_for_user)))

		except TwitterHTTPError as e:
			print("error: %s" % (str(e)))
	#follow = threading.Thread(target=auto_follow_followers_for_user, args=(next_call_mutual,)).start()
	#follow.join()

def auto_follow_followers():
	"""
		Follows back everyone who's followed you
	"""
	newSleep();

	following = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])
	followers = set(t.followers.ids(screen_name=TWITTER_HANDLE)["ids"])

	not_following_back = followers - following

	for user_id in not_following_back:
		if sessionfollows > random.random() * 75 + 150:
			continue
		try:
			t.friendships.create(user_id=user_id, follow=False)
			sessionfollows = sessionfollows + 1
		except Exception as e:
			print("error: %s" % (str(e)))
	#o = threading.Thread(target=auto_follow_others_thread, args=(next_call_mutual,)).start()
	#o.join()


def auto_unfollow_nonfollowers():
	"""
		Unfollows everyone who hasn't followed you back
		Needs to be able to not always reach the 200... a day...
		Also needs to start at RANDOM times in the morning
		to mimic REAL useage as not to be banned...
		Doesnt have a limit... probally breaks at any time.
	"""
	newSleep();
	global sessionunfollows
	sessionunfollows = 0
	unfollowlimit = random.random() * 25 + 125
	following = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])
	followers = set(t.followers.ids(screen_name=TWITTER_HANDLE)["ids"])

	# put user IDs here that you want to keep following even if they don't
	# follow you back
	users_keep_following = set([])

	not_following_back = following - followers

    # make sure the "already followed" file exists
	if not os.path.isfile(ALREADY_FOLLOWED_FILE):
		with open(ALREADY_FOLLOWED_FILE, "w") as out_file:
			out_file.write("")

	# update the "already followed" file with users who didn't follow back
	already_followed = set(not_following_back)
	af_list = []
	with open(ALREADY_FOLLOWED_FILE) as in_file:
		for line in in_file:
			af_list.append(int(line))

	already_followed.update(set(af_list))
	del af_list

	with open(ALREADY_FOLLOWED_FILE, "w") as out_file:
		for val in already_followed:
			out_file.write(str(val) + "\n")

	for user_id in not_following_back:
		if sessionunfollows > unfollowlimit:
			continue
		if user_id not in users_keep_following:
			time.sleep(random.random() * 4 + 10)
			t.friendships.destroy(user_id=user_id)
			sessionunfollows = sessionunfollows + 1
			print("unfollowed %d (%d out of %d for the session) " % (user_id, sessionunfollows, unfollowlimit))

def auto_mute_following():
	"""
		Mutes everyone that you are following
	"""
	following = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])
	muted = set(t.mutes.users.ids(screen_name=TWITTER_HANDLE)["ids"])

	not_muted = following - muted

	# put user IDs of people you do not want to mute here
	users_keep_unmuted = set([])
            
	# mute all        
	for user_id in not_muted:
		if user_id not in users_keep_unmuted:
			t.mutes.users.create(user_id=user_id)
			print("muted %d" % (user_id))


def auto_unmute():
	"""
		Unmutes everyone that you have muted
	"""
	muted = set(t.mutes.users.ids(screen_name=TWITTER_HANDLE)["ids"])

	# put user IDs of people you want to remain muted here
	users_keep_muted = set([])

	# mute all        
	for user_id in muted:
		if user_id not in users_keep_muted:
			t.mutes.users.destroy(user_id=user_id)
			print("unmuted %d" % (user_id))
