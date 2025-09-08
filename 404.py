print("hello user welcome to 404 temp bot")
ForC = input("what would you like to convert to 1 for fahrenheit or 2 for celsius ")
temp = float(input("what is the temperature "))
if ForC == "1":
    result = (temp - 32) * 0.5555
if ForC == ("2"):
    result = temp * 1.8 + 32
print("the temperature is", result, )