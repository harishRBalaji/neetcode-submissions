class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numberVsFrequencyMap = new HashMap<>();
        for (int num: nums) {
            numberVsFrequencyMap.put(num, numberVsFrequencyMap.getOrDefault(num, 0) + 1);
        }
        List<Map.Entry<Integer, Integer>> keyValueEntryMapList = new ArrayList<>(numberVsFrequencyMap.entrySet());
        keyValueEntryMapList.sort((a, b) -> {
            return Integer.compare(b.getValue(), a.getValue());
        });
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = keyValueEntryMapList.get(i).getKey();
        }
        return result;
    }
}
