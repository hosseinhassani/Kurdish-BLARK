# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 12 Mar 2015
# Last update @: 19 Feb 2016

## commonKuSoVocab preprocesses the created vocabulary
## in order to find the number of common words among the two
## dialects: Kuramnji and Sorani.
## The function finds the commonality based on the assigned
## weighting, currently 100.
##

def commonKuSoVocab():
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    # os.chdir("/...")


    newWeightingList = []
    commonVocab = []
    weightingList = getVocabList.getWeightingList()
    
    allVocabNo = 0
    commonVocabNo = 0
    KurmanjiVocabNo = 0
    SoraniVocabNo = 0
    weight = '100'

    for node in weightingList:
        itemNo, vocab, kurmanjiWeight, soraniWeight = node.split()
        allVocabNo += 1
        if (kurmanjiWeight == soraniWeight):
            commonVocabNo += 1
            commonVocab.append(vocab)
            
        if (kurmanjiWeight == weight.encode('utf-8' )):
            KurmanjiVocabNo += 1
        elif (soraniWeight == weight.encode('utf-8' )):
            SoraniVocabNo += 1            

    commonVocabPerecntage = (commonVocabNo * 100) / allVocabNo
    commonVocabPerecntage2K = (commonVocabNo * 100) / KurmanjiVocabNo
    commonVocabPerecntage2S = (commonVocabNo * 100) / SoraniVocabNo
    
    print(allVocabNo, KurmanjiVocabNo, SoraniVocabNo, commonVocabNo)
    print(commonVocabPerecntage, commonVocabPerecntage2K, commonVocabPerecntage2S)
    print commonVocab
    return commonVocabNo, commonVocab, allVocabNo, KurmanjiVocabNo, SoraniVocabNo

#commonKuSoVocab()
