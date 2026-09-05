int lengthOfLongestSubstring(char* s){
    int last[256];
    for(int i = 0; i < 256; i++)
        last[i] = -1;

    int maxLen = 0;
    int left = 0;

    for(int right = 0; s[right] != '\0'; right++) {
        if(last[s[right]] >= left) {
            left = last[s[right]] + 1;
        }

        last[s[right]] = right;

        int len = right - left + 1;
        if(len > maxLen)
            maxLen = len;
    }

    return maxLen;
}