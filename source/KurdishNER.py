# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 11 April 2016
# Last update @: 10 May 2016

## KurdishNER is the first attempt to build a tool for Name Entity Recognition
## in Kurdish.
## At this stage, finding proper names, in particular person names,
## is the main target.
## The tool uses four instruments to recognize a person name:
##
## 1. A Gazetteer. This includes certain proper names such as zerdeşt, êran,
## nemsa, emerika, and such. It is larger the a normal gazzetteer that is
## usually used for geographical names and such in more established NER
## approaches. 
## 2. A dictionary of Kurdish names. This is larger than the Gazetteer. It includes
## Kurdish person names.
## 3. A dictioanray of Arabic names. It includes most of Arabic names that
## can certainly be identified in Kurdish texts. The nickname/moniker equivalents
## would be kept in item 2 (The dictionary of Kurdish names).
## 4. A bag-of-words. It has been extracted from a large corpus. Here, large
## should be considered in the context of Kurdish. There is corupus that I have
## collected based of different texts and Pewan (http://klpp.github.io/),
## which is mainly based on the news media.
## 5. A set of rules.
##
## What about other foiegn names such as English names?
##
## The method and its five components, as a semi-supervised machine learning
## process, should be expanded and reviewed regularly.
## However, the main goal of this stage is to establish the firs Kurdish NER.
## The quality factors, particularly, the order of algorithm, the efficiency 
## in terms of space and speed, as well as high level of accuracy
## are secondary at this point.

###################################################

import os
import sys
import codecs
import csv
import io
import timeit

import getVocabList
import KurdishStemmer
import vocabManip

import matplotlib


import HH_KCL_Tbx_defs

#os.chdir("/....")

##################################################

def getNameDic(dicFile):
    import re

    nameDic =[]

    nameDic = vocabManip.getList(dicFile)
    
    return nameDic

##################################################


def findPersonNameCandidates(tokens):
    personNameCandidates = []
    personNameCandidatesRuleApplied = []
    pNCTrigramAll = []
    pNCTrigramRA = [] # Trigrams of the more highly probable candidates
                      # with rules applied.

    nameDic = getNameDic(HH_KCL_Tbx_defs.KurdishNameDic)
    gazetteer = getNameDic(HH_KCL_Tbx_defs.KurdishGazetteer)
    # Rarely some Arabic names such as "faris" may be confused with "Iranian"
    # as an adjective. Therfore, "faris" has been palced in Kurdish name dictionary.
    # Assyrian and Chaldean names are also listed in Kurdish name dictionary.
    ArabicNames = getNameDic(HH_KCL_Tbx_defs.KurdishNameDic_Arabic)

    isCandid = False
    isCheckedCandid = False
    isStemmed = False
    stemmedToken = ' '

    # CHECK if stemming helps! ==> ehmedê xanî ==> ehmed xanî

    for token in tokens:
        # The following check should be swapped if the gazetteer entry grows
        # to be larger than Arabic Names list. The reason is the "short-cirrcut"
        # evaluation of the conditions in which it would be more efficient if
        # the shorter list is checked first.
        if(token in gazetteer or token in ArabicNames):
            isCheckedCandid = True
            isStemmed = False
        else:
            stemmed_token = KurdishStemmer.strip_suffix(token)
            if(stemmed_token in gazetteer or stemmed_token in ArabicNames):
                isCheckedCandid = True
                isStemmed = True
                
        # If token is not found in Kurdish Dictionary try with stemmed format of the token. 
            else:
                if(token in nameDic):
                    isCandid = True
                    isStemmed = False
                else:
                    stemmed_token = KurdishStemmer.strip_suffix(token)
                    if (stemmed_token in nameDic):
                        isCandid = True
                        isStemmed = True

                        # If the token is in gazetteer or
                        # If either successor or predecessor is a salutation or
                        # If the successor of the token is a PN companion verb or
                        # it either successor or predecessor is found in the name dictionary
                        # then the toke is highly probably (! needs more check) is a person name.
                        # IT MIGHT BE A COMMA that has separated the names (how to check it?)

                        # In order to apply rules we need to have the surrounding text,
                        # that is, a few words before and after the name candidate. 
                        # As we are interested in using ngrams, when we have annotaed corpus,
                        # we try to simulate a similar situation by trying different order of
                        # ngrams to investigate the efficiency of the method and to find  
                        # an optimum ngram that produces the most accurate result.
                        # For this, we have to find the predecessors and successor indexs
                        # of the list of the tokens of our input text, where we found a name candidate.
                        # We put these ngarams in a corresponding list to our candidate names list
                        # and we apply the checking rules on each candidate name entry alongside
                        # its corresponding ngram entry.
                        if(tokens[tokens.index(token)-1] in HH_KCL_Tbx_defs.KurdishSalutationHead \
                           or tokens[tokens.index(token)+1] in HH_KCL_Tbx_defs.KurdishSalutationTail \
                           or tokens[tokens.index(token)-1] in HH_KCL_Tbx_defs.KurdishPNCompanionWordHead \
                           or tokens[tokens.index(token)+1] in HH_KCL_Tbx_defs.KurdishPNCompanionWordTail \
                           or tokens[tokens.index(token)+1] in gazetteer \
                           or tokens[tokens.index(token)-1] in gazetteer \
                           or tokens[tokens.index(token)+1] in ArabicNames \
                           or tokens[tokens.index(token)-1] in ArabicNames \
                           or tokens[tokens.index(token)+1] in nameDic \
                           or tokens[tokens.index(token)-1] in nameDic \
                           ):
                            isCheckedCandid = True
   
        if(isCheckedCandid == True):
            if (isStemmed == True):
                personNameCandidates.append(stemmed_token)
            else:
                personNameCandidates.append(token)
            temp = tokens[tokens.index(token)-1] + ' ' + token + ' ' + tokens[tokens.index(token)+1]
            pNCTrigramAll.append(temp)
            if (isStemmed == True):
                personNameCandidatesRuleApplied.append(stemmed_token)
            else:
                personNameCandidatesRuleApplied.append(token)
            pNCTrigramRA.append(temp)
            isCheckedCandid = False
        elif(isCandid == True):
            if (isStemmed == True):
                personNameCandidates.append(stemmed_token)
            else:
                personNameCandidates.append(token)
            temp = tokens[tokens.index(token)-1] + ' ' + token + ' ' + tokens[tokens.index(token)+1]
            pNCTrigramAll.append(temp)
            isCandid = False
            
            
    return personNameCandidates, personNameCandidatesRuleApplied,\
           pNCTrigramAll, pNCTrigramRA


