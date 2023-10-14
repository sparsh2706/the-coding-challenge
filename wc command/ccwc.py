#!/usr/bin/env python3

import os
import argparse
import sys

def count_bytes(data=None, filename=None):
    """Counts the number of bytes in a File"""
    if filename:
        return os.stat(filename).st_size
    else:
        return len(data.encode('utf-8'))


def count_lines(data=None, filename=None):
    """Counts the number of lines in a File"""
    if filename:
        with open(filename) as f:
            data = f.read()
    return len(data.splitlines())
    

def count_words(data=None, filename=None):
    """Counts the number of words in a File"""
    if filename:
        with open(filename) as f:
            data = f.read()
    
    return len(data.split())


def count_chars(data=None, filename=None):
    """Counts the number fo characters in a File"""
    if filename:
        with open(filename) as f:
            data = f.read()
    return len(data)


def output(bytes, lines, words, chars, filename):
    """Prints the Output"""
    counts = {
        'lines': lines,
        'words': words,
        'bytes': bytes,
        'chars': chars
    }
    
    output_str = ''.join((str(counts[key]) + ' ') for key in counts if counts[key] != -1)
    print(f'{output_str} {filename}')


def parser_args():
    """Arguments to pass executing the command"""
    parser = argparse.ArgumentParser(description='wc command utility')
    # Takes optional argument '-c' to count bytes
    parser.add_argument('-c', action='store_true', help='Count number of bytes in File')
    parser.add_argument('-l', action='store_true', help='Count number of lines in File')
    parser.add_argument('-w', action='store_true', help='Count number of words in File')
    parser.add_argument('-m', action='store_true', help='Count number of characters in File')
    
    parser.add_argument('file', type=str, nargs='?', default='', help='File to process')
    # nargs makes the file optionala argument
    
    return parser.parse_args()


def main():

    args = parser_args()
    
    if not args.file:
        data = sys.stdin.read()
    else:
        data = None
        
    byte_count = -1
    line_count = -1
    word_count = -1
    char_count = -1

        
    if args.c:
        byte_count = count_bytes(data, args.file)
    
    if args.l:
        line_count = count_lines(data, args.file)
        
    if args.w:
        word_count = count_words(data, args.file)
    
    if args.m:
        char_count = count_chars(data, args.file)
    
    if not args.c and not args.l and not args.w and not args.m:
        byte_count = count_bytes(data, args.file)
        line_count = count_lines(data, args.file)
        word_count = count_words(data, args.file)

        
    output(byte_count, line_count, word_count, char_count, args.file)
    

if __name__ == '__main__':
    main()

# To make the script executable: chmod +x ccwc.py
# Run the script as a command: ./ccwc.py -c test.txt
