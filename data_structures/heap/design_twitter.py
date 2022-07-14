# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 10 条推文。

# 实现 Twitter 类：

# Twitter() 初始化简易版推特对象
# void postTweet(int userId, int tweetId) 根据给定的 tweetId 和 userId 创建一条新推文。每次调用此函数都会使用一个不同的 tweetId 。
# List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近  10 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。
# void follow(int followerId, int followeeId) ID 为 followerId 的用户开始关注 ID 为 followeeId 的用户。
# void unfollow(int followerId, int followeeId) ID 为 followerId 的用户不再关注 ID 为 followeeId 的用户。


import heapq
from collections import defaultdict
from itertools import chain, islice
from typing import List


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # userId: [(dt, tweetId)]
        self.follows = defaultdict(set)  # userId: set()
        # 使用正整数给 tweet 排序
        # 但是入堆中要加上负号
        self.tweet_seq = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 维护升序 tweet 列表
        self.tweets[userId].append((-self.tweet_seq, tweetId))
        self.tweet_seq += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        使用最小堆模拟最大堆进行 k 路归并。
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
