investigated_number = int(input("investigated number: "))
while investigated_number >= 10 :
    print ("Please enter a number between 0 through 10")
    investigated_number = int(input("investigated number: "))
while investigated_number <= -1:
    print ("Please enter a number between 0 through 10")
    investigated_number = int(input("investigated number: "))

lower_range_number = int(input("low range number: "))
while lower_range_number <= -1:
    print("Please select a higher number")
    lower_range_number = int(input("low range number: "))

higher_range_number = int(input("high range number: "))
while higher_range_number < lower_range_number:
    print("select a number equal to or higher than your low range number")
    higher_range_number = int(input("high range number: "))

for i in range (lower_range_number, higher_range_number + 1 ):
    print(investigated_number, "x", i, "=", investigated_number*i)