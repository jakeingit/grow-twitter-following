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