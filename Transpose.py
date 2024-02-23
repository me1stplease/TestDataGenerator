def transpose(A, B, M, N):
    for i in range(N):
        for j in range(M):
            B[i][j] = A[j][i]
