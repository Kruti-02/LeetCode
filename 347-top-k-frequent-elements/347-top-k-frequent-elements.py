class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Use hashmap to count occurance of each value
        count = {}
        #Create an array of same size as input array
        freq = [[] for i in range(len(nums)+1)]
        #Go to each value in nums and count how many times it occurs
        for n in nums:
            count[n] = 1+ count.get(n,0)
        # go through each  value that we counted
        for n,c in count.items():
            # In frequency  array : Insert for this particular count i.e index and append the value n
            freq[c].append(n)
        # Create a result output.
        res = []
        #Go through the frequency array and start with last index until 0 and -1 for descending order
        for i in range(len(freq)-1,0,-1):
            #Go for every value in frequency with index i
            for n in freq[i]:
                #Append that value to the result
                res.append(n)
                #stop appending when result output is equal to k
                if len(res) == k:
                    return res
        