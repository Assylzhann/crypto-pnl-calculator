import tweepy
import datetime
import os

# === Settings ===
USERNAME = "SentientAGI"  # Replace with your desired Twitter handle
DATA_FILE = "last_tweet_id.txt"

# === API Keys (create at https://developer.x.com/) ===
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# === Authentication ===
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def get_last_tweet_id():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return f.read().strip()
    return None

def save_last_tweet_id(tweet_id):
    with open(DATA_FILE, "w") as f:
        f.write(str(tweet_id))

def get_new_tweets():
    last_id = get_last_tweet_id()
    tweets = api.user_timeline(screen_name=USERNAME, since_id=last_id, tweet_mode="extended", count=10)
    if tweets:
        save_last_tweet_id(tweets[0].id)
    return tweets

def main():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    tweets = get_new_tweets()

    if tweets:
        print(f"🕖 Daily Sentient update ({today})")
        for t in reversed(tweets):
            print(f"- {t.created_at}: {t.full_text[:100]}...")
    else:
        print(f"No new tweets for {today}")

if __name__ == "__main__":
    main()