##################################################

def isThisaPersonName(token):
    itIsaName = False

    nameDic = getNameDic(HH_KCL_Tbx_defs.KurdishNameDic)

    if(token in nameDic):
        itIsaName = True

    return itIsaName
    

##################################################

def checkNameCandidate(name, trigram):
    itIsaName = False

    nameDic = getNameDic(HH_KCL_Tbx_defs.KurdishNameDic)

    if(token in nameDic):
        itIsaName = True

    return itIsaName

    

##################################################


####### Test Driver #########

#print isThisaPersonName(u'şivan') # Correct result

#print isThisaPersonName(u'emîr')  # Correct result

start_time = timeit.default_timer()

inputList = []
#inputList = vocabManip.getList(HH_KCL_Tbx_defs.KurdishNameDic) # Correct result# Worked fine
#inputList = vocabManip.makeTokenListOutOfFile('lsPewan.txt') # Results in testRun-KurdishNER-on-lsPewan-30Apr2016.txt

#inputList = vocabManip.makeTokenListOutOfFile('kt22.txt') # NOT CORRECT: herdî

#inputList = vocabManip.makeTokenListOutOfFile('arefzeravan.txt')
#inputList = vocabManip.makeTokenListOutOfFile('lst28.txt')
#inputList = vocabManip.makeTokenListOutOfFile('lst29.txt') # This one is a good source for dics
#inputList = vocabManip.makeTokenListOutOfFile('lst15.txt') # bew perî bawer, false finding
#inputList = vocabManip.makeTokenListOutOfFile('lst19.txt') # ewan talan, false finding - names removed from dictionary as they are not popular.
#inputList = vocabManip.makeTokenListOutOfFile('mehmeduzun.txt')

inputList = vocabManip.makeTokenListOutOfFile('KNER_TestData/KNER_TestSample_Sorani_3.txt')

cn, cnWithRA, trigramAll, trigramRA = findPersonNameCandidates(inputList)  # Correct result 

fcn = vocabManip.removeDupsAndSort(cnWithRA)

for n in cn: # Correct result
    print  n

for g in trigramAll:    # Correct result
    print  g

#for i in inputList:
#    print i

print '================================================================='
print '        Execution time: ', timeit.default_timer() - start_time, ' sec'
print '        Number of tokens: ', len(inputList)
print '        Number of trigrames generated: ', len(trigramAll)
print '        Number of candidte names found: ', len(cn)
print '        Number of names after rules applied: ', len(cnWithRA)
print '        Number of final names after duplicates removed: ', len(fcn)
print '================================================================='



#for g in trigramAll:    # Correct result
#    print  g

for g in trigramRA: # Correct result
    print  g

for n in fcn: # Correct result
    print  n

import numpy as np
import matplotlib.pyplot as plt

#d1 = [96,   102,   142,  152, 189, 197,   240, 230, 300,  334,  729, 812, 2304, 603,  11628, 1000, 35172, 120000]
#et = [0.09, 0.10, 0.10, 0.09, 0.02, 0.11, 0.09, 0.19, 0.9, 0.09, 0.11, 0.12, 0.12, 0.10, 0.80, 0.3, 2.49,  4.0]
d1 = [96,   102,   142,  152, 189, 197,   240, 230, 300]
et = [0.09, 0.10, 0.10, 0.09, 0.02, 0.11, 0.09, 0.19, 0.9]
plt.figure(1)
plt.subplot(211)
plt.plot(d1, et, 'k')
plt.show()

