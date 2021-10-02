def canPartition(nums):
	s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: return False
        nums.sort(reverse=True)
        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            break
            return memo[x]
        return dfs(0, s >> 1)

"""

Partition Equal Subset Sum


----------------------------------------
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

----------------------------------------
Time Complexity:
Worst case = O(nlogn)
Space Complexity: O(n)

"""
