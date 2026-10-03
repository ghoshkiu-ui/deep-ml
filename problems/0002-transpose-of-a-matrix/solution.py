def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    rows, cols = len(a),len(a[0])
    zero_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            zero_matrix[j][i] = a[i][j]
    return zero_matrix