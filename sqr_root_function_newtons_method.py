def sqrt(n):
  x = 1
  iterations = 6 * (10 ** 7)
  while iterations > 0:
    iterations = iterations - 1
    x = (x + n / 2) / 2
  return x
