class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        max_str = set();
        max_len = 0;
        left = 0;
        right = 0;
        
        while (left < n):
            if(s[left] not in max_str):
                max_str.add(s[left])
                left+=1
            else:
                max_len = max(max_len,len(max_str));
                max_str.remove(s[right])
                right+=1
        
        return max(max_len, len(max_str));
        
