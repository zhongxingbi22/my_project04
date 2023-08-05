def swap(a, b):
  """This function swaps the values of two variables.

  Args:
    a: The first variable.
    b: The second variable.

  Returns:
    None.
  """
  temp = a
  a = b
  b = temp

if __name__ == "__main__":
  a = 10
  b = 20

  print("Before: a = {}, b = {}".format(a, b))
  swap(a, b)
  print("After: a = {}, b = {}".format(a, b))
