# CS395 Final

import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

IN_FILENAME = "tweets.csv"
OUT_FILENAME = "edges.csv"
BETTER_OUT_FILENAME = "better_edges.csv"
RESULTS_FILENAME = "results.txt"

KEYWORDS = ['illegal', 'aliens', 'refugees', 'biden', 'trump', 'jobs', 'wall', 'greencard', 'visa', 'citizen', 'US',
            '#illegal', '#aliens', '#refugees', '#biden', '#trump', '#jobs', '#wall', '#greencard', '#visa', '#citizen',
            '#US', '#undocumented', 'undocumented']

BETTER_KEYWORDS = ['immigration', '#immigration', 'residents', '#residents', 'immigrants', '#immigrants']



def main():
    # Create a dictionary for the words
    word_dict = {}
    # Open file in read mode
    with open(IN_FILENAME, "r", encoding='utf-8') as csvInFile:
        writeFile = open(OUT_FILENAME, "w", encoding='utf-8')
        csvReader = csv.reader(csvInFile)
        next(csvReader)
        writeFile.write("ID,Keyword\n")
        # For every line in the CSV read in print the row
        for col in csvReader:
            if col[0] != '':
                #print(col[0], col[3].lower())
                splitStrs = col[3].lower().split(" ")
                for word in splitStrs:
                    if word in KEYWORDS:
                        writeFile.write(col[0].strip('"'))
                        writeFile.write(",")
                        if word[0] == '#':
                            #writeFile.write(str(word[1:]))
                            # Add an index instead of a hash word
                            hashed_word = str(hash(word[1:]))
                            word_dict[str(word[1:])] = hashed_word
                            writeFile.write(hashed_word)
                        else:
                            #writeFile.write(str(word))
                            hashed_word = str(hash(word))
                            word_dict[str(word)] = hashed_word
                            writeFile.write(hashed_word)
                        writeFile.write('\n')
    print(word_dict)
    writeFile.close()
    Data = open(OUT_FILENAME, "r")
    next(Data, None)  # skip the first line in the input file
    Graphtype = nx.Graph()

    # Create networkx edge list from csv file data
    G = nx.parse_edgelist(Data, 't', ',', Graphtype, int, (('Keyword', float),))
    for line in Data:
        x = line.rstrip().split(',')
        #print(x[0], x[1])

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
    writeFile.close()

    resultsFile = open(RESULTS_FILENAME, "w", encoding='utf-8')

    # Find communities
    communities = list(greedy_modularity_communities(G))

    # Get largest community
    largest_community = (sorted(communities[0]))

    nx.edges(G)

    # Loop through nodes to write them to file
    # for i in range(len(largest_community)):
    #     resultsFile.write(str(largest_community[i]) + "\n")

    resultsFile.write("# of communities: " + str(len(communities)) + "\n")

    # Compute the degree assortativity coefficients
    assoc = nx.degree_assortativity_coefficient(G)
    # Write Results to file
    resultsFile.write("assortativity: " + str(assoc) + "\n")
    # Get Density
    density = nx.density(G)
    # Write Results to file
    resultsFile.write("density: " + str(density) + "\n")
    # Get Avg Clustering
    avg_clus = nx.average_clustering(G)
    # Write Results to file
    resultsFile.write("average clustering: " + str(avg_clus) + "\n")

    # hex_string = "0x616263"
     #bytes_object = bytes.fromhex(hex_string)
     #ascii_string = bytes_object.decode("ASCII")
    # print(ascii_string)

    resultsFile.close()

    ## //////////////////////////////////////////////////////////////////////////////////
    ## BETTER KEYWORDS
    ## //////////////////////////////////////////////////////////////////////////////////
    with open(IN_FILENAME, "r", encoding='utf-8') as csvInFile:
        writeFile = open(OUT_FILENAME, "w", encoding='utf-8')
        csvReader = csv.reader(csvInFile)
        next(csvReader)
        writeFile.write("ID,Keyword\n")
        # For every line in the CSV read in print the row
        for col in csvReader:
            if col[0] != '':
                #print(col[0], col[3].lower())
                splitStrs = col[3].lower().split(" ")
                for word in splitStrs:
                    if word in BETTER_KEYWORDS:
                        writeFile.write(col[0].strip('"'))
                        writeFile.write(",")
                        if word[0] == '#':
                            writeFile.write(str(hash(word[1:])))
                        else:
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
        #print(x[0], x[1])

    # Create graph
    nx.draw_networkx(G,
                     pos=nx.spring_layout(G, seed=395),
                     edge_color='lightgrey',
                     node_size=3,
                     with_labels=False,
                     node_color='black')
    # Save drawing to file
    plt.savefig('better_graph_plot.pdf')
    plt.show()

    Data.close()
    writeFile.close()

    resultsFile = open(RESULTS_FILENAME, "a", encoding='utf-8')
    resultsFile.write("//////////////////////////////////////////////////\n")
    resultsFile.write("BETTER KEYWORDS RESULTS\n")
    resultsFile.write("//////////////////////////////////////////////////\n")
    # Find communities
    communities = list(greedy_modularity_communities(G))

    # Get largest community
    largest_community = (sorted(communities[0]))
    nx.edges(G)

    # Loop through nodes to write them to file
    # for i in range(len(largest_community)):
    #     resultsFile.write(str(largest_community[i]) + "\n")

    resultsFile.write("# of communities: " + str(len(communities)) + "\n")

    # Compute the degree assortativity coefficients
    assoc = nx.degree_assortativity_coefficient(G)
    # Write Results to file
    resultsFile.write("assortativity: " + str(assoc) + "\n")
    # Get Density
    density = nx.density(G)
    # Write Results to file
    resultsFile.write("density: " + str(density) + "\n")
    # Get Avg Clustering
    avg_clus = nx.average_clustering(G)
    # Write Results to file
    resultsFile.write("average clustering: " + str(avg_clus) + "\n")

    resultsFile.close()
main()
