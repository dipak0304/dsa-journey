class Solution:
    def judgePoint24(self, cards):
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            n = len(nums)
            # try all pairs
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    # pick nums[i] and nums[j], build new list
                    next_nums = []
                    for k in range(n):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    # try all operations
                    a, b = nums[i], nums[j]
                    for val in [a + b, a - b, a * b]:
                        if dfs(next_nums + [val]):
                            return True
                    # division (avoid div by zero)
                    if abs(b) > 1e-6:
                        if dfs(next_nums + [a / b]):
                            return True
            return False

        return dfs([float(x) for x in cards])
