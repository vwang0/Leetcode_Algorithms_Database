"""
0849. Maximize Distance to Closest Person
Easy

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
 

Constraints:

2 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        last = -1
        N = len(seats)
        for i in range(N):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) // 2)
                last = i
        return max(res, N - last - 1)

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        length, turn = len(seats), []
        for i in range(length):
            if seats[i] == 1:
                turn.append(i)
        res = max(turn[0], length - turn[-1] - 1)
        for i in range(0, len(turn) - 1):
            if (turn[i+1] - turn[i]) // 2 > res:
                res = (turn[i+1] - turn[i]) // 2
        return res
