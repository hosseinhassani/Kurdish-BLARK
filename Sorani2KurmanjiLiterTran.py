# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 14 Mar 2015
# Last update @: 23 Feb 2016

## Sorani2KurmanjiLiterTran is a literal (word-for-word) translator.
## It uses a dictionary to replace any Sorani word with its equivalent Kurmanji.
## If no such equivalent were found, then the word is left as it was.
## For those words that found in the dictionary, but with their equivlent Kuramnji
## reamind un-set, the dictionary has added two qustion marks ("??")
## to the endo of the word, in order to make the process of setting the reight
## equivalent later.



def Sorani2KurmanjiLiterTran(inputFile, outputFile):
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    infile = codecs.open(inputFile, 'r', encoding = 'utf-8')
    inputText = infile.read()
    infile.close()
    

    # Keep numbers and digits
    # The problem of \r, ., \n, and punctuations still exist.
    tregex = re.compile(ur'[$""!£"%$''&:`)(.,?/\'\r\n]', re.IGNORECASE)
    sanitizedText1 = tregex.sub(' ', inputText) # remove special and non-aplha chars
    sanitizedText = re.sub(' +', ' ', sanitizedText1) # remove excessive spaces 

    words = re.split(r' ', sanitizedText)
    numberOfWords = len(words)

    
    translatedText = []
    targetDic = getVocabList.getKurmanjiDic('/home/hosseinhassani/Hossein/w4u/SoraniKurmanjiDicNew')
    equivalent = False
    newVocab = [] # The vocabulary that were not found in the target dictionary

    for w in words:
        for node in targetDic:
            itemNo, Kurmanji, Sorani = node.split()
            # The following conversion are necessary.
            # I have to find out the reason, as without these conversions.
            # The comparsion of words does not work properly.
            w = u'{}'.format(w);
            Kurmanji = u'{}'.format(Kurmanji);
            Sorani = u'{}'.format(Sorani);
            if (w.lower() == Kurmanji):
                # The equivlent for some Kurmanji words have more than one token.
                # The tokens have been separated in the dictionary with dashes ('-').
                # An re has been used to replace these spearators with blank,
                # make the translated text more natural.
                translatedText.append(Sorani + ' ')
                equivalent = True
                break
            else:
                equivalent = False
                    
        if equivalent <> True:
            translatedText.append(w + ' ')
            # Only interested in alphabetic tokens with at lesst 2 characters
            # Check for duplication in the new vocabs
            if w.isalpha() and len(w) > 1:              
                newVocab.append(w.lower())
            equivalent = True
                
    # Remove duplicates and just send a list of unique new vocabs 
    seen = set()
    uniqueNewVocab = []
    for v in newVocab:
        if v not in seen:
            uniqueNewVocab.append(v)
            seen.add(v)
                

    outfile = codecs.open(outputFile, 'w', encoding = 'utf-8')

    for item in translatedText:
        outfile.write(item)
                                            
    outfile.close()


    return translatedText, uniqueNewVocab, numberOfWords

