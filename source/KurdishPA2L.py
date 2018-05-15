# -*- coding: utf-8 -*-

# Hossein Hassani
# Started @: 24 Dec 2014
# Last update @: 23 Apr 2016

# Kurdish Persian/Arabic to Latin transliterator
# This program reads a text (assuming it has been written in Kudish using
# Persian/Arabic script) and converts it to its LTR equivalent in Latin script.

##  ئ ا ب   چ   د   ە ئ ێ  ف   گ     ى     ج  ژ  ک  ل  ڵ  م  ن  ۆ  پ
##  ق  ر ڕ  س   ش   ت  و   ڤ   خ    ز  ح   ع  غ

##  a   b   ç   d   e   ê  f   g  h  i  î  c  j   k  l    m  n  o  p
##  q   r   s   ş   t  u û v w x  y z  h   e  x
## 
##  ئا   ـا   ا ب   ـبـ   ـب   بـ چ   ـچ   ـچـ   چـ د   ــد ە   ـه   ئە
##  ێ   ـێ   ـێـ   ێـ   ئێـ  ف   ـف   ـفـ   فـ گ   ـگ   ـگـ   گــ
##  هـ   ـهـ ى   ئى   ـيـ   يـ ج   ـج   ـجـ   جـ  ژ   ـژ
##  ک   ـک   ـکـ   کــ ل   ـل   ـلـ   لــ ڵ   ـڵ   ـڵـ   ڵــ م   ـم   ـمـ   مــ
##  ن   ـن   ـنـ   نــ ۆ   ـۆ   ئۆ پ   ـپ   ـپـ   پــ ق   ـق   ـقـ   قــ ر   ـر
##  ڕ   ـڕ س   ـس   ـسـ   ســ ش   ـش   ـشـ   شــ ت   ـت   ـتـ   تــ و   ـو   ئو
##  وو   ـوو ڤ   ـڤ   ـڤـ   ڤـ و   ـو خ   ـخ   ـخـ   خـ ى   ئى   ـيـ   يـ ز   ـز
##  ح   ـح   ـحـ   حـ ع   ـع   ـعـ   عـ غ   ـغ   ـغـ   غـ

##  A a  B   b Ç   ç D d E e Ê   ê F   f G   g H   h I   i Î   î C   c J   j K   k
##  L   l M   m N   n O   o P   p Q   q R   r S   s Ş   ş T   t U   u Û   û V   v
##  W   w X   x Y   y Z   z H  h E  e X  x


def KurdishPA2L(inputFile, outputFile):

    import os
    import codecs
    import nltk



    def replace_all(text, trigramDic, bigramDic, digramDic):
        for i, j in trigramDic.iteritems():
            text = text.replace(i, j.decode('utf-8'))

        for i, j in bigramDic.iteritems():
            text = text.replace(i, j.decode('utf-8'))


        for i, j in digramDic.iteritems():
            text = text.replace(i, j.decode('utf-8'))

        return text

    # -------------------------------------
    # The order of process is important!
    # -------------------------------------

#######################

##  Attention: "furtive i" issue                                 ##
##  If two consecutive consonants such as p and ş appears in     ##
##  a token, an i should be inserted between the two.            ##

##\cite{mccarus1958kurdish} talking about consecutive cluster and \enquote{furtive i}

##\cite{mccarus1960kurdish} ????? check the related content ?????

##\cite{thackston2006kurmanji} \enquote{Kurdish writers are not in agreement on the writing of the furtive i, and many omit it, particularly when it is unstressed,
##i.e. some write ez fêhim dikim ‘I understand’ while others write ez fêhm dikim.}
    
