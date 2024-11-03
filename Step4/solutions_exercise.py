import csv
import matplotlib.pyplot as plt


allData = []
with open('../dataset.csv', newline="") as csvFile:
    csvData = csv.reader(csvFile, delimiter=',')
    for row in csvData:
        allData.append(row)
        
parsedData = []
for row in allData[1:]:
    parsedData.append([row[1],row[3]])
    
data = []
for row in parsedData:
    if "" not in row :
        data.append(row)

platforms = ["PS4","XOne","PC","WiiU"]
genres = ["Action","Adventure","Fighting","Misc","Platform","Puzzle","Racing","Role-Playing","Shooter","Simulation","Sports","Strategy"]

dataDict = {}
for platform in platforms:
    dataDict[platform] = [0,0,0,0,0,0,0,0,0,0,0,0]

for platform in platforms:
    for i,genre in enumerate(genres):
        entries = data.count([platform,genre])
        dataDict[platform][i] += entries

cData = {}
cData["platforms"] = platforms
for key in genres:
    cData[key] = []

for key in platforms:
    for i,genre in enumerate(genres):
        cData[genre].append(dataDict[key][i])

print(cData)
    
fig, ax = plt.subplots(figsize=(14,8))
plt.xticks([x for x in range(len(platforms))],platforms,  fontsize='10')

barWidth = 0.05
barGap = 0.01
x_0 = [x - 9 * barWidth / 2 - 10 * barGap  for x in range(len(platforms))]
x_1 = [x + barWidth + barGap for x in x_0]
x_2 = [x + barWidth + barGap for x in x_1]
x_3 = [x + barWidth + barGap for x in x_2]
x_4 = [x + barWidth + barGap for x in x_3]
x_5 = [x + barWidth + barGap for x in x_4]
x_6 = [x + barWidth + barGap for x in x_5]
x_7 = [x + barWidth + barGap for x in x_6]
x_8 = [x + barWidth + barGap for x in x_7]
x_9 = [x + barWidth + barGap for x in x_8]
x_10 = [x + barWidth + barGap for x in x_9]
x_11 = [x + barWidth + barGap for x in x_10]
ax.bar(x_0,cData["Action"],label="Action",width=barWidth,color="lightcoral")
ax.bar(x_1,cData["Adventure"],label="Adventure",width=barWidth,color="goldenrod")
ax.bar(x_2,cData["Fighting"],label="Fighting",width=barWidth,color="darkgoldenrod")
ax.bar(x_3,cData["Misc"],label="Misc",width=barWidth,color="darkkhaki")
ax.bar(x_4,cData["Platform"],label="Platform",width=barWidth,color="yellowgreen")
ax.bar(x_5,cData["Puzzle"],label="Puzzle",width=barWidth,color="mediumaquamarine")
ax.bar(x_6,cData["Racing"],label="Racing",width=barWidth,color="lightseagreen")
ax.bar(x_7,cData["Role-Playing"],label="Role-Playing",width=barWidth,color="darkturquoise")
ax.bar(x_8,cData["Shooter"],label="Shooter",width=barWidth,color="skyblue")
ax.bar(x_9,cData["Simulation"],label="Simulation",width=barWidth,color="mediumpurple")
ax.bar(x_10,cData["Sports"],label="Sports",width=barWidth,color="orchid")
ax.bar(x_11,cData["Strategy"],label="Strategy",width=barWidth,color="pink")

ax.legend(loc='center left',title="Platforms",bbox_to_anchor=(1, 0.5))

plt.show()


