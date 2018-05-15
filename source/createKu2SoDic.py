# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 13 Mar 2015
# Last update @: 23 Feb 2016

## createKu2SoDic preprocesses the created vocabulary
## in order to find the Kuramnji words whose weighting are zero alongside
## common vocabulary among the two dialects: Kuramnji and Sorani.

###################################################
def updateKu2SoDic(dicFile, newVocabList):
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    updatedVocabList = []
    seen = set()
    
    currentVocabList = getVocabList.getKurmanjiDic(dicFile)
    
    # Format current dic to be ready for merging with the new vocabs
    for node in currentVocabList:
        itemNo, Kurmanji, Sorani = node.split()
        updatedVocabList.append(u'{: <25}\t{: <4}'.format(Kurmanji, Sorani))
        seen.add(Kurmanji.lower())
        
    # Merge the new vocabs with the existing dictionary
    for node in newVocabList:
        Kurmanji, Sorani = node.split()
        if Kurmanji.lower() not in seen:
            updatedVocabList.append(u'{: <25}\t{: <4}'.format(Kurmanji, Sorani))
           
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
def mergeSo2KuDic(KDic, SDic):
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    updatedVocabList = []
    
    currentVocabList = getVocabList.getKurmanjiDic(KDic)
    So2KuDic = getVocabList.getSoraniDic(SDic)
    
    seen = set() # This set is used to check the duplicates
    # Format current dic to be ready for merging with the new vocabs
    for node in currentVocabList:
        itemNo, Kurmanji, Sorani = node.split()
        seen.add(Kurmanji) # There shouldn't be duplicates in the curretn dic
        updatedVocabList.append(u'{: <25}\t{: <4}'.format(Kurmanji, Sorani))
        
    # Merge the vocabs from the Sorani-to-Kurmanji wich do not exist
    # in the current Kurmanji-to-Sorani dictionary
    for node in So2KuDic:
        itemNo, Sorani, Kurmanji = node.split()
        if Kurmanji not in seen:
            seen.add(Kurmanji)
            updatedVocabList.append(u'{: <25}\t{: <4}'.format(Kurmanji, Sorani))
           

    updatedVocabList.sort()


    try:
        outfile = codecs.open(KDic, 'w', encoding = 'utf-8')

        i = 0
        for item in updatedVocabList:
            i = i + 1
            w = u'{: <6}\t{: <25}\n'.format(i, item)
            outfile.write(w)

        outfile.close()
    except:
        return # Leave with no harm! (Perhaps I shoul put a proper message here.)

##################################################

def createKu2SoDic():
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    os.chdir("/home/hosseinhassani/Hossein/w4u")


    weightingList = getVocabList.getWeightingList()
    
    allVocab = 0
    commonVocab = 0
    KurmanjiVocab = 0
    SoraniVocab = 0
    weight = '100'
 
    KurmanjiSoraniDic = []
    for node in weightingList:
        itemNo, vocab, kurmanjiWeight, soraniWeight = node.split()
#        print(itemNo, kurmanjiWeight, soraniWeight)
        if ((kurmanjiWeight == soraniWeight) or (kurmanjiWeight == weight.encode('utf-8' ))):
            KurmanjiSoraniDic.append(u'{: <25}\t{: <4}'.format(vocab, vocab))

    outfile = codecs.open('KurmanjiSoraniDic', 'w', encoding = 'utf-8')

    i = 0
    for item in KurmanjiSoraniDic:
        i = i + 1
        w = u'{: <6}\t{: <25}\n'.format(i, item)
        outfile.write(w)

    outfile.close()
       
###################################################
#createKu2SoDic()
