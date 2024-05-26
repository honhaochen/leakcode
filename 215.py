from typing import List, Union


class MaxHeap:

    def __init__(self):
        self.arr: List[int] = []

    def pop(self) -> Union[int, None]:
        if len(self.arr) == 0:
            return None

        if len(self.arr) == 1:
            return self.arr.pop()

        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        res = self.arr.pop()
        self.heapify(0)
        return res

    def push(self, x: int) -> None:
        self.arr.append(x)
        index = len(self.arr) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.arr[index] > self.arr[parent_index]:
                self.arr[index], self.arr[parent_index] = (
                    self.arr[parent_index],
                    self.arr[index],
                )
                index = parent_index
            else:
                break

    def heapify(self, index: int) -> None:
        larger_index = index
        if (
            2 * index + 1 < len(self.arr)
            and self.arr[larger_index] < self.arr[2 * index + 1]
        ):
            larger_index = 2 * index + 1

        if (
            2 * index + 2 < len(self.arr)
            and self.arr[larger_index] < self.arr[2 * index + 2]
        ):
            larger_index = 2 * index + 2

        if index == larger_index:
            return

        self.arr[index], self.arr[larger_index] = (
            self.arr[larger_index],
            self.arr[index],
        )
        return self.heapify(larger_index)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        m = MaxHeap()
        for x in nums:
            m.push(x)

        for _ in range(k - 1):
            m.pop()

        return m.pop()


s = Solution()
a = s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(a)
