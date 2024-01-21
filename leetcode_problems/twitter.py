from collections import defaultdict

# class Tweet:
#     tweetId:int = None
#     userId:int = None
# class User:
#     userId:int = None
#     tweets:list[Tweet] = []
#     followers:list[User] = []
#     def __init__(self, userId:int):
#         self.userId = userId
#     def __eq__(self, other:User) -> bool:
#         return self.userId = other.userId


class Twitter:
    def __init__(self):
        self.users = {}
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.users[userId].append((userId, tweetId))
        self.tweets[tweetId] = userId

    def getNewsFeed(self, userId: int) -> list[int]:
        tempUsers = [userId] + list(self.followers[userId])
        op = []
        for t, u in list(self.tweets.items())[::-1]:  # get in reverse OR put in reverse
            if u in tempUsers:
                op.append(t)
            if len(op) >= 10:
                break
        return op

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
