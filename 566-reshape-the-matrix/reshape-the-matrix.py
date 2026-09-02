class Solution:

  def matrixReshape(
      self, mat: list[list[int]], r: int, c: int
  ) -> list[list[int]]:
    m, n = len(mat), len(mat[0])

    # If the total number of elements doesn't match, return original matrix
    if m * n != r * c:
      return mat

    # Flatten the matrix into a single list
    flat = [val for row in mat for val in row]

    # Reconstruct the new r x c matrix
    return [flat[i * c : (i + 1) * c] for i in range(r)]