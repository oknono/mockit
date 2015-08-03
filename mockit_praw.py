#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw
import sys
import markov
from time import time

user_agent = "Mockit:v0.1 \"https://github.com/oknono/mockit\"(by /u/oknono12)"
r = praw.Reddit(user_agent=user_agent)

def title_string(sub, limit=100): 
    '''Return string containing the text of a specified number of most popular post title from a specified subreddit'''
    posts = ""
    subreddit = r.get_subreddit(sub)
    for post in subreddit.get_controversial_from_all(limit=limit):
        title = post.title.encode('utf-8').strip()
        posts += title
    print "length of posts is {}".format(len(posts))
    return posts

def generate_post_title(sub='relationships', order=6, length =120):
    ''' generate a post title given a subreddit, sample length and title length'''
    text = title_string(sub)
    post = markov.generateText(text, order, length)
    return post


if __name__ == "__main__":
    t0 = time()
    print
    try:
        generate_post_title(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
        generate_post()
    t1 = time()
    print
    print "Calling Reddit API to create a random post took {} seconds".format(t1-t0)
