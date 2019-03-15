import argparse
import collections
import os
import sys


"""
CSapx Project 1: Word Count

A program that finds teh median vendor out of a list.  If the program is run
as:

$ python3 word_count.py #

The list is gotten from the command line.

author: Julie Sojkowski @ RIT CS
email:jas7845@g.rt.edu
9/16/18
"""

Word = collections.namedtuple("Word", ("name", "year", "count"))


def open_file(filename):
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
    parser.add_argument("word",  help=" a word to display the total occurrences of")
    parser.add_argument("filename", help=" a comma separated value unigram file")
    args = parser.parse_args()
    filename = str(args.filename)
    word = str(args.word)

    if not os.path.isfile(args.filename):
        return sys.stderr.write('Error: the file ' + args.filename + ' does not exist!')

    word_dict = open_file(filename)
    if word in word_dict:
        print(word, ":", word_dict[word])
    else:
        return sys.stderr.write('Error: the word ' + args.word + ' does not exist!')


if __name__ == '__main__':
    main()