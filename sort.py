
# Sort function implementation
def sort(width, height, length, mass):
  # creating bool varuable with description logic for bulky and heavy
  bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
  heavy = mass >= 20

  # using bulky and heavy variable to implement logic
  if bulky and heavy:
      return "REJECTED"
  elif bulky or heavy:
      return "SPECIAL"
  else:
      return "STANDARD"

  
