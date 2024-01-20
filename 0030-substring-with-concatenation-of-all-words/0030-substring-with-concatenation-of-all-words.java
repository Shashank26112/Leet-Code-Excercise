import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        
        if (s == null || words == null || s.length() == 0 || words.length == 0) {
            return result;
        }
        
        int wordLen = words[0].length();
        int wordCount = words.length;
        int totalLen = wordLen * wordCount;

        // Create a map to store the frequency of each word in the words array
        Map<String, Integer> wordFrequency = new HashMap<>();
        for (String word : words) {
            wordFrequency.put(word, wordFrequency.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i <= s.length() - totalLen; i++) {
            String substring = s.substring(i, i + totalLen);
            Map<String, Integer> substringFrequency = new HashMap<>();

            // Check if the current substring is a valid concatenation of words
            for (int j = 0; j < totalLen; j += wordLen) {
                String word = substring.substring(j, j + wordLen);
                substringFrequency.put(word, substringFrequency.getOrDefault(word, 0) + 1);
            }

            if (wordFrequency.equals(substringFrequency)) {
                result.add(i);
            }
        }
        
        return result;
    }
}
