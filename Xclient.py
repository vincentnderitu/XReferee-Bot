import os
import tweepy
from src.utils import get_env, log

def create_client():
    client = tweepy.Client(
        bearer_token=get_env("TWITTER_BEARER_TOKEN"),
        consumer_key=get_env("TWITTER_API_KEY"),
        consumer_secret=get_env("TWITTER_API_SECRET"),
        access_token=get_env("TWITTER_ACCESS_TOKEN"),
        access_token_secret=get_env("TWITTER_ACCESS_SECRET")
    )
    return client

def poll_mentions_loop():
    client = create_client()
    log("Polling mentions... (Ctrl+C to stop)")

    for tweet in tweepy.Paginator(
        client.get_users_mentions, 
        id=client.get_me().data.id, 
        tweet_fields=["conversation_id","author_id"], 
        max_results=5
    ):
        for mention in tweet.data or []:
            handle_mention_event(client, mention)
