def age_check(age):
  print(f"You are {age}")
  if age < 18:
    print("You can't drink!")
  elif age == 18 or 19:
    print("You are new to this!")
  elif age > 19 and age < 25:
    print("You are still kind of young!")
  else:
    print("Enjoy your drink!")


age_check(19)