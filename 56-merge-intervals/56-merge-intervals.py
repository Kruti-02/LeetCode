class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        results = []
        start = intervals[0][0] # 1, 8, 15
        end = intervals[0][1] # 3, 6, 10, 18
        i = 1
        while i < len(intervals): 
            next_start = intervals[i][0] # 2, 8, 15
            next_end = intervals[i][1] # 6, 10, 18
            if next_start <= end: # true
                if next_end > end: # true
                    end =  next_end
                i+=1
            else:
                results.append([start,end]) # [[1, 6], [8,10]]
                start = intervals[i][0] # 8, 15 
                end = intervals[i][1] # 10, 18
        results.append([start, end])
        return results
           
        
        