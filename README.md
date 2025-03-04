# Soul Publishing Reddit API Task

This project uses Poetry for dependency management and leverages the (Cheery JVM's) Agent pattern for fetching and printing the latest posts from a given subreddit.

## Requirements

- Python 3.8 to <4.0
- Poetry

## Setup

1. Clone the repository or download the project files.

2. Rename `./.env.example` file to `./.env`

3. Set your secrets values per key in the `./.env` file

4. Install Poetry if not already installed:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -

5. Set up dependencies:
   ```bash
   poetry install

6.  Run the tests:
   ```bash
   poetry run pytest

7. Run the Reddit agent script

   ```bash
   poetry run python soul_publishing/reddit_agent.py

## Next steps

1. Create a CI (Github Actions) setup for both development and agent operation
2. Improve the agent design via applying missions and goals
3. Improve the configuration setup, add direnv
4. Improve the agent tests with service tests (actual API calls, not just mocking)
5. Improve the request/response type safety via pydantic
6. Improve the static analysis: add copy/paste detector, ruff, git hooks
7. Research Microsoft's Magma model for AI agents operating over user interfaces 
