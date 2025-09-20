import heapq
nums = [2, 1, 3, 2, 3, 2, 2, 3, 1, 0, 0, 0, 0, 0, 5]
k = 2
result = [0, 2]

def top_freq_elem(nums, k):
    counter = {}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0) #O(n)
    sort_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[:k]
    result = []
    for val in sort_counter:
        result.append(val[0])
    return result
   
def topFreqElement(nums, k):
    count = {}
    freq_map = [[] for i in range(len(nums))]
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, freq in count.items():
        freq_map[freq].append(num)

    result = []
    for i in range(len(freq_map)-1,0,-1):
        for num in freq_map[i]:
            result.append(num)
            if len(result) == k:
                return result

def topFreqElm(nums, k):
    counter = {}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)
    min_heap = []
    for num, freq in counter.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        elif min_heap[0][0] < freq:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (freq, num))
    return [num for freq, num in min_heap]
           


print(top_freq_elem(nums, 2))
print(topFreqElement(nums, 2))
print(topFreqElm(nums, 2))