#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import collections
#import outputprogram 
import os
import subprocess
#import popen

fileNameIntent = "intent.conf"
fileNameMappings = "mappings.conf"
outputFile = "outputprogram.py"
templateFile = "automation_template.txt"
automationline = ''
mappings = collections.defaultdict(list)
intents = [] 

def digestIntents (): 
    with open(fileNameIntent, 'r') as fIntent:
        for intentline in fIntent.readlines():
            intentline.rstrip()
            global intents
            intents.append(intentline)
            #print intentline
    return 0 


def digestMappings (): 
    with open(fileNameMappings,'r') as fMapping:
        for mappingline in fMapping.readlines():
            mappingline.rstrip()
            mapKeyValue = mappingline.split("=",1)
            key = mapKeyValue[0].lstrip()
            key = mapKeyValue[0].rstrip()
            value = mapKeyValue[1].lstrip()
            value = mapKeyValue[1].rstrip()
            mappings[key].append(value)
            #print key,  mappings[key]
            #print mappingline 
    return 0



if __name__== "__main__":

    intentsRet = digestIntents()
    if (intentsRet != 0):
        print ("Error reading Intents file\n")
        
    mappingsRet = digestMappings()
    if (mappingsRet != 0):
        print ("Error reading Intents file\n")

    # Opening the ouputfile to write the code
    fOutput = open (outputFile, "w")
    print "# Creating outputprogram.py file for generating the code\n"

    # Take the template and use it.
    with open(templateFile, "r") as fTemplate:
        for templateline in fTemplate.readlines():
            fOutput.write(templateline)
            if re.search("def testUntitled", templateline, re.IGNORECASE):
                #print intents
                print "# Intents are :"
                for intentline_t in intents:
                    print intentline_t
                    intentWordArray = []
                    intentWordArray = intentline_t.split("->")
                    for wordIntent in intentWordArray:
                        wordIntent = wordIntent.rstrip()
                        wordIntent = wordIntent.lstrip()
                        print wordIntent
                        if wordIntent in mappings:
                            #print "Yes for the intent the key in dict exists\n"
                            automationline = str(mappings[wordIntent])
                            automationline = automationline.lstrip('[\' "')
                            automationline = automationline.rstrip('\"\']')
                            fOutput.write("\t\t")
                            fOutput.write(automationline)
                            fOutput.write("\n")
            
    #p = subprocess.Popen(["python", "outputprogram.py"], stdout=subprocess.PIPE)
    subprocess.Popen(["python", "outputprogram.py"])
