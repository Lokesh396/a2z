import sys
import os
from pathlib import Path
from collections import defaultdict
import heapq
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.postcount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.postcount, tweetId])
        self.postcount -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        tweets.extend(self.tweets[userId][-10:])
        for followee in self.follows[userId]:
            tweets.extend(self.tweets[followee][-10:])
        
        heapq.heapify(tweets)
        out = []
        for i in range(min(10, len(tweets))):
            out.append(heapq.heappop(tweets)[1])
        
        return out


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()