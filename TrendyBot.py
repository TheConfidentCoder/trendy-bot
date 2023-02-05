import praw
import os
import time
import config

# Initialize a Reddit instance
reddit = praw.Reddit(client_id=os.environ.get("CLIENT_ID"),
                     client_secret=os.environ.get("CLIENT_SECRET"),
                     username=os.environ.get("USERNAME"),
                     password=os.environ.get("PASSWORD"),
                     user_agent=os.environ.get("USER_AGENT"))

# Define the subreddit you want to post to
subreddit = reddit.subreddit("worldnews")

# Define the interval at which you want to check for trending topics
interval = 60 * 60 * 24 # 24 hours

while True:
    # Get the top 10 hot posts in the subreddit
    hot_posts = subreddit.hot(limit=10)
    
    # Create a string to store the trending topics
    trending_topics = "Trending Topics Today:\n\n"

    # Add the titles of the hot posts to the trending_topics string
    for post in hot_posts:
        trending_topics += post.title + "\n\n"

    # Submit a post with the trending topics
    subreddit.submit("Daily Trending Topics", selftext=trending_topics)

    # Wait for the defined interval before checking again
    time.sleep(interval)
