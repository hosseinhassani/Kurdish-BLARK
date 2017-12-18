# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 27 Dec 2014
# Last update @: 08 Mar 2015

## BUILDWEIGHTINGLIST preprocesses tokenizes an input text
## and maintains a counter for each word.
## It then looks up each word in the weightingList.
## If the word exist in the list it does nothing,
## else it adds the word to the list.
## It uses the following criteria to add a word to the list
## and assigns a factor of 100 to the word
##

def buildWeightingList(inputFile, dialect, outputFile):
# inputFile is a Kurdish tex in Lattin scrip.
# dialect is the major dialect of the text : Kurmanji or Sorani
# outputFile is the file the wegitng list will be created.

###########################################################
#####  It works for Persian/Arabic script as well!  #######
###########################################################
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    # os.chdir("/home/hossein/w4u")

    # infile = codecs.open('LSorani5.txt', encoding = 'utf-8')
    # infile = codecs.open(inputFile, encoding = 'utf-8')
    infile = codecs.open(inputFile, 'r', encoding = 'utf-8')
    inputText = infile.read()
    infile.close()

    #print inputText

    ## IMPORTANT : replace, sub, and these type of operations, do not
    ## change the input string. They apply the change on a copy of the input string
    ## and return this copy as the result, so always assign them
    ## to another variable, otherwise you will not ge what you want
    ## (THIS COST ME TWO DAYS to understand!)
    ## HH- Dec 4, 2014 - 00:30 am

##################################################################
# “ “Típén …hwd ′an  FINd SOLUTION FOR THIS CASE - re with unicode
##################################################################


    tregex = re.compile(ur'[0-9$""!£"%$''&:`)(.,?/\'\r\n]', re.IGNORECASE)
    sanitizedText1 = tregex.sub(' ', inputText) # remove special and non-aplha chars
    sanitizedText = re.sub(' +', ' ', sanitizedText1) # remove excessive spaces 

    #print sanitizedText

    words = re.split(r' ', sanitizedText)

    # find and remove words with multiple occurences
    # create a new list that contains a single occurence of each word
    dicwords = []  
    for w in words:
        if w not in dicwords:
            dicwords.append(w)

    f1 = 0
    f2 = 0 
    if (dialect == 'Kurmanji'):
        f1 = 100
    elif (dialect == 'Sorani'):
        f2 = 100


    newWeightingList = []
    weightingList = getVocabList.getWeightingList()
    newWord = False

    for w in dicwords:
        if (len(w) >= 2):
            for node in weightingList:
                itemNo, vocab, kurmanjiWeight, soraniWeight = node.split()
#                print(itemNo)
                if (w == vocab):
                    if (dialect == 'Kurmanji'):
                        newWeightingList.append(u'{: <25}\t{: <4}\t{: <4}'.format(w, 100, soraniWeight))
                    else:
                        if (dialect == 'Sorani'):
                            newWeightingList.append(u'{: <25}\t{: <4}\t{: <4}'.format(w, kurmanjiWeight, 100))
                        else:
                            newWeightingList.append(u'{: <25}\t{: <4}\t{: <4}'.format(w, kurmanjiWeight, soraniWeight))
                    weightingList.pop(weightingList.index(node))
                    newWord = False
                    break
                else:
                    newWord = True
                    
            if newWord:
                newWeightingList.append(u'{: <25}\t{: <4}\t{: <4}'.format(w, f1, f2))
                newWord = False

    for node in weightingList:
        itemNo, vocab, kurmanjiWeight, soraniWeight = node.split()
        newWeightingList.append(u'{: <25}\t{: <4}\t{: <4}'.format(vocab, kurmanjiWeight, soraniWeight))

    newWeightingList.sort()

    outfile = codecs.open(outputFile, 'w', encoding = 'utf-8')
        
    i = 0
    for item in newWeightingList:
       i = i + 1
       w = u'{: <6}\t{: <25}\n'.format(i, item)
       outfile.write(w)
                                            
    outfile.close()

##############################################################################        
