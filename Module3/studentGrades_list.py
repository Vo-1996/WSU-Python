

STUDENT_LIST_DATA = [
    [
        "name",
        "CaliforniaTacos",
        "BlueBoxesAndWhatYouCanFitInThem",
        "HowThinCanYouMakeACATCable",
    ],
    ["ricardo", 81, 97, 83],
    ["christina", 81, 94, 69],
    ["james", 99, 80, 95],
    ["brandon", 78, 78, 75],
    ["andrea", 89, 75, 74],
    ["connor", 81, 73, 77],
    ["nicole", 79, 90, 72],
    ["kara", 87, 69, 82],
    ["brian", 87, 82, 71],
    ["sydney", 85, 99, 95],
    ["richard", 85, 78, 74],
    ["emily", 92, 79, 69],
    ["elizabeth", 75, 65, 89],
    ["ashley", 88, 85, 65],
    ["stephanie", 91, 72, 83],
    ["donald", 95, 85, 73],
    ["cory", 80, 66, 67],
    ["daniel", 99, 84, 94],
    ["patricia", 92, 95, 92],
    ["colton", 96, 66, 75],
    ["monica", 73, 85, 81],
    ["brent", 68, 77, 96],
    ["carlos", 86, 93, 98],
    ["virginia", 93, 78, 83],
    ["christopher", 74, 94, 88],
    ["jacob", 96, 66, 90],
    ["peter", 69, 70, 65],
    ["angela", 65, 72, 74],
    ["jennifer", 78, 94, 95],
    ["shane", 82, 82, 81],
    ["william", 90, 83, 86],
    ["dawn", 92, 92, 74],
    ["christine", 81, 65, 71],
    ["chelsea", 68, 95, 91],
    ["deborah", 82, 71, 80],
    ["anne", 87, 89, 76],
    ["anthony", 81, 84, 89],
    ["wendy", 88, 92, 87],
    ["matthew", 92, 90, 85],
    ["teresa", 81, 92, 74],
    ["gabriel", 67, 99, 79],
    ["timothy", 90, 87, 85],
    ["joshua", 98, 80, 94],
    ["alex", 92, 88, 73],
    ["paul", 89, 98, 79],
    ["lynn", 91, 89, 71],
    ["frank", 87, 69, 85],
    ["kimberly", 99, 71, 100],
    ["tara", 99, 75, 67],
    ["patrick", 85, 86, 68],
    ["shannon", 82, 75, 79],
    ["travis", 92, 92, 99],
    ["vincent", 89, 77, 82],
    ["jason", 84, 83, 85],
    ["jessica", 71, 86, 82],
    ["mary", 81, 78, 77],
    ["cassandra", 73, 84, 81],
    ["juan", 71, 70, 81],
    ["nancy", 99, 99, 65],
    ["tyler", 72, 74, 93],
    ["michael", 73, 80, 95],
    ["jade", 86, 87, 71],
    ["zachary", 92, 97, 71],
    ["gary", 82, 74, 81],
    ["meghan", 80, 74, 87],
    ["gloria", 79, 80, 88],
    ["jose", 97, 77, 92],
    ["sara", 89, 67, 80],
    ["linda", 99, 98, 82],
    ["frederick", 88, 76, 70],
    ["veronica", 74, 94, 88],
]

#print(STUDENT_LIST_DATA[1][1])


userInput = str(input("Enter name to search: "))


for names in STUDENT_LIST_DATA:
    if names[0] == userInput:
        #print(names[::1][::1])
        CaliforniaTacos = names[::1][1]
        BlueBoxesAndWhatYouCanFitInThem = names[::1][2]
        HowThinCanYouMakeACATCable = names[::1][3]

        if CaliforniaTacos > BlueBoxesAndWhatYouCanFitInThem and CaliforniaTacos > HowThinCanYouMakeACATCable:
            print(userInput, "CalifoniaTocas is the highest graded assignment!")
        elif BlueBoxesAndWhatYouCanFitInThem > CaliforniaTacos and BlueBoxesAndWhatYouCanFitInThem > HowThinCanYouMakeACATCable:
            print(userInput, "BlueBoxesAndWhatYouCanFitInThem is the highest graded assignment!")
        elif HowThinCanYouMakeACATCable > CaliforniaTacos and HowThinCanYouMakeACATCable > BlueBoxesAndWhatYouCanFitInThem:
            print(userInput, "HowThinCanYouMakeACATCable is the highest graded assignment!")

        mean = (CaliforniaTacos + BlueBoxesAndWhatYouCanFitInThem + HowThinCanYouMakeACATCable) / 3
        print(userInput, "average for the class is", mean)






        #[print(names[0]) for names in STUDENT_LIST_DATA]



#usersInput = str(input("Enter name to search: "))


#for names_in_list in STUDENT_LIST_DATA:
#    print(e)
#    for grades in names_in_list:
#        print()

    #if usersInput == STUDENT_LIST_DATA:
        #print(STUDENT_LIST_DATA[usersInput][::1])