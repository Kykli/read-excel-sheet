import openpyxl
import pprint

# Open Excel file
wb = openpyxl.load_workbook("FILENAME.xlsx")
sheet = wb["SHEETNAME"]
xData = {}

# Read rows in file and fill xData{}
for row in range(2, sheet.max_row + 1):
    city = sheet["A" + str(row)].value
    streetAddress = sheet["B" + str(row)].value
    postalCode = sheet["C" + str(row)].value
    
    xData.setdefault(city, {streetAddress, postalCode})
    xData.setdefault(streetAddress, {city, postalCode})
    #xData.setdefault(postalCode, {city, streetAddress})

# Write results in file
resultFile = open("FILENAME.py", "w")
resultFile.write("allData =" + pprint.pformat(xData))

resultFile.close()