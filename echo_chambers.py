# CS395 Final

import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

IN_FILENAME = "tweets.csv"
OUT_FILENAME = "edges.csv"

KEYWORDS = ['illegal', 'aliens', 'refugees', 'biden', 'trump', 'jobs', 'wall', 'greencard', 'visa', 'citizen', 'US',
            '#illegal', '#aliens', '#refugees', '#biden', '#trump', '#jobs', '#wall', '#greencard', '#visa', '#citizen',
            '#US', '#undocumented', 'undocumented']

def main():
        # Open file in read mode
        with open(IN_FILENAME, "r", encoding='utf-8') as csvInFile:
            writeFile = open(OUT_FILENAME, "w", encoding='utf-8')
            csvReader = csv.reader(csvInFile)
            next(csvReader)
            writeFile.write("ID,Keyword\n")
            # For every line in the CSV read in print the row
            for col in csvReader:
                if col[0] != '':
                    print(col[0], col[3].lower())
                    splitStrs = col[3].lower().split(" ")
                    for word in splitStrs:
                        if word in KEYWORDS:
                            writeFile.write(col[0].strip('"'))
                            writeFile.write(",")
                            if word[0] == '#':
                                #writeFile.write(str(word[1:]))
                                writeFile.write(str(hash(word[1:])))
                            else:
                                #writeFile.write(str(word))
                                writeFile.write(str(hash(word)))
                            writeFile.write('\n')
        writeFile.close()
        Data = open(OUT_FILENAME, "r")
        next(Data, None)  # skip the first line in the input file
        Graphtype = nx.Graph()

        # Create networkx edge list from csv file data
        G = nx.parse_edgelist(Data, 't', ',', Graphtype, int, (('Keyword', float),))
        for line in Data:
            x = line.rstrip().split(',')
            print(x[0],x[1])
        # Create graph
        nx.draw_networkx(G,
                pos=nx.spring_layout(G, seed=395),
                edge_color='lightgrey',
                node_size=3,
                with_labels = False,
                node_color='black')
        # Save drawing to file
        plt.savefig('graph_plot.pdf')
        plt.show()

        Data.close()
        # with open(OUT_FILENAME, "r", encoding='utf-8') as graphDataReader:
            # graph = nx.Graph()
            # graphDataReader = csv.reader(graphDataReader)

main()
