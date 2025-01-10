class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1 # nums1의 마지막 유효 원소의 인덱스
        p2 = n - 1 # nums2의 마지막 원소의 인덱스
        p = m + n - 1 # nums1의 마지막 인덱스

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            
            p -= 1

        