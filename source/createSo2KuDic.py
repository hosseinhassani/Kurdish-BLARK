# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 13 Mar 2015
# Last update @: 23 Feb 2016

## createSo2KuDic preprocesses the created vocabulary
## in order to find the Sorani words whose weighting are zero alongside
## common vocabulary among the two dialects: Kuramnji and Sorani.

def updateSo2KuDic(dicFile, newVocabList):
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    updatedVocabList = []
    seen = set()
    
    currentVocabList = getVocabList.getSoraniDic(dicFile)
    
    # Format current dic to be ready for merging with the new vocabs
    for node in currentVocabList:
        itemNo, Sorani, Kurmanji = node.split()
        updatedVocabList.append(u'{: <25}\t{: <4}'.format(Sorani, Kurmanji))
        seen.add(Sorani.lower())

        
    # Merge the new vocabs with the existing dictionary
    for node in newVocabList:
        Sorani, Kurmanji = node.split()
        if Sorani.lower() not in seen:
            updatedVocabList.append(u'{: <25}\t{: <4}'.format(Sorani, Kurmanji))
        
    updatedVocabList.sort()

    try:
        outfile = codecs.open(dicFile, 'w', encoding = 'utf-8')

        i = 0
        for item in updatedVocabList:
            i = i + 1
            w = u'{: <6}\t{: <25}\n'.format(i, item)
            outfile.write(w)

        outfile.close()
    except:
        return # Leave with no harm! (Perhaps I shoul put a proper message here.)

##################################################

    
##################################################
def mergeKu2SoDic(SDic, KDic):
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    updatedVocabList = []
    
    currentVocabList = getVocabList.getSoraniDic(SDic)
    Ku2SoDic = getVocabList.getKurmanjiDic(KDic)
    
    seen = set() # This set is used to check the duplicates
    # Format current dic to be ready for merging with the new vocabs
    for node in currentVocabList:
        itemNo, Sorani, Kurmanji = node.split()
        seen.add(Sorani) # There shouldn't be duplicates in the curretn dic
        updatedVocabList.append(u'{: <25}\t{: <4}'.format(Sorani, Kurmanji))
        
    # Merge the vocabs from the Kurmanji-to-Sorani wich do not exist
    # in the current Sorani-to-Kurmanji dictionary
    for node in Ku2SoDic:
        itemNo, Kurmanji, Sorani = node.split()
        if Sorani not in seen:
            seen.add(Sorani)
            updatedVocabList.append(u'{: <25}\t{: <4}'.format(Sorani, Kurmanji))
           

    updatedVocabList.sort()


    try:
        outfile = codecs.open(SDic, 'w', encoding = 'utf-8')

        i = 0
        for item in updatedVocabList:
            i = i + 1
            w = u'{: <6}\t{: <25}\n'.format(i, item)
            outfile.write(w)

        outfile.close()
    except:
        return # Leave with no harm! (Perhaps I shoul put a proper message here.)

##################################################


def createSo2KuDic():
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    os.chdir('/home/hosseinhassani/Hossein/w4u')


    weightingList = getVocabList.getWeightingList()
    
    allVocab = 0
    commonVocab = 0
    KurmanjiVocab = 0
    SoraniVocab = 0
    weight = '100'
 
    SoraniKurmanjiDic = []
    for node in weightingList:
        itemNo, vocab, kurmanjiWeight, soraniWeight = node.split()
#        print(itemNo, kurmanjiWeight, soraniWeight)
        if ((kurmanjiWeight == soraniWeight) or (soraniWeight == weight.encode('utf-8' ))):
            SoraniKurmanjiDic.append(u'{: <25}\t{: <4}'.format(vocab, vocab))

    outfile = codecs.open('SoraniKurmanjiDic', 'w', encoding = 'utf-8')

    i = 0
    for item in SoraniKurmanjiDic:
       i = i + 1
       w = u'{: <6}\t{: <25}\n'.format(i, item)
       outfile.write(w)

    
#createSo2KuDic()
