import praw
import os
from dotenv import load_dotenv

from soul_publishing.post_printer_agent import PostPrinterAgent

class RedditAgent:
    """
    Agent for interacting with the Reddit API to fetch the latest posts from a subreddit.
    """
    def __init__(self):
        """
        Initialize the RedditAgent with credentials from the .env file.
        """
        load_dotenv()
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD")
        )

    def fetch_latest_posts(self, subreddit_name, limit=5):
        """
        Fetch the latest posts from a given subreddit.

        Parameters:
        subreddit_name (str): The name of the subreddit to fetch posts from.
        limit (int): The number of posts to fetch. Default is 5.

        Returns:
        list: A list of posts from the subreddit.
        """
        if not subreddit_name:
            print("Subreddit name cannot be empty.")
            return []

        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            posts = subreddit.new(limit=limit)
            return posts
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return[]


if __name__ == "__main__":
    subreddit_name = input("Enter a subreddit name to pull latest 5 posts:")
    reddit_agent = RedditAgent()
    posts = reddit_agent.fetch_latest_posts(subreddit_name)
    
    printer_agent = PostPrinterAgent()
    printer_agent.print_posts(posts)
