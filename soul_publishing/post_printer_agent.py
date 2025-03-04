import praw

from prawcore.exceptions import NotFound, Forbidden, Redirect 

class PostPrinterAgent:
    """
    Agent for printing the details of Reddit posts.
    """
    def print_posts(self, posts):
        """
        Prints the title, author, and upvote count of each post.

        Parameters:
        posts (list): A list of Reddit posts to print.
        """
        try: 
            for post in posts:
                print(f"Title: {post.title}")
                print(f"Author: {post.author}")
                print(f"Upvotes: {post.score}")
                print("-" * 40)
        except NotFound:
            print(f"Subreddit posts are found or are banned.")
        except Redirect:
                print(f"Requested subreddit has been temporarily moved.")
        except Forbidden:
            print(f"Access to subreddit posts is forbidden.")
        except praw.exceptions.PRAWException as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e.response.text}")
