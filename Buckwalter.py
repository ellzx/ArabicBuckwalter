#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Author : Zied Elloumi
        python script to convert Arabic chr to Backwalter',
        and Backwalter to Arabic chr',
        I used standart transliteration from : 
        http://www.qamus.org/transliteration.htm '''

import sys 

ar2bw={'\'': u'\u0621','|'  :  u'\u0622','>' :  u'\u0623','&' :  u'\u0624',
       '<' :  u'\u0625','}' :  u'\u0626','A' :  u'\u0627','b' :  u'\u0628',
       'p' :  u'\u0629','t' :  u'\u062A','v' :  u'\u062B','j' :  u'\u062C',
       'H' :  u'\u062D','x' :  u'\u062E','d' :  u'\u062F','*' :  u'\u0630',
       'r' :  u'\u0631','z' :  u'\u0632','s' :  u'\u0633','$' :  u'\u0634',
       'S' :  u'\u0635','D' :  u'\u0636','T' :  u'\u0637','Z' :  u'\u0638',
       'E' :  u'\u0639','g' :  u'\u063A','_' :  u'\u0640','f' :  u'\u0641',
       'q' :  u'\u0642','k' :  u'\u0643','l' :  u'\u0644','m' :  u'\u0645',
       'n' :  u'\u0646','h' :  u'\u0647','w' :  u'\u0648','Y' :  u'\u0649',
       'y' :  u'\u064A','F' :  u'\u064B','N' :  u'\u064C','K' :  u'\u064D',
       'a' :  u'\u064E','u' :  u'\u064F','i' :  u'\u0650','~' :  u'\u0651',
       'o' :  u'\u0652','`' :  u'\u0670','{' :  u'\u0671','P' :  u'\u067E',
       'J' :  u'\u0686','V' :  u'\u06A4','G' :  u'\u06AF',' ' :  ' '}

bw2ar={'\'':  u'\u0621','|' :  u'\u0622','>' :  u'\u0623','&' :  u'\u0624', 
       '<' :  u'\u0625','}' :  u'\u0626','A' :  u'\u0627','b' :  u'\u0628', 
       'p' :  u'\u0629','t' :  u'\u062A','v' :  u'\u062B','j' :  u'\u062C', 
       'H' :  u'\u062D','x' :  u'\u062E','d' :  u'\u062F','*' :  u'\u0630', 
       'r' :  u'\u0631','z' :  u'\u0632','s' :  u'\u0633','$' :  u'\u0634', 
       'S' :  u'\u0635','D' :  u'\u0636','T' :  u'\u0637','Z' : u'\u0638', 
       'E' :  u'\u0639','g' :  u'\u063A','_' :  u'\u0640','f' : u'\u0641', 
       'q' :  u'\u0642','k' :  u'\u0643','l' :  u'\u0644','m' : u'\u0645', 
       'n' :  u'\u0646','h' :  u'\u0647','w' :  u'\u0648','Y' : u'\u0649', 
       'y' :  u'\u064A','F' :  u'\u064B','N' :  u'\u064C','K' : u'\u064D', 
       'a' :  u'\u064E','u' :  u'\u064F','i' :  u'\u0650','~' : u'\u0651', 
       'o' :  u'\u0652','`' :  u'\u0670','{' :  u'\u0671','P' : u'\u067E', 
       'J' :  u'\u0686','V' :  u'\u06A4','G' :  u'\u06AF',' ' : ' '}

def convert (string,dict):
   chrlist=list(string.strip()) 
   for i in range (0,len(chrlist)):
       if chrlist[i] in dict.keys():
            chrlist[i]=dict[chrlist[i]] 
   return "".join(chrlist)

def usage ():
    print ("Usage: \n\tpython3 Buckwalter.py -c ar2bw < input_ar_file > output_bw_file                 \n\techo \"String\" | python3 -c ar2bw ")
for line in sys.stdin:
    if (sys.argv[1] in ["ar2bw","bw2ar"]):
        print (convert(line,ar2bw))
    else:
        usage()
        exit()
