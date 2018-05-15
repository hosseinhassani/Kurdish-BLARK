# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 02 Jan 2015
# Last update @: 22 feb 2016

## GETVOCABLIST reads the fixed vocabulary list in KurmanjiSoraniWeighting.txt and returns a
## cell array of the words
## GETVOCABLIST() reads the fixed vocabulary list in KurmanjiSoraniWeighting.txt 
## and returns a cell array of the words in vocabList.
## GETDIC returns the dictionary

import os
import sys
import codecs
import csv
import io

# Read the fixed vocabulary list


os.chdir("/....")


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]


def getWeightingList():
    weightingList = []
    with io.open('KurmanjiSoraniWeighting.txt', 'r', encoding='utf-8') as csvfile:
        text = unicode_csv_reader(csvfile, delimiter=',', quotechar='"')
        for row in text:
            for item in row:
                weightingList.append(item)
    return weightingList


def getVocabList():
    vocabList = [];
    weightingList = getWeightingList()
    for node in weightingList:
        itemNo, vocab, kurmanjiWeight, soraniWeight = node.split()
        vocabList.append(vocab.encode('utf-8'))
    return vocabList

def getKurmanjiDic(dicfile):
    temp = []
    with io.open(dicfile, 'r', encoding='utf-8') as csvfile:
        text = unicode_csv_reader(csvfile, delimiter=',', quotechar='"')
        for row in text:
            for item in row:
                temp.append(item)

    KurmanjiDic = []
    for node in temp:
        #print (node)
        itemNo, Kurmanji, Sorani = node.split()
        KurmanjiDic.append(u'{: <25}\t{: <4}\t{: <4}'.format(itemNo, Kurmanji, Sorani))

    return KurmanjiDic

def getSoraniDic(dicfile):
    temp = []
    with io.open(dicfile, 'r', encoding='utf-8') as csvfile:
        text = unicode_csv_reader(csvfile, delimiter=',', quotechar='"')
        for row in text:
            for item in row:
                temp.append(item)

    SoraniDic = []
    for node in temp:
        #print (node)
        itemNo, Sorani, Kurmanji = node.split()
        SoraniDic.append(u'{: <25}\t{: <4}\t{: <4}'.format(itemNo, Sorani, Kurmanji))

    return SoraniDic
