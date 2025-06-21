class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res=defaultdict(int)
        for i in range(len(arr)):
            res[arr[i]]=1+res.get(arr[i],0)
        res1=[]
        for val,cnt in res.items():
            res1.append(cnt)
        res1.sort()
        for i in range(len(res1)-1):
            if res1[i]==res1[i+1]:
                return False
        return True