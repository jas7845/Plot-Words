import argparse
import collections
import string
import sys
import os
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/")
import numpy as np
import matplotlib.pyplot as plt

"""
CSapx Project 1: Letter Frequency

A program that finds teh median vendor out of a list.  If the program is run
as:

$ python3 letter_freq.py #

The list is gotten from the command line.

author: Julie Sojkowski @ RIT CS
email:jas7845@g.rt.edu
9/16/18
"""

Word = collections.namedtuple("Word", ("name", "year", "count"))


def open_file(filename):
    """
    opens the file and creates a dictionary with all the letters and counts
    :param filename: file name to look through
    :return: dictionary with alphabet letters and the sum of each occurence
    """
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    word_list = list()
    with open(filename) as file:
        for line in file:
            line = line.split(',')
            word_list.append(Word(name=str(line[0]), year=int(line[1]), count=int(line[2])))

    word_dict = dict()

    for i in word_list:
        if i.name in word_dict:
            word_dict[i.name] += i.count
        else:
            word_dict[i.name] = i.count
    for word in word_dict:
        for letter in word:
            if letter in alphabet:
                alphabet[letter] += word_dict[word]
    return alphabet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help=" a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display letter frequencies to standard output", action="store_true")
    parser.add_argument("-p", "--plot", help="plot letter frequencies using matplotlib", action="store_true")
    args = parser.parse_args()
    filename = str(args.filename)
    output = args.output
    plot = args.plot
    alphabet = open_file(filename)
    sum = 0
    objects = []
    numbers = []

    if not os.path.isfile(args.filename):
        return sys.stderr.write('Error: the file ' + args.filename + ' does not exist!')

    for letter in alphabet:
        sum += alphabet[letter]

    if output:
        print(output)
        for letter in alphabet:
            print(letter, ":", alphabet[letter] / sum)

    if plot:
        for letter in alphabet:
            numbers.append(alphabet[letter] / sum)

        for key in alphabet:
            objects.append(key)

        y_pos = np.arange(len(objects))
        plt.bar(y_pos, numbers, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Frequency')
        plt.xlabel('Letter')
        plt.title('Letter Frequencies: ' + filename)

        plt.show()


if __name__ == '__main__':
    main()
