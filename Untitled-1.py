total = 0

while True:
  user_input = int(input("Enter a number(-1 to quit):"))
  print("user typed:", user_input)

  print("Total is now:",  total)
  if user_input==-1:
     break

  total = total + user_input
  print("total at the end of the loop is:", total)

print("Total", total)