#######################

    digramDic = {
            '١'.decode('utf-8'): '1',
            '٢'.decode('utf-8'): '2',
            '٣'.decode('utf-8'): '3',
            '٤'.decode('utf-8'): '4',
            '٥'.decode('utf-8'): '5',
            '٦'.decode('utf-8'): '6',
            '٧'.decode('utf-8'): '7',
            '٨'.decode('utf-8'): '8',
            '٩'.decode('utf-8'): '9',
            '٠'.decode('utf-8'): '0',
            '1'.decode('utf-8'): '1',
            '2'.decode('utf-8'): '2',
            '3'.decode('utf-8'): '3',
            '4'.decode('utf-8'): '4',
            '5'.decode('utf-8'): '5',
            '6'.decode('utf-8'): '6',
            '7'.decode('utf-8'): '7',
            '8'.decode('utf-8'): '8',
            '9'.decode('utf-8'): '9',
            '0'.decode('utf-8'): '0',
            '['.decode('utf-8'): '[',
            ']'.decode('utf-8'): ']',
            '/'.decode('utf-8'): '/',
            ':'.decode('utf-8'): ':',
            '"'.decode('utf-8'): '"',
            '.'.decode('utf-8'): '.',
            ' '.decode('utf-8'): ' ',
            '،'.decode('utf-8'): ',',
    #        '‌'.decode('utf-8'): '',
    #        ' '.decode('utf-8'): ' ',
            'ئ'.decode('utf-8'): 'e',
            'ه'.decode('utf-8'): 'e',
            'ە'.decode('utf-8'): 'e',
            'ا'.decode('utf-8'): 'a',
            'ێ'.decode('utf-8'): 'ê',
            'ب'.decode('utf-8'): 'b',
            'پ'.decode('utf-8'): 'p',
            'ت'.decode('utf-8'): 't',   # ث 11/4/2016 and ة ء ؤ
            'ج'.decode('utf-8'): 'c',
            'چ'.decode('utf-8'): 'ç',
            'ح'.decode('utf-8'): 'h',
            'خ'.decode('utf-8'): 'x',
            'د'.decode('utf-8'): 'd',
            'ذ'.decode('utf-8'): 'z',
            'ر'.decode('utf-8'): 'r',   # the case of ذ 11/4/2016
            'ڕ'.decode('utf-8'): 'r',
            'ز'.decode('utf-8'): 'z',
            'ژ'.decode('utf-8'): 'j',
            'س'.decode('utf-8'): 's',
            'ش'.decode('utf-8'): 'ş',
            'ع'.decode('utf-8'): 'e',
            'غ'.decode('utf-8'): 'x',
            'ف'.decode('utf-8'): 'f',
            'ق'.decode('utf-8'): 'q',
            'ک'.decode('utf-8'): 'k',
            'ك'.decode('utf-8'): 'k',
            'گ'.decode('utf-8'): 'g',
            'ل'.decode('utf-8'): 'l',
            'ڵ'.decode('utf-8'): 'l',
            'م'.decode('utf-8'): 'm',
            'ن'.decode('utf-8'): 'n',
            'ۆ'.decode('utf-8'): 'o',
            'ه'.decode('utf-8'): 'h',
            'ھ'.decode('utf-8'): 'h',    # Added on 11/04/2016 found from recent data
            'ي'.decode('utf-8'): 'i',    # a case of أ also should be looked into.   
            'ی'.decode('utf-8'): 'î',
            'و'.decode('utf-8'): 'u',
            'ڤ'.decode('utf-8'): 'v',
            'و'.decode('utf-8'): 'û',
            'و'.decode('utf-8'): 'w',
            'ى'.decode('utf-8'): 'y',
            }

    bigramDic = {
            'ئا'.decode('utf-8'): 'a',
            'ئە'.decode('utf-8'): 'e',
            'ئه‌'.decode('utf-8'): 'e',
            'ـە'.decode('utf-8'): 'e',
            'ئا'.decode('utf-8'): 'a',
            'ئە'.decode('utf-8'): 'e',
            'ئێ'.decode('utf-8'): 'ê',
            'ـێ'.decode('utf-8'): 'ê',
            'ێـ'.decode('utf-8'): 'ê',
            'ەب'.decode('utf-8'): 'eb',
            'ـب'.decode('utf-8'): 'b',
            'بـ'.decode('utf-8'): 'b',
            'بک'.decode('utf-8'): 'bk',
            'با'.decode('utf-8'): 'ba',
            'به'.decode('utf-8'): 'be',
            'بۆ'.decode('utf-8'): ' bû',
            'بی'.decode('utf-8'): 'bi',
            'ـپ'.decode('utf-8'): 'p',
            'په'.decode('utf-8'): 'pe',
            'ـت'.decode('utf-8'): 't',
            'تە'.decode('utf-8'): 'te',
            'تو'.decode('utf-8'): 'tu',    # Added on 11/04/2016 found from recent data
            'ـج'.decode('utf-8'): 'c',
            'جـ'.decode('utf-8'): 'c',
            'ـچ'.decode('utf-8'): 'ç',
            'چـ'.decode('utf-8'): 'ç',
            'ـح'.decode('utf-8'): 'h',
            'حـ'.decode('utf-8'): 'h',
            'ـخ'.decode('utf-8'): 'x',
            'خـ'.decode('utf-8'): 'x',
            'ده'.decode('utf-8'): 'de',
            'دی'.decode('utf-8'): 'di',
            'ـر'.decode('utf-8'): 'r',
            'ره'.decode('utf-8'): 're',
            'ـڕ'.decode('utf-8'): 'r',
            'ـز'.decode('utf-8'): 'z',
            'زو'.decode('utf-8'): 'zu',    # Added on 11/04/2016 found from recent data
            'ـژ'.decode('utf-8'): 'j',
            'ـس'.decode('utf-8'): 's',
            'ســ'.decode('utf-8'): 's',
            'سو'.decode('utf-8'): 'su',
            'سه'.decode('utf-8'): 'se',
            'سە'.decode('utf-8'): 'se',
            'شه'.decode('utf-8'): 'şe',
            'ـش'.decode('utf-8'): 'ş',
            'شــ'.decode('utf-8'): 'ş',
            'عا'.decode('utf-8'): 'a',
            'ـع'.decode('utf-8'): 'e',
            'ـع'.decode('utf-8'): 'e',
            'عـ'.decode('utf-8'): 'e',
            'عی'.decode('utf-8'): 'e',
            'عێ'.decode('utf-8'): 'e',
            'ـغ'.decode('utf-8'): 'x',
            'غـ'.decode('utf-8'): 'x',
            'ـف'.decode('utf-8'): 'f',
            'فـ'.decode('utf-8'): 'f',
            'ـق'.decode('utf-8'): 'q',
            'قم'.decode('utf-8'): 'qim',     # Added on 11/04/2016 found from recent data
            'قو'.decode('utf-8'): 'qu',
            'قه'.decode('utf-8'): 'qe',
            'ـک'.decode('utf-8'): 'k',
            'کب'.decode('utf-8'): 'kb',
            'كه'.decode('utf-8'): 'ke',
            'کو'.decode('utf-8'): 'ku',
            'كو'.decode('utf-8'): 'ku',     # Added on 11/04/2016 found from recent data
            'ـگ'.decode('utf-8'): 'g',
            'گو'.decode('utf-8'): 'gu',     # Added on 11/04/2016 found from recent data
            'ـل'.decode('utf-8'): 'l',
            'ڵه'.decode('utf-8'): 'le',
            'له'.decode('utf-8'): 'le',
            'ـم'.decode('utf-8'): 'm',
            'مو'.decode('utf-8'): 'mu',  # Added on 22/04/2016 found from recent data
            'مە'.decode('utf-8'): 'me',
            'ـن'.decode('utf-8'): 'n',
            'نز'.decode('utf-8'): 'niz', # Added on 22/04/2016 found from recent 
            'نه'.decode('utf-8'): 'ne',
            'نن'.decode('utf-8'): 'nin', # Added on 22/04/2016 found from recent
            'من'.decode('utf-8'): 'min', # Added on 22/04/2016 found from recent
            'ـۆ'.decode('utf-8'): 'o',
            'ئۆ'.decode('utf-8'): 'o',
            'اە'.decode('utf-8'): 'ah',
            'يـ'.decode('utf-8'): 'î',
            'یی'.decode('utf-8'): 'iy',
            'وو'.decode('utf-8'): 'û',
            'ـو'.decode('utf-8'): 'u',
            'ـڤ'.decode('utf-8'): 'v',
            'ڤـ'.decode('utf-8'): 'v',
            'فـ'.decode('utf-8'): 'f',
            'ـق'.decode('utf-8'): 'q',
            'ـو'.decode('utf-8'): 'w',
            'ها'.decode('utf-8'): 'ha',
            'هۆ'.decode('utf-8'): 'ho',
            'هه'.decode('utf-8'): 'he',
            'هە'.decode('utf-8'): 'he',
            'هێ'.decode('utf-8'): 'hê',
            'هێ'.decode('utf-8'): 'he',
            'ئى'.decode('utf-8'): 'y',
            'يـ'.decode('utf-8'): 'y',
            'یه'.decode('utf-8'): 'ye',
            'یە'.decode('utf-8'): 'ye',
            'یا'.decode('utf-8'): 'ya',
            'یو'.decode('utf-8'): 'yu',
            }

    trigramDic = {
            'ئه‌'.decode('utf-8'): ' e',
            ' ئە'.decode('utf-8'): ' e', 
            ' ئو'.decode('utf-8'): ' o',
            'ـهـ'.decode('utf-8'): 'e',
            'ه‌ن'.decode('utf-8'): 'en',
            'ـێـ'.decode('utf-8'): 'ê',
            'ـبـ'.decode('utf-8'): 'b',
            'ـپـ'.decode('utf-8'): 'p',
            'پــ'.decode('utf-8'): 'p',
            'په'.decode('utf-8'): 'pe',
            'ـت'.decode('utf-8'): 't',
            'ـتـ'.decode('utf-8'): 't',
            'تــ'.decode('utf-8'): 't',
            'ته‌'.decode('utf-8'): 'te',
            'ـجـ'.decode('utf-8'): 'c',
            'جه‌'.decode('utf-8'): 'ce',
            'ـچـ'.decode('utf-8'): 'ç',
            'ـحـ'.decode('utf-8'): 'h',
            'حـ'.decode('utf-8'): 'h',
            'ـخـ'.decode('utf-8'): 'x',
            'ده‌'.decode('utf-8'): 'de',
            'ده‌'.decode('utf-8'): 'de',
            'ده‌'.decode('utf-8'): 'de',
            'ژه‌'.decode('utf-8'): 'je',
            'ـسـ'.decode('utf-8'): 's',
            'ســ'.decode('utf-8'): 's',
            'ـشـ'.decode('utf-8'): 'ş',
            'شــ'.decode('utf-8'): 'ş',
            'ـفـ'.decode('utf-8'): 'f',
            'ـقـ'.decode('utf-8'): 'q',
            'قــ'.decode('utf-8'): 'q',
            'قــ'.decode('utf-8'): 'q',
            'قوو'.decode('utf-8'): 'qû',  # Added on 22/04/2016 found from recent data
            'کــ'.decode('utf-8'): 'k',
            'ـکـ'.decode('utf-8'): 'k',
            'کــ'.decode('utf-8'): 'k',
            'ـگـ'.decode('utf-8'): 'g',
            'گــ'.decode('utf-8'): 'g',
            'گــ'.decode('utf-8'): 'g',
            'ـلـ'.decode('utf-8'): 'l',
            'لــ'.decode('utf-8'): 'l',
            'لــ'.decode('utf-8'): 'l',
            'مــ'.decode('utf-8'): 'm',
            'نــ'.decode('utf-8'): 'n',
            'ـمـ'.decode('utf-8'): 'm',
            'مــ'.decode('utf-8'): 'm',
            'مه‌'.decode('utf-8'): 'me',
            'ـنـ'.decode('utf-8'): 'n',
            'نــ'.decode('utf-8'): 'n',
            ' ئی'.decode('utf-8'): ' î',
            'ـيـ'.decode('utf-8'): 'î',
            'وه‌'.decode('utf-8'): 'we',
            '‌وه'.decode('utf-8'): 'we',
            ' و '.decode('utf-8'): ' u ',
            ' ئو'.decode('utf-8'): ' o',
            'ـوو'.decode('utf-8'): ' û ',
            'ـڤـ'.decode('utf-8'): 'v',
            ' هۆ'.decode('utf-8'): ' ho',
            'ـيـ'.decode('utf-8'): 'y',
            'يـ'.decode('utf-8'): 'y',
            'ێیە'.decode('utf-8'): 'êye',
            ' یو'.decode('utf-8'): ' yo',
            }


#    os.chdir("/home/hossein/w4u")
#    f = codecs.open('t1.txt', encoding='utf-8')
    f = codecs.open(inputFile, encoding='utf-8')
    originalText = f.read()
#    print originalText
    f.close()


    convertedText = replace_all(originalText, trigramDic, bigramDic, digramDic)
     
#    print convertedText

#    o = codecs.open('LSorani5.txt', 'w', encoding='utf-8')
    o = codecs.open(outputFile, 'w', encoding='utf-8')
    o.write(convertedText);
    o.close()
















