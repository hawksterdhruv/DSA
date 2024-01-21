import pytest

from ..twitter import Twitter

operations = [
    "postTweet",
    "postTweet",
    "postTweet",
    "postTweet",
    "postTweet",
    "postTweet",
    "postTweet",
    "postTweet",
    "postTweet",
    "postTweet",
    "postTweet",
    "getNewsFeed",
]
inputs = [
    [1, 5],
    [1, 3],
    [1, 101],
    [1, 13],
    [1, 10],
    [1, 2],
    [1, 94],
    [1, 505],
    [1, 333],
    [1, 22],
    [1, 11],
    [1],
]

outputs = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    [11, 22, 333, 505, 94, 2, 10, 13, 101, 3],
]


@pytest.fixture(scope="module")
def get_twitter():
    twitter = Twitter()
    return twitter


@pytest.mark.parametrize("operation, inp, output", zip(operations, inputs, outputs))
def test_twitter(operation, inp, output, get_twitter):
    try:
        method = getattr(get_twitter, operation)
        print(method.__name__, inp)
        res = method(*inp)
        print(res)
        print(get_twitter.tweets)
        assert res == output
    except AttributeError:
        print(f"Unsupported operation: {operation}")
