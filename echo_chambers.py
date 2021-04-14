# CS395 Final

import csv
import networkx as nx
import matplotlib.pyplot as plt

IN_FILENAME = "tweets.csv"
OUT_FILENAME = "edges.csv"

KEYWORDS = ['illegal', 'aliens', 'refugees', 'biden', 'trump', 'jobs', 'wall', 'greencard', 'visa', 'citizen', 'US',
            '#illegal', '#aliens', '#refugees', '#biden', '#trump', '#jobs', '#wall', '#greencard', '#visa', '#citizen',
            '#US', '#undocumented', 'undocumented']

def main():

        graph = nx.Graph()
        with open(IN_FILENAME, "r", encoding='utf-8') as csvInFile:
            writeFile = open(OUT_FILENAME, "w", encoding='utf-8')
            csvReader = csv.reader(csvInFile)
            next(csvReader)
            for row in csvReader:
                print(row[0], row[3].lower())
                splitStrs = row[3].lower().split(" ")
                for word in splitStrs:
                    if word in KEYWORDS:
                        writeFile.write(row[0].strip('"'))
                        writeFile.write(", ")
                        writeFile.write(word)
                        writeFile.write('\n')


main()
