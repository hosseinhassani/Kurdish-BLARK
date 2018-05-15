# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 16 Jan 2015
# Last update @: 10 May 2016

# Kurdish Stemmer currently is a rule-based stemmer, which works for
# kurmanji/Sorani dialects (currently works on Latin script only).
# The prorma receives a vocubulary aray and returuns a word stem (root) for each
# item in the vocabulary list.
# The rules for stemming have been taken of the following resources:

# Stemming for Kurdish Information Retrieval:
# Shahin Salavati, Kyumars Sheykh Esmaili, and Fardin Akhlaghian

# http://www.linguist.univ-paris-diderot.fr/~gwalther/Geraldine_Walther/Publications_files/icil11sorani_slides.pdf

# http://public.wsu.edu/~gordonl/S05/256/word_formation.pdf

# Derivational Morphemes in English with Reference to Dialects in Kurdish
# http://www.iasj.net/iasj?func=fulltext&aId=60470

# When endoclitics account for structure in morphology: a Sorani Kurdish case study
# http://www.diplist.it/mmm8/abstract/Walther.pdf

# http://kurdishdna.blogspot.com/2012/04/kurdish-verbs.html

# Kurmanji Kurdish Lexicography: a Survey and Discussion
#http://www.kurdishacademy.org/?q=fa/node/142

# Stemming Algorithms - A Case Study for Detailed Evaluation
# http://nicotournetesis.googlecode.com/svn/trunk/docs/papers/Stemming%20Algorithms.pdf


import os
import unicodedata
import codecs
#    import re

# This section must be revised based on a stemmer algorithm for Kurdish.
# For example, Porter algorithm for English has several steps to remove
# different suffixes. Similar approach must be taken for Kurdish, with
# taking particularities of Kurmanji and Sorani dialects into consideration.

# Issues:
# 1. affix not just suffix (prefix and postfix)
# 2. endoclitics (article: "Fitting into morphological structure:
#                           accounting for Sorani Kurdish endoclitics"

# watch out: beguman -> begu ????


#####################################################################################

suffix = {
    'birdin'.decode('utf-8'),
    'birina'.decode('utf-8'),
    'girtin'.decode('utf-8'),
    'yekanî'.decode('utf-8'),
    'girin'.decode('utf-8'),
    'ayetî'.decode('utf-8'),
    'birin'.decode('utf-8'),
    'dikin'.decode('utf-8'),
    'dekat'.decode('utf-8'),
    'deken'.decode('utf-8'),
    'yekan'.decode('utf-8'),
    'krdnî'.decode('utf-8'),
    'kird'.decode('utf-8'),
    'krdn'.decode('utf-8'),
    'dike'.decode('utf-8'),
    'ekan'.decode('utf-8'),
    'kiri'.decode('utf-8'),
    'kraw'.decode('utf-8'),
    'stan'.decode('utf-8'),
    'mana'.decode('utf-8'),
    'xane'.decode('utf-8'),
    'yekî'.decode('utf-8'),
    'bún'.decode('utf-8'),
    'êkî'.decode('utf-8'),
    'kir'.decode('utf-8'),
    'man'.decode('utf-8'),
    'yan'.decode('utf-8'),
    'yek'.decode('utf-8'),
    'eyş'.decode('utf-8'),
    'im'.decode('utf-8'),
    'eş'.decode('utf-8'),
    'îş'.decode('utf-8'),
    'm'.decode('utf-8'),
    'a'.decode('utf-8'),
    'ê'.decode('utf-8'),
  }

#####################################################################################

def strip_suffix_from_a_list(vocabulary, suffix):
    s = []

    for v in vocabulary:
        sv = v.strip()
        for ts in suffix:
            nosuffix = True
#                if (uv.endswith(ts.decode('utf-8'))):
            if (sv.endswith(ts)):
                nosuffix = False
                if ((len(sv) - len(ts)) >= 2): # suffix strip shoud yeild a stem
                                              # with less than 2 letter.
                    l = len(ts)
                    s.append(sv[:-l])
                else:               
                    nosuffix = True
                vocabulary.pop(vocabulary.index(v)) # reomve the processed word
                break
            else:
                nosuffix = True

        if (nosuffix == True):
            s.append(sv)

    s.sort()

    return s

#####################################################################################

def strip_suffix(word):

    s=' '
    sv = word.strip()
    for ts in suffix:
        nosuffix = True
#                if (uv.endswith(ts.decode('utf-8'))):
        if (sv.endswith(ts)):
            nosuffix = False
            if ((len(sv) - len(ts)) >= 2): # suffix strip shoud yeild a stem
                                          # with less than 2 letter.
                l = len(ts)
                s = sv[:-l]
            break

    return s

#####################################################################################
