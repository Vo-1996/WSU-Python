with open('example3Input.csv', 'r', encoding='utf-8)') as dataFile:
    for line in dataFile.readlines():
        lineData = (line.strip().split(','))
        if line[0] == 'prism':
            print(lineData)
