import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from users import FreeUser, PremiumUser, User


@pytest.fixture(autouse=True)
def reset_posts():
    User.all_posts = []


def test_free_user_can_create_only_two_posts():
    free_user = FreeUser("John", "John@email.com")

    assert free_user.create_post("First post") is True
    assert free_user.create_post("Second post") is True
    assert free_user.create_post("Third post") is False
    assert len(free_user.posts) == 2


def test_premium_user_can_create_more_than_two_posts():
    premium_user = PremiumUser("Alice", "Alice@email.com")

    assert premium_user.create_post("First post") is True
    assert premium_user.create_post("Second post") is True
    assert premium_user.create_post("Third post") is True
    assert len(premium_user.posts) == 3