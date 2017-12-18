# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 11 Dec 2015
# Last update @: 30 Apr 2016

## vocabMainp includes functions for manipulating a vocabulary list.
## For example, an extracted list from a corpus would be processed by
## sorting the list and removing the possible duplications.
## It also changes the upercase to the lower.
## It strips extra spaces at the end of tokens of a list.

###################################################


import os
import sys
import codecs
import csv
import io

import getVocabList
import KurdishStemmer

import matplotlib
# Read the fixed vocabulary list


#provide the proper location where your files are located.
#os.chdir("/home/username/KurdishBLARK")


def getList(inFile):
    vList = []
    with io.open(inFile, 'r', encoding='utf-8') as csvfile:
        text = getVocabList.unicode_csv_reader(csvfile, delimiter=',', quotechar='"')
        for row in text:
            for item in row:
                vList.append(item.lower())
    return vList

##################################################


def makeListOutOfText(text):
    madeList = []

    for row in text:
        for item in row:
            madeList.append(item.lower())

    return madeList

##################################################

def vocabManip(inFile, outFile):
    vListAll = getList(inFile)
    vListAll.sort()
    seen = set()    

    vList = []    
    # Remove duplicate entires
    for node in vListAll:
        if node not in seen:
            vList.append(u'{:}'.format(node))
            seen.add(node)
        
    try:
        outfile = codecs.open(outFile, 'w', encoding = 'utf-8')

        i = 0
        for item in vList:
#            i = i + 1
#            w = u'{: <6}\t{: <25}\n'.format(i, item)
            w = u'{:}\n'.format(item)
            outfile.write(w)

        outfile.close()
    except:
        return # Leave with no harm! (Perhaps I shoul put a proper message here.)

##################################################
def stripBlanks(inFile, outFile):
    vListAll = getList(inFile)
       
    vList = []    
    for node in vListAll:
        vList.append(u'{:}'.format(node.strip()))

    try:
        outfile = codecs.open(outFile, 'w', encoding = 'utf-8')

        i = 0
        for item in vList:
#            i = i + 1
#            w = u'{: <6}\t{: <25}\n'.format(i, item)
            w = u'{:}\n'.format(item)
            outfile.write(w)

        outfile.close()
    except:
        return # Leave with no harm! (Perhaps I shoul put a proper message here.)
##################################################

# Find common words between two lists, which are read from two files
# and write the results into another file.
def commonWords(list1file, list2file, cwfile):
    list1 = getList(list1file)
    list2 = getList(list2file)
    cw = list(set(list1).intersection(list2))
    cw.sort()

    try:
        cwf = codecs.open(cwfile, 'w', encoding = 'utf-8')

        i = 0
        for item in cw:
#            i = i + 1
#            w = u'{: <6}\t{: <25}\n'.format(i, item)
            w = u'{:}\n'.format(item)
            cwf.write(w)

        cwf.close()
    except:
        return # Leave with no harm! (Perhaps I shoul put a proper message here.)

##################################################



##################################################


def mergeFiles():
    mergedfile = codecs.open('merged.txt', 'w', encoding = 'utf-8')

    for i in range(100000, 1537696):
        infilename = str(i)+'.txt'

        if os.path.isfile(infilename):
            infile = codecs.open(infilename, 'r', encoding = 'utf-8')
            if (infile):
                inputtext = infile.read()
                infile.close()
        
                mergedfile.write(inputtext)

    mergedfile.close()

    

##################################################

##################################################

def saveListOutOfFile(inFile, outFile):
    import re
    
    nList = []
    seen = set()
    
    inf = codecs.open(inFile, 'r', encoding = 'utf-8')
    text = inf.read()
    inf.close()

    tregex = re.compile(ur'[$""!£"%$''&:`)(.,?/\'\r\n\t]', re.IGNORECASE)
    sanitizedText1 = tregex.sub(' ', text) # remove special and non-aplha chars
    sanitizedText = re.sub(' +', ' ', sanitizedText1) # remove excessive spaces 

    tokens = re.split(r' ', sanitizedText)
    for node in tokens:
        if node.lower() not in seen:
            nList.append(u'{:}'.format(node.lower()))
            seen.add(node.lower())

    nList.sort()       
    
    try:
        out = codecs.open(outFile, 'w', encoding = 'utf-8')

        i = 0
        for item in nList:
#            i = i + 1
#            w = u'{: <6}\t{: <25}\n'.format(i, item)
            w = u'{:}\n'.format(item)
            out.write(w)

        cwf.close()
    except:
        return # Leave with no harm! (Perhaps I shoul put a proper message here.)


##################################################


# Returns a list of tokens after some data cleaning
# Sorts the list and removes the duplicate entries
def makeSortedUnigueListOutOfFile(inFile):
    import re
    
    nList = []
    seen = set()
    
    inf = codecs.open(inFile, 'r', encoding = 'utf-8')
    text = inf.read()
    inf.close()

    tregex = re.compile(ur'[$""!£"%$''&:`)(.,?/\'\r\n\t]', re.IGNORECASE)
    sanitizedText1 = tregex.sub(' ', text) # remove special and non-aplha chars
    sanitizedText = re.sub(' +', ' ', sanitizedText1) # remove excessive spaces 

    tokens = re.split(r' ', sanitizedText)
    for node in tokens:
        if node.lower() not in seen:
            nList.append(u'{:}'.format(node.lower()))
            seen.add(node.lower())

    nList.sort()       

    return nList    

##################################################

# Remove the duplicates from a lsit and sort ther result
def removeDupsAndSort(inputList):
    outList = []
    seen = set()
    
    for item in inputList:
        if item not in seen:
            outList.append(item)
            seen.add(item)

    outList.sort()
    
    return outList


##################################################

# Returns a list of tokens after some data cleaning
def makeTokenListOutOfFile(inFile):
    import re
    
    nList = []
    
    inf = codecs.open(inFile, 'r', encoding = 'utf-8')
    text = inf.read()
    inf.close()

    tregex = re.compile(ur'[$""!£"%$''&:`)(.,?/\'\r\n\t]', re.IGNORECASE)
    sanitizedText1 = tregex.sub(' ', text) # remove special and non-aplha chars
    sanitizedText = re.sub(' +', ' ', sanitizedText1) # remove excessive spaces 

    tokens = re.split(r' ', sanitizedText)
    for node in tokens:
        nList.append(u'{:}'.format(node.lower()))


    return nList    

##################################################
