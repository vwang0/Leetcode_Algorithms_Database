"""
346. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        from collections import deque

        self.size = size
        self.windowLen = 0
        self.windowSum = 0
        self.windowQue = deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.windowLen += 1
        self.windowQue.append( val )
        self.windowSum += val

        if self.windowLen > self.size:
            self.windowLen -= 1
            self.windowSum -= self.windowQue.popleft()

        return float(self.windowSum) / float(self.windowLen)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)