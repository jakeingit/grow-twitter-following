'''
#1 This code will automatically un-follow everyone who hasn't followed you back.
You hit a limit with unfollowing... 200 a day.. double check to see if it even checks that...
Makes much more sense to have this FIRST since you'd add people and then unfollow them right away
Should be ran once every 24 hours... so it can get 200 unfollows...
May use the limit from the previous day to cause a rate limit...
'''

from twitter_follow_bot import auto_unfollow_nonfollowers
print("Doing cool automated stuff so it frees up cool stuff for you to do better stuff!")
print("===========================================")
print("Now Unfollowing people who dont follow you with ~N(25,12) total")
print("===========================================")
auto_unfollow_nonfollowers()