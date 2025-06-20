class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        temp1=[]
        answer=[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                if nums1[i] not in temp1:
                    temp1.append(nums1[i])
        answer.append(temp1)
        temp2=[]
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                if nums2[i] not in temp2:
                    temp2.append(nums2[i])
        answer.append(temp2)
        return answer