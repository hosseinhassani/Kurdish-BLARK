# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 06 Mar 2016
# Last update @: 06 Mar 2016

## Levenishtein distance 

############################################################
# levenshtein has been taken from https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance

def levenshtein(source, target):
    import numpy as np
    
    if len(source) < len(target):
        return levenshtein(target, source)

    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)

    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]    

###################################################

def LevenshteinDistance4Ku2SoDic(dicFile, output):
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    outputlist = []
    
    currentVocabList = getVocabList.getKurmanjiDic(dicFile)
    
    # Format current dic to be ready for merging with the new vocabs
    outfile = codecs.open(output, 'w', encoding = 'utf-8')

    for node in currentVocabList:
        itemNo, Kurmanji, Sorani = node.split()
        outputlist.append(u'{: <6}{: <32}\t{: <4}'.format(levenshtein(Kurmanji, Sorani), Kurmanji, Sorani))
        
           
    outputlist.sort()


    i = 0
    for item in outputlist:
        i = i + 1
        w = u'{: <6}\t{: <32}\n'.format(i, item)
        outfile.write(w)

    outfile.close()

##################################################


##################################################
def LevenshteinDistance4So2KuDic(dicFile, output):
    import os
    import unicodedata
    import codecs
    import re

    import getVocabList

    outputlist = []
    
    currentVocabList = getVocabList.getSoraniDic(dicFile)
    
    # Format current dic to be ready for merging with the new vocabs
    outfile = codecs.open(output, 'w', encoding = 'utf-8')

    for node in currentVocabList:
        itemNo, Sorani, Kurmanji = node.split()
        outputlist.append(u'{: <6}{: <32}\t{: <4}'.format(levenshtein(Sorani, Kurmanji), Sorani, Kurmanji))
        
           
    outputlist.sort()


    i = 0
    for item in outputlist:
        i = i + 1
        w = u'{: <6}\t{: <32}\n'.format(i, item)
        outfile.write(w)

    outfile.close()
    
##################################################
