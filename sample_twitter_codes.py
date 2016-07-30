'''
CHECK TO SEE IF SCHOCASTIC VARIABLES TO BE SET CAN THROW OFF TWITTER...
'''
''''
In this code we'll have a bunch of examples you can use at your own discretion. 

Simply remove the three ' marks above and below the code you want in order to run it, while
leaving the text within a new set of three ' marks.

Once that's done, go to your Terminal, navigate to where this code and the twitter_follow_bot
code is (they have to be in the same folder), and just type in "python sample_twitter_codes.py" (without quotes)

WARNING: Following too many people, favoriting too many things, CAN and WILL get you banned.

Be smart. And have fun :). 

Justin and Nat
'''

'''
#1 This code will automatically un-follow everyone who hasn't followed you back.
You hit a limit with unfollowing... 200 a day.. double check to see if it even checks that...
Makes much more sense to have this FIRST since you'd add people and then unfollow them right away
lol
'''
from random import randint
import random, time, threading
print("===========================================")
print("Running the Script, c Jake GK 2016")
print("")

random_secondwait = random.randint(60 * 60 * 36, 60 * 60 * 48)
next_call_mutual = time.time() + random.randint(60 * 60 * 3, 60 * 60 * 5)
next_call_fav = time.time() + random_secondwait
next_call_auto = time.time() + random_secondwait

def randintWithHalfRandomness():
	if randint(0,1) == 1:
		return randint(3,9)
	else:
		return 0;
		
from twitter_follow_bot import auto_unfollow_nonfollowers
print("Doing cool automated stuff so it frees up cool stuff for you to do better stuff!")
print("===========================================")
print("Now Unfollowing people who dont follow you with ~N(25,12) total")
print("===========================================")
#auto_unfollow_nonfollowers()



'''
#2 In this code, change "jakegosskuehn" to the twitter handle whose followers you want to follow, 
and set the count to how many people should be followed. Default is 100.

Good follow up would be to get a list of your most popular followers, and follow from THEM.
'''
print("===========================================")
print("Now Following people who follow you! ~N(25,12) total")
print("===========================================")
from twitter_follow_bot import auto_follow_followers_for_user
#auto_follow_followers_for_user("jakegosskuehn", count=100)

'''
#3 Here you can automatically follow people who tweet about a certain phrase. Just replace the phrase
with something relevant to you! Also you can set the count to whatever makes you most comfortable.
'''

print("===========================================")
print("Now following those who like your hashtags! ~B(.5)*U(3,9)")
print("===========================================")
from twitter_follow_bot import auto_follow
from twitter_follow_bot import auto_fav
from twitter_follow_bot import auto_follow_others_thread

#auto_follow_others_thread()



'''
#4 This code will let you favoite things that are relevant to you. Just replace "phrase" with the phrase
you want to favorite for, and set the count to how many things you want to favorite.
This code is already part of: auto_follow_others_thread()... makes sense to fav and follow at the same time ;P
'''
#from twitter_follow_bot import auto_fav
#auto_fav("socialmediamarketing", count=1)
#auto_fav("nomadlife", count=1)
#auto_fav("homebrewweekend", count=1)
#auto_fav("socialmediamanager", count=1)
#auto_fav("startupculture", count=1)
#auto_fav("rollotomassi", count=1)
#auto_fav("betabucksalphafucks", count=1)
#auto_fav("pussypass", count=1)
#auto_fav("cherrybit", count=1)


'''
Finish: I put all threads in one method, and join everything together. That method will be called again to loop it all again.

'''
from twitter_follow_bot import newSleep
#def recallAllThreads():
global toggle
toggle = false
while(True):
	unfollowThread1 = threading.Thread(target=auto_unfollow_nonfollowers)
	followMutualFollowersThread2 = threading.Thread(target=auto_follow_followers_for_user, args=('jakegosskuehn', 100,))
	followAndLikeOthersThread3 = threading.Thread(target=auto_follow_others_thread)
	if(toggle)
	{
	unfollowThread1.start()
	}
	followMutualFollowersThread2.start()
	followAndLikeOthersThread3.start()
	#restartThreading4.start()
	if(toggle)
	{
	unfollowThread1.join()
	}
	followMutualFollowersThread2.join()
	followAndLikeOthersThread3.join()
	#restartThreading4.join()
	
	print("===========================================")
	print("PYTHON BOT IS LOOPING AGAIN. Sleeping for 24 hours.")
	print("===========================================")
	time.sleep(randint(60*60*24,60*60*25))
	toggle = true;
#restartThreading4 = threading.Thread(target=recallAllThreads)

