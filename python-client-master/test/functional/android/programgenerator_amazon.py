#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import collections
#import outputprogram 
import os
import subprocess
#import popen

fileNameIntent = "intent_amazon.conf"
fileNameMappings = "mappings_amazon.conf"
outputFile = "outputprogram_amazon.py"
templateFile = "automation_template_amazon.txt"
automationline = ''
mappings = collections.defaultdict(list)
intents = [] 

#
# Send Key, Value, Parent
#
def addObjectsToProgram (wordIntent_t,value_t, parent_t):
    #print "Yes for the intent the key in dict exists\n"
#    print "...", wordIntent_t, "..."
    if (parent_t == "credentials"):
        print parent_t, wordIntent_t, value_t
        if (wordIntent_t == "username" or  wordIntent_t == "password"):
            arrayUsername = list(value_t)
            for character_t in arrayUsername:
                charFrameLine = "self.driver.find_element_by_xpath(\"xpath=//*[@text='%s']\").click()" %character_t                
                print charFrameLine
                fOutput.write("\t\t")
                fOutput.write(charFrameLine)
                fOutput.write("\n")
            print "# [Info] The intent is existinglogin"
        #else: 
    elif (wordIntent_t == "authenticate"):
        print "# [Info] The intent is authenticate"
    else: 
        automationline = str(mappings[wordIntent_t])
        automationline = automationline.lstrip('[\' "')
        automationline = automationline.rstrip('\"\']')
        fOutput.write("\t\t")
        fOutput.write(automationline)
        fOutput.write("\n")



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
    print mappings
    # Opening the ouputfile to write the code
    fOutput = open (outputFile, "w")
    print "# Creating outputprogram.py file for generating the code\n"

    # Take the template and use it.
    with open(templateFile, "r") as fTemplate:
        for templateline in fTemplate.readlines():
            fOutput.write(templateline)
            if re.search("def testUntitled", templateline, re.IGNORECASE):
                print "# Overall Intent is:"
                for intentline_t in intents:
                    print intentline_t
                    intentWordArray = []
                    intentWordArray = intentline_t.split("->")
                    for wordIntent in intentWordArray:
                        wordIntent = wordIntent.rstrip()
                        wordIntent = wordIntent.lstrip()
                        propertiesArray = []
                        propertiesArray = wordIntent.split(".",1)
                        print propertiesArray
                        if (len(propertiesArray) == 1):
                            if wordIntent in mappings:
                                #print "Only 1 parameter in the intent %s" %wordIntent
                                addObjectsToProgram (wordIntent,"none","none")
                                #continue 
                        elif (len(propertiesArray) >= 2):
                            #print "More than 2 parameters in the intent" 
                            for id_t, property_t in enumerate(propertiesArray):
                                property_t = property_t.rstrip()
                                property_t = property_t.lstrip()
                                #print id_t, property_t
                                if (id_t == 0):
                                    if property_t in mappings:
                                        addObjectsToProgram (property_t,"none","none")
                                elif (id_t >= 1):
                                    key_values = []
                                    key_values = property_t.split(",")
                                    for key_val_t in key_values:
                                        key_val = []
                                        key_val = key_val_t.split(":")

                                        key_t = key_val[0]
                                        key = key_t.replace("{", "")
                                        key = key.replace("}", "")
                                        if len(key_val) == 2:
                                            value_t = key_val[1]
                                            value = value_t.replace("}", "")
                                            value = value.replace("{", "")
                                            print "\t Key: %s, value: %s Parent: %s" %(key, value, propertiesArray[0])
                                            addObjectsToProgram (key,value,propertiesArray[0])
                                        else:
                                            print "No key exists for the key: %s" %(key) 
                                            key = 0

            
    #subprocess.Popen(["python", "outputprogram_amazon.py"])
