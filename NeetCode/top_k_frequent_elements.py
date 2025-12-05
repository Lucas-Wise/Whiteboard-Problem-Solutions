from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [num for num, _ in freq.most_common(k)]

if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1,2,2,3,3,3], 2))  
    print(solution.topKFrequent([7,7], 1))          