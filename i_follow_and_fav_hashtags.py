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

auto_follow_others_thread()