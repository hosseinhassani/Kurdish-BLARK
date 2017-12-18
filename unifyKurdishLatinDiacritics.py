# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 09 Feb 2016
# Last update @: 11 Feb 2016

# This utility unifies the diacritics of a Kurdish text in latin.
# For example í will be changed to î

def UnifyKurdishLatinDiacritics(inputFile):

    import os
    import codecs
    

    def replace_all(text, diacriticsDic):
        for i, j in diacriticsDic.iteritems():
            text = text.replace(i, j.decode('utf-8'))

        return text

    # -------------------------------------
    # The order of process is important!
    # -------------------------------------

    diacriticsDic = {
            'é'.decode('utf-8'): 'ê',
            'É'.decode('utf-8'): 'Ê',
            'í'.decode('utf-8'): 'î',
            'Í'.decode('utf-8'): 'Î',
            'ú'.decode('utf-8'): 'û',
                    }

    f = codecs.open(inputFile, encoding='utf-8')
    originalText = f.read()
#    print originalText
    f.close()


    convertedText = replace_all(originalText, diacriticsDic)
     
#    print convertedText

    o = codecs.open(inputFile, 'w', encoding='utf-8')
    o.write(convertedText);
    o.close()

