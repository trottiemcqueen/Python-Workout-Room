#Function ability to call itself

def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

print(sum([15, 12, 5, 1]))

def sums(numbers):
  if not numbers:
    return 0
  remaining_sums = sums(numbers[1:])
  return numbers[0] + remaining_sums

print(sums([5, 10, 15, 20, 25, 30]))
