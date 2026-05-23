class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        def can_eat(k):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            return hours <= h

        while left < right:
            mid = (left + right) // 2
            if can_eat(mid):
                right = mid
            else:
                left = mid + 1

        return left
