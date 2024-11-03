import csv

import matplotlib.pyplot as plt


def theorySolution():
    fig, ax = plt.subplots(figsize=(12, 8))

    trees = [["North America","Latin America","Africa","Asia and the Pacific","Europe"],
             [10.9           ,4.3            ,2.6     ,5.0                   ,0.6],
             [12.3           ,6.7            ,3.3     ,6.5                   ,0.7]]
    numberPoints = len(trees[0])
    barWidth = 0.2
    barGap = 0.05
    x_1 = [x-barWidth/2 - barGap/2 for x in range(numberPoints)]
    x_2 = [x+barWidth/2 + barGap/2 for x in range(numberPoints)]
    ax.bar(x_1,trees[2],width=barWidth, label="2020",color=(.2,.1,.5,.9))
    ax.bar(x_2,trees[1],width=barWidth, label="2023")
    ax.legend(loc='center left', title="year", bbox_to_anchor=(1, 0.5))
    plt.xticks([x for x in range(numberPoints)],trees[0],  fontsize='10')
    plt.show()



def exerciseSolution():
    data = exerciseSolutionCSV()
    print(data)
    fig, ax = plt.subplots(figsize=(14, 8))

    plt.xticks([x for x in range(len(data["platform"]))], data["platform"], fontsize='10')
    barWidth = 0.2
    barGap = 0.05
    x_0 = [x - barWidth - barGap for x in range(len(data["platform"]))]
    x_1 = [x for x in range(len(data["platform"]))]
    x_2 = [x + barWidth + barGap for x in x_1]

    ax.bar(x_0, data["na_sales"], label="NA sales", width=barWidth)
    ax.bar(x_1, data["eu_sales"], label="EU sales", width=barWidth)
    ax.bar(x_2, data["jp_sales"], label="JP sales", width=barWidth)

    ax.legend(loc='center left', title="Platforms", bbox_to_anchor=(1, 0.5))
    plt.show()

def exerciseSolutionCSV():
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

exerciseSolution()