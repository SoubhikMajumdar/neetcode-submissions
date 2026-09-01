class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> freq;
        
        int longest = 0;
        int left = 0;
        int max_freq = 0;

        for (int right = 0; right < s.size(); right++) {
            freq[s[right]]++;

            max_freq = max(max_freq, freq[s[right]]);

            while ((right - left + 1) - max_freq > k) {
                freq[s[left]]--;
                left++;
            }

            longest = max(longest, right - left + 1);
        }

        return longest;
    }
};
