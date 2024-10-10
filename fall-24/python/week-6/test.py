arr = [11, 13, 25, 28, 35, 45, 55, 60, 65]
T = 60
def binary_search(arr, t):
  L = 0
  R = len(arr) - 1

  while L <= R:
    M = (L + R) // 2
    if arr[M] == 60:
      return M
    elif arr[M] < T:
      L = M +1
    else:
      R = M - 1
  return -1

print(binary_search(arr, T))