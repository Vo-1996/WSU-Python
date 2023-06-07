investigated_number = int(input("investigated number: "))
while investigated_number >= 10 :
    print ("Please enter a number between 0 through 10")
    investigated_number = int(input("investigated number: "))
while investigated_number <= -1:
    print ("Please enter a number between 0 through 10")
    investigated_number = int(input("investigated number: "))

low_range_number = int(input("low range number: "))
while low_range_number <= -1:
    print("Please select a high number")
    low_range_number = int(input("low range number: "))

high_range_number = int(input("high range number: "))
while high_range_number < low_range_number:
    print("select a number equal to or high than your low range number")
    high_range_number = int(input("high range number: "))

for i in range (low_range_number, high_range_number + 1 ):
    print(investigated_number, "x", i, "=", investigated_number*i)