"""
https://leetcode.com/problems/minimum-cost-for-tickets/

In a country popular for train travel, you have planned some train travelling one year in advance.
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can
travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.



Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.


Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        Want min cost at the end of the year (i.e. day 365).
        If a day is not in the list of days traveled, it's min cost is the min cost of the previous day.
        For a day that is in the list of days traveled:
        1. If buy 1-day ticket, the min cost is min cost of previous day + cost of 1 day ticket
        2. If buy 7-day ticket, the min cost is min cost of 7 days ago + cost of 7 day ticket
        3. If buy 30-day ticket, the min cost is min cost of 30 days ago + cost of 30 day ticket
        Since min cost is always rising, don't have to consider minimum costs from earlier (i.e. 6 days ago, 5 days ago)
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        spend = [0] * 366

        for day in range(366):
            if day not in days:
                spend[day] = spend[day - 1]
            else:
                spend_1_day = spend[max(day - 1, 0)] + costs[0]
                spend_7_day = spend[max(day - 7, 0)] + costs[1]
                spend_30_day = spend[max(day - 30, 0)] + costs[2]
                spend[day] = min(min(spend_1_day, spend_7_day), spend_30_day)

        return spend[365]
