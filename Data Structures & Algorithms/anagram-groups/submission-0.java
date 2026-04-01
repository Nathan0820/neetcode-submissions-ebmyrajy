class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        
        for (String curr : strs) {
            int[] freq = new int[26];

            for (char c : curr.toCharArray()) {
                freq[c - 'a']++;
            }

            String key = Arrays.toString(freq);
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(curr);
        }
        return new ArrayList<>(map.values());
    }
}
