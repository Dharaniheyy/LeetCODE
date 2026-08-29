class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            i, j = 0, n - 1
            while i <= j:
                if i == j:
                    row[i] ^= 1
                elif row[i] == row[j]:
                    row[i] ^= 1
                    row[j] ^= 1
                i += 1
                j -= 1
        return image