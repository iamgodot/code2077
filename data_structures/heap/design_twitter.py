# Design Twitter
# https://leetcode.com/problems/design-twitter/description/


import heapq
from collections import defaultdict
from itertools import chain, islice


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # userId: [(dt, tweetId)]
        self.follows = defaultdict(set)  # userId: set()
        self.tweet_seq = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.tweet_seq, tweetId))
        self.tweet_seq += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Time: O(n*k*logk)
        Space: O(logk)
        """
        tweets = heapq.merge(
            *(self.tweets[uid] for uid in chain(self.follows[userId], [userId]))
        )
        return [tweet[1] for tweet in islice(tweets, 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]
