class RangeSumQuery(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        """"Initialize BIT with list in O(n)"""
        self.list = nums
        self.array = [0] + nums
        for idx in range(1, len(self.array)):
            idx2 = idx + (idx & -idx)
            if idx2 < len(self.array):
                self.array[idx2] += self.array[idx]

    def update(self, idx, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        add = val - self.list[idx]
        self.list[idx] = val
        idx += 1
        while idx < len(self.array):
            self.array[idx] += add
            idx += idx & -idx
        

    def sumRange(self, from_idx, to_idx):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_query(to_idx) - self.prefix_query(from_idx - 1)
        
    def prefix_query(self, idx):
        """Computes prefix sum of up to including the idx-th element"""
        idx += 1
        result = 0
        while idx:
            result += self.array[idx]
            idx -= idx & -idx
        return result
        


# Your RangeSumQuery object will be instantiated and called as such:
# numArray = RangeSumQuery(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
