import csv
allData = []

# Theory exercises
def theorySolution():
    with open('../dataset.csv', newline='') as csvFile:
        csvData = csv.reader(csvFile, delimiter=',')
        for row in csvData:
            allData.append(row)

    parsedData = []
    for row in allData[1:]:
        parsedData.append([row[2],row[10],row[12]])
    # Removing entries that are empty
    data = []
    for row in parsedData:
        if "" not in row and 'tbd' not in row:
            data.append(row)

    # Turning values of columns 1 and 2 into floats
    for row in data:
        try:
            row[0] = int(row[0])
            row[1] = float(row[1])
            row[2] = float(row[2])
        except:
            print(row)

    for row in data:
        row[2] *= 10


    # get all years that we have in the dataset
    availableYears = []
    for row in data:
        if row[0] not in availableYears:
            availableYears.append(row[0])

    # crating a dictionary that will have the following structure: year:[nr_entries, total_reviewer_score, total_user_score]
    dataDict = {}
    for year in availableYears:
        dataDict[year] = [0,0,0]
    # merging the data
    for row in data:
        year = row[0]
        dataDict[year][0] += 1
        dataDict[year][1] += row[1]
        dataDict[year][2] += row[2]

    # computing the averages
    for year in dataDict.keys():
        dataDict[year][1] //= dataDict[year][0]
        dataDict[year][2] //= dataDict[year][0]
        # removing the number of games from the table
        dataDict[year].pop(0)

    # flattening the data
    #Now that we have the data we need to turn it into a more convenient form
    cData = dict()
    keys = ["year","critic_review","user_review"]
    for key in keys:
        cData[key] = []
    for key in dataDict.keys():
        cData["year"].append(key)
        cData["critic_review"].append(dataDict[key][0])
        cData["user_review"].append(dataDict[key][1])

    return cData


# Start of exercise solutions

def exerciseSolution():
    allData = []
    with open('../dataset.csv', newline='') as csvFile:
        csvData = csv.reader(csvFile, delimiter=',')
        for row in csvData:
            allData.append(row)

    parsedData = []
    for row in allData:
        parsedData.append([row[1], row[5], row[6], row[7]])
    data = []
    for row in parsedData:
        if "" not in row and row[0] in ["PS4","XOne","PC","WiiU"]:
            data.append(row)

    for row in data:
        row[1] = float(row[1])
        row[2] = float(row[2])
        row[3] = float(row[3])

    # Dictionary : cData {"platform":["PS4","XOne","PC","WiiU"],
    #                      "na_sales": [a, b, c, d],
    #                      "eu_sales": [a, b, c, d],
    #                      "jp_sales": [a, b, c, d]}

    cData = {}
    cData["platform"] = ["PS4","XOne","PC","WiiU"]
    cData["na_sales"] = [0,0,0,0]
    cData["eu_sales"] = [0,0,0,0]
    cData["jp_sales"] = [0,0,0,0]

    for row in data:
        platform = row[0]
        column = cData["platform"].index(platform)
        cData["na_sales"][column] += row[1]
        cData["eu_sales"][column] += row[2]
        cData["jp_sales"][column] += row[3]

    return cData

print(theorySolution())