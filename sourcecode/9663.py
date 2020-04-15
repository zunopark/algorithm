n = int(input())
final = []

def is_avail(candidate, current_col):
    current_row = len(candidate)
    for row in range(current_row):
        if candidate[row] == current_col or abs(candidate[row]-current_col) == current_row - row:
            return False
    return True


def DFS(n, current_row, current_candidate, final):
    if current_row == n:
        final.append(current_candidate[:])
        return
    
    for col in range(n):
        if is_avail(current_candidate, col):
            current_candidate.append(col)
            DFS(n, current_row+1, current_candidate, final)
            current_candidate.pop()
    
DFS(n, 0, [], final)
print(final)