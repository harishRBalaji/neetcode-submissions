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
        List<Integer> resultList = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            resultList.add(keyValueEntryMapList.get(i).getKey());
        }
        int[] result = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            result[i] = resultList.get(i);
        }
        return result;
    }
}
