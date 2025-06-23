class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count=defaultdict(int)
        count=0
        for i in range(len(grid)):
            row_tuple=tuple(grid[i])
            row_count[row_tuple]+=1
        for i in range(len(grid)):
            col_tuple=tuple(grid[j][i] for j in range(len(grid)))
            count+=row_count[col_tuple]

        return count