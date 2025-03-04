import pytest

from soul_publishing.post_printer_agent import PostPrinterAgent
from unittest.mock import MagicMock

@pytest.fixture
def reddit_agent():
    """
    Fixture to create a RedditAgent instance for testing.
    """
    return PostPrinterAgent()


def test_print_posts(capfd):
    """
    Test printing the details of Reddit posts.
    """
    printer_agent = PostPrinterAgent()
    mock_post = MagicMock()
    mock_post.title = "Test Title"
    mock_post.author = "Test Author"
    mock_post.score = 100

    posts = [mock_post]
    printer_agent.print_posts(posts)
    
    # Capture the printed output
    captured = capfd.readouterr()
    output = captured.out
    
    # Assert the expected output
    expected_output = (
        "Title: Test Title\n"
        "Author: Test Author\n"
        "Upvotes: 100\n"
        "----------------------------------------\n"
    )
    assert output == expected_output
