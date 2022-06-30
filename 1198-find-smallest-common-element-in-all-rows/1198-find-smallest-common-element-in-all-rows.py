class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        m = len(mat)
        n = len(mat[0])
        
        for i in range(n):
            current_element = mat[0][i]
            found = True
            for j in range(1 , m):
                ind = bisect.bisect_right(mat[j] , current_element) -1
                #print(mat[j] , ind , current_element)
                if mat[j][ind] != current_element or ind == -1:
                    found = False   
            if found:
                return current_element
        
        return -1