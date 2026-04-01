class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1); //HERE
        }

        for (int i = 0; i < t.length(); i++) {
            char d = t.charAt(i);
            map.put(d, map.getOrDefault(d, 0) - 1); //HERE
        }

				//final check
        for (int val : map.values()) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
}
