# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 01 March 2015
# Last update @: 01 March 2015

# Kurmanji to Sorani Literal Translator
# This program reads a text in Kurmanji and using sense-for-sense method
# translates it to Sorani. 
# The program later can be augmented by checking the probability of the text
# to be Kurmanji (this can be achieved by using a dialect classifer that has
# currently been written in Octave).


def Kurmanji2SoraniLT(inputFile, outputFile):

    import os
    import unicodedata
    import codecs
    import re

    import getVocabList




    infile = codecs.open(inputFile, 'r', encoding = 'utf-8')
    inputText = infile.read()
    infile.close()

    ## IMPORTANT : replace, sub, and these type of operations, do not
    ## change the input string. They apply the change on a copy of the input string
    ## and return this copy as the result, so always assign them
    ## to another variable, otherwise you will not ge what you want
    ## (THIS COST ME TWO DAYS to understand!)
    ## HH- Dec 4, 2014 - 00:30 am

    tregex = re.compile(ur'[0-9$""!£"%$''&:`)(.,?/\'\r\n]', re.IGNORECASE)
    sanitizedText1 = tregex.sub(' ', inputText) # remove special and non-aplha chars
    sanitizedText = re.sub(' +', ' ', sanitizedText1) # remove excessive spaces 

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
