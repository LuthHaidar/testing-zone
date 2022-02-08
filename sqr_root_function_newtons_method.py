def sqrt(n):
  x = 1
  for i in range(6 * (10 ** 5)):
    x = (x + n / 2) / 2
  return x
