import tweepy
import os

class TwitterService:
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
        )

    def post_thread(self, tweets):
        previous_tweet_id = None
        for tweet in tweets:
            response = self.client.create_tweet(
                text=tweet,
                in_reply_to_tweet_id=previous_tweet_id
            )
            previous_tweet_id = response.data["id"]
