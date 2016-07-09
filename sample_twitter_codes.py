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
import random
print("===========================================")
print("Running the Script, c Jake GK 2016")
print("")

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
auto_follow_followers_for_user("jakegosskuehn", count=100)




'''
#3 Here you can automatically follow people who tweet about a certain phrase. Just replace the phrase
with something relevant to you! Also you can set the count to whatever makes you most comfortable.
'''



print("===========================================")
print("Now following those who like your hashtags! ~B(.5)*U(3,9)")
print("===========================================")
from twitter_follow_bot import auto_follow
from twitter_follow_bot import auto_fav
auto_fav("socialmediamarketing", count=randint(0,1))
auto_follow("socialmediamarketing", count=randintWithHalfRandomness())
auto_fav("softwaredevelopment", count=randint(0,1))
auto_follow("softwaredevelopment", count=randintWithHalfRandomness())
auto_fav("startup", count=randint(0,1))
auto_follow("startup", count=randintWithHalfRandomness())
auto_fav("smm", count=randint(0,1))
auto_follow("smm", count=randintWithHalfRandomness())
auto_fav("homebrew", count=randint(0,1))
auto_follow("homebrew", count=randintWithHalfRandomness())
auto_fav("nomad", count=randint(0,1))
auto_follow("nomad", count=randintWithHalfRandomness())


'''
#4 This code will let you favoite things that are relevant to you. Just replace "phrase" with the phrase
you want to favorite for, and set the count to how many things you want to favorite.
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


print("===========================================")
print("PYTHON BOT IS DONE. I WILL SLEEP UNTIL CALLED.")
print("===========================================")
