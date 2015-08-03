#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw
import sys
import markov
from time import time

user_agent = "Mockit:v0.1 \"https://github.com/oknono/mockit\"(by /u/oknono12)"
r = praw.Reddit(user_agent=user_agent)

def title_string(sub, limit=100): 
    '''Return string containing the titles of a specified number of most popular 
    post title from a specified subreddit'''
    posts = ""
    subreddit = r.get_subreddit(sub)
    for post in subreddit.get_top_from_all(limit=limit):
        title = post.title.encode('utf-8').strip()
        posts += title
    print "length of posts is {}".format(len(posts))
    return posts

def generate_post_title(sub='relationships', order=6, length =120):
    ''' generate a post title given a subreddit, sample length and title length'''
    text = title_string(sub)
    post = markov.generateText(text, order, length)
    return post

def body_string(sub, limit=100):
    '''Return string containing the body texts of a specified number of most popular 
    posts from a specified subreddit'''
    posts = ""
    subreddit = r.get_subreddit(sub)
    for post in subreddit.get_top_from_all(limit=limit):
        body = post.selftext.encode('utf-8').strip()
        posts += body
    #print "length of posts is {}".format(len(posts))
    #print posts
    return posts

def generate_post_body(sub='relationships', order=15, length=500):
    ''' generate a post body given a subreddit, sample length and title length'''
    text = body_string(sub)
    post = markov.generateText(text, order, length)
    return post


if __name__ == "__main__":
    t0 = time()
    print
    try:
       generate_post_title(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
       print
       generate_post_body(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
       print "Title:"
       generate_post_title()
       print "Body:"
       generate_post_body()
    t1 = time()
    print
    print "Calling Reddit API to create a random post took {} seconds".format(t1-t0)
