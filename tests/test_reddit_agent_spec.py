import pytest

from soul_publishing.reddit_agent import RedditAgent
from prawcore.exceptions import NotFound, Forbidden
from unittest.mock import patch, MagicMock
from prawcore.exceptions import NotFound, Forbidden

@pytest.fixture
def reddit_agent():
    """
    Fixture to create a RedditAgent instance for testing.
    """
    return RedditAgent()

def test_fetch_latest_posts_success(reddit_agent):
    """
    Test fetching the latest posts from a subreddit successfully.
    """
    # Mock the Reddit API response for a successful fetch
    with patch.object(reddit_agent.reddit, 'subreddit') as mock_subreddit:
        mock_subreddit.return_value.new.return_value = [MagicMock()]
        mock_post = MagicMock()
        mock_post.title = "Test Title"
        mock_post.author = "Test Author"
        mock_post.score = 100
        mock_subreddit.return_value.new.return_value = [mock_post]

        posts = list(reddit_agent.fetch_latest_posts('test_subreddit', limit=1))
        
        assert len(posts) == 1
        assert posts[0].title == "Test Title"
        assert posts[0].author == "Test Author"
        assert posts[0].score == 100

def test_fetch_latest_posts_not_found(reddit_agent):
    """
    Test fetching posts from a non-existent subreddit.
    """
    # Mock the Reddit API response for a non-existent subreddit
    with patch.object(reddit_agent.reddit, 'subreddit', side_effect=NotFound):
        posts = reddit_agent.fetch_latest_posts('non_existent_subreddit', limit=1)
        
        assert len(posts) == 0

def test_fetch_latest_posts_forbidden(reddit_agent):
    """
    Test fetching posts from a forbidden subreddit.
    """
    # Mock the Reddit API response for a forbidden subreddit
    with patch.object(reddit_agent.reddit, 'subreddit', side_effect=Forbidden):
        posts = reddit_agent.fetch_latest_posts('forbidden_subreddit', limit=1)
        
        assert len(posts) == 0
