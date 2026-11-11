def between_0_and_100(score):
  #check
  if score >= 0 and score <= 100:
    return True
  else:
    return False


score = int(input("Enter your score: "))
if between_0_and_100(score):
  print("Valid Score")
else:
  print("Invalid Score - Must be between 0 and 100")
