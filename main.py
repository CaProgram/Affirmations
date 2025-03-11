print("Hello. Welcome to your affirmation generator.")
name = input("What is your name? ")

if name == "David" or name == "david":
  DOW = input("What day of the week is it? ")
  if DOW == "monday" or DOW == "Monday":
    print("It is going to be a great Monday!", name)
  if DOW == "tuesday" or DOW == "Tuesday":
    print("It is going to be a awesome Tuesday!", name)
  if DOW == "wednesday" or DOW == "Wednesday":
    print("It is going to be a fabulous Wednesday!", name)
  if DOW == "thursday" or DOW == "Thursday":
    print("It is going to be a terrific Thursday!", name)
  if DOW == "friday" or DOW == "Friday":
    print(name, "It is the best day of the week, Friday!")
elif name == "Mark" or name == "mark":
  DOW = input("What day of the week is it? ")
  if DOW == "monday" or DOW == "Monday":
    print("It is going to be a great Monday!", name)
  if DOW == "tuesday" or DOW == "Tuesday":
    print("It is going to be a terrific Tuesday!", name)
  if DOW == "wednesday" or DOW == "Wednesday":
   print("It is going to be a fabulous Wendesday!", name)
  if DOW == "thursday" or DOW == "Thursday":
    print("It is going to be an awesome Thursday!", name)
  if DOW == "friday" or DOW == "Friday":
    print(name, "It is the best day of the week, Friday!")
else:
  print("I don't know your name, but I hope you are having a wonderful day!")