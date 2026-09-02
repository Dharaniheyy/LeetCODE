import re
from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert banned list to a hash set for O(1) lookup speed
        banned_set = set(banned)
        
        # Replace non-alphanumeric characters with spaces and convert to lowercase
        words = re.findall(r'\w+', paragraph.lower())
        
        # Count frequency of non-banned words
        count = Counter(word for word in words if word not in banned_set)
        
        # Return the most common word
        return count.most_common(1)[0][0]