import argparse
import collections
import sys
import os
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/")
import numpy as np
import matplotlib.pyplot as plt

"""
CSapx Project 1: Word Frequency

A program that finds teh median vendor out of a list.  If the program is run
as:

$ python3 Word_freq.py #

The list is gotten from the command line.

author: Julie Sojkowski @ RIT CS
email:jas7845@g.rt.edu
9/16/18
"""

Word = collections.namedtuple("Word", ("name", "year", "count"))


def open_file(filename):
    """
    Creates a dictionary with the word and count
    :param filename: name of the file with the words and years and counts
    :return: word dictionary with just word and count
    """
    word_list = list()
    with open(filename) as file:
        for line in file:
            line = line.split(',')
            word_list.append(Word(name=str(line[0]), year=int(line[1]), count=int(line[2])))

    word_dict = dict()
    for word in word_list:
        if word.name in word_dict:
            word_dict[word.name] += word.count
        else:
            word_dict[word.name] = word.count

    return word_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help=" a word to display the total occurrences of")
    parser.add_argument("filename", help=" a comma separated value unigram file")
    parser.add_argument("-o OUTPUT", "--output OUTPUT", dest="output", type=int,
                        help="display the top OUTPUT (#) ranked words by number of occurrences")
    parser.add_argument("-p", "--plot",
                        help="plot the word rankings from top to bottom based on occurrences", action="store_true")
    args = parser.parse_args()

    filename = str(args.filename)
    num_ranks = int(args.output)
    word = str(args.word)
    plot = args.plot

    if not os.path.isfile(args.filename):
        return sys.stderr.write('Error: the file ' + args.filename + ' does not exist!')
    word_dict = open_file(filename)
    if word not in word_dict:
        return sys.stderr.write('Error: the word ' + args.word + ' does not exist!')

    word_dict = open_file(filename)
    final_val = []
    word_sorted = sorted(word_dict.values(), reverse=True)
    values = list(word_dict.values())

    for i in range(0, len(word_dict)):  # list of words in the correct order with the corresponding count in word_sorted
        final_val.append(list(word_dict.keys())[list(word_dict.values()).index(max(values))])
        values.remove(max(values))
    rank = final_val.index(word)+1
    print(word, "is ranked #", rank)

    for i in range(0, num_ranks):  # prints out each rank, word , and count in order until the user imput is reached
        print("#", i+1, "word: ", final_val[i], "frequency:", word_dict[final_val[i]])

    if plot:
        y_pos = []
        for i in range(0, len(word_dict)):
            y_pos.append(i+1)

        plt.margins(0)

        plt.plot(y_pos, word_sorted, "blue", marker='.')
        plt.plot(rank, word_dict[word], 'r*', markersize=12)
        plt.annotate(word, (rank, word_dict[word]))
        plt.loglog(y_pos, word_sorted, "green")
        plt.tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)  # labels along the bottom edge are off
        plt.ylabel('Total Number of Occurrences')
        xlabel = 'Rank of word ("' + word + '" is rank ' + str(rank) + ')'
        plt.xlabel(xlabel)
        plt.title('Word Frequencies: ' + filename)
        plt.show()

if __name__ == '__main__':
    main()