class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numberVsFrequencyMap = new HashMap<>();
        for (int num: nums) {
            numberVsFrequencyMap.put(num, numberVsFrequencyMap.getOrDefault(num, 0) + 1);
        }
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> {
            return a[0] - b[0];
        });
        for (Map.Entry<Integer, Integer> entry: numberVsFrequencyMap.entrySet()) {
            minHeap.offer(new int[]{entry.getValue(), entry.getKey()});
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = minHeap.poll()[1];
        }
        return result;
    }
}
