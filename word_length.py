import argparse
import sys
import os
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/")
import numpy as np
import matplotlib.pyplot as plt

"""
CSapx Project 1: Word Frequency

A program that finds average word length.  If the program is run
as:

$ python3 word_freq.py #

The list is gotten from the command line.

author: Julie Sojkowski @ RIT CS
email:jas7845@g.rt.edu
9/16/18
"""


def open_file(filename):
    year_dict = dict()
    with open(filename) as file:
        for line in file:
            line = line.split(',')
            word = line[0]
            year = int(line[1])
            count = int(line[2])
            if year in year_dict:
                tot_count = year_dict[year][0] + count
                tot_len = year_dict[year][1] + count*len(word)
                year_dict[year] = (tot_count, tot_len)
            else:
                year_dict[year] = (count, count*len(word))
    return year_dict


def year_frequency_dict(year_dict, start, end):
    """
    makes a new dict with year, frequency
    :param year_dict: dictionary with year, (count, total letters)
    :param start: start year
    :param end:  end year
    :return: dictionary with year: frequency
    """
    year_freq_dict = dict()
    for year in range(start, end+1):
        if year in year_dict:
            year_freq_dict[year] = year_dict[year][1]/year_dict[year][0]
    return year_freq_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start",  help=" the starting year range")
    parser.add_argument("end", help=" the ending year range")
    parser.add_argument("filename", help=" a comma separated value unigram file")
    parser.add_argument("-o", "--output",
                        help="display the average word lengths over years", action="store_true")
    parser.add_argument("-p", "--plot",
                        help=" plot the average word lengths over years", action="store_true")
    args = parser.parse_args()
    end = int(args.end)
    start = int(args.start)
    filename = str(args.filename)
    if start > end:
        return sys.stderr.write('Error: start year must be less than or equal to end year!')
    if not os.path.isfile(args.filename):
        return sys.stderr.write('Error: the file ' + args.filename + ' does not exist!')
    output = args.output
    plot = args.plot
    year_dict = open_file(filename)

    year_fd = year_frequency_dict(year_dict, start, end)  # make dict with year, frequency
    year = start
    if output:
        for key in year_fd:  # prints out each year and frequency in order until the user imput is reached
            if key <= end or key <= start:
                print(key, ": ", year_fd[key])
                year += 1

    if plot:  # plots the graph from start date to end date
        x_pos = []
        y_pos = []
        for i in range(start, end+1):
                x_pos.append(i)
        year = start
        for key in year_fd:
            if year <= end:
                y_pos.append(year_fd[key])
                year += 1
        plt.margins(0)
        plt.plot(x_pos, y_pos, "blue", marker='.')
        plt.tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=True,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=True)  # labels along the bottom edge are off
        plt.ylabel('Average Word Length')
        plt.xlabel('Year')
        plt.title('Average Word Lengths from ' + str(start) + ' to ' + str(end) + ': '+ filename)
        plt.show()


if __name__ == '__main__':
    main()
