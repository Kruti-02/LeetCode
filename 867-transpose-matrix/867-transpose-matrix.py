class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        length = len(matrix[0])
        ans = []
        
        for i in range (length):
            result=[]
            for sub_arr in matrix:
                result.append(sub_arr[i])
            ans.append(result)
        return ans
        
        
        