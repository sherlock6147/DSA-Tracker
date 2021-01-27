import openpyxl
import json
#pah of file
pathOfFile = ("FINAL450 DSA.xlsx")
# Open the Workbook
workbook = openpyxl.load_workbook(pathOfFile)
# Get the sheet
sheet = workbook.active
# Get the topics
topicsSet = {""}
for i in range(6, 481):
    cell = 'A' + str(i)
    topicsSet.add(sheet[cell].value)
topicsSet.remove("")
# Get the different projects
print(len(topicsSet))
# Get all the problems into a list of Problems
listOfProblems = []
for i in range(6, 481):
    topicCell = 'A' + str(i)
    problemCell = 'B' + str(i)
    status = False
    problem = {}
    if (sheet[topicCell].value == None):
        continue
    problem["topic"] = sheet[topicCell].value
    problem["problemStatement"] = sheet[problemCell].value
    problem["status"] = status
    listOfProblems.append(problem)
pathForJSONFile = "/Outputs/listOfProblems.json"
outputFile = open(pathForJSONFile, "w")
json.dump(listOfProblems,outputFile,indent=4)
print(listOfProblems)