import csv


#takes countryInfo text file from geonames and makes csv
def parseCountriesTxt(newFile, dataFile):
    with open(newFile, 'wt',  newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
          quotechar='|' , quoting=csv.QUOTE_MINIMAL)

        with open(dataFile, newline='') as csvfile2:
             spamreader = csv.reader(csvfile2, delimiter='\t', quotechar='|')
             for row in spamreader:

                 #rows that don't contain data start with #
                 if(row[0][0] != "#"):
                     #print(row[0][0])
                     #print(row)
                     spamwriter.writerow(row)

#takes the countryInfo csv and pulls specific columns
def parseCountriesCsv(newFile, dataFile):
    with open(newFile, 'wt',  newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
          quotechar='|', quoting=csv.QUOTE_MINIMAL)

        with open(dataFile, newline='') as csvfile2:
             spamreader = csv.reader(csvfile2, quotechar='|')
             for row in spamreader:
                 #row[0] - ISO
                 #row[1] - ISO3
                 #row[4] - country name
                 #row[16] - geoID assigned by geonames
                 line = [row[0], row[1], row[4], row[16]]
                 #print(line)
                 spamwriter.writerow(line)


def main():
    parseCountriesTxt('test.csv','../DATA/countryInfo.txt')
    parseCountriesCsv('testFilter.csv', './test.csv')

main()
