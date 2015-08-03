import praw
import sys
from time import time

user_agent = "Mockit:v0.1 \"https://github.com/oknono/mockit\"(by /u/oknono12)"
r = praw.Reddit(user_agent=user_agent)

def list_top_post(name, limit=100):
    
    '''Return a specified number of most popular post from a specified subreddit'''
    subreddit = r.get_subreddit(name)
    for index, post in enumerate(subreddit.get_top_from_all(limit=limit), 1):
        print index, post.title

#list_top_post()
#print ""
#list_top_post('awww', 500)

if __name__ == "__main__":
    args = sys.argv[:]
    script = args.pop(0)
    name = args[0]
    t0 = time()
    list_top_post(name)
    t1 = time()
    print "Calling Reddit API for 100 posts took {} seconds".format(t1-t0)
