#!/usr/bin/python
import re

fileNameIntent = "intent.conf"
fileNameMappings = "mappings.conf"
outputFile = "outputprogram.py"
templateFile = "automation_template.txt"
automationline = ''
mappings = {}
intents = {}

def digestIntents (): 
    with open(fileNameIntent, 'r') as fIntent:
        intents = fIntent.readlines()
#        print intents
    return 0 


def digestMappings (): 
    with open(fileNameMappings,'r') as fMapping:
        mappings = fMapping.readlines()
#        print mappings
    return 0



if __name__== "__main__":

    intentsRet = digestIntents()
    if (intentsRet != 0):
        print ("Error reading Intents file\n")
        
    mappingsRet = digestMappings()
    if (mappingsRet != 0):
        print ("Error reading Intents file\n")

    fOutput = open (outputFile, "w")
        #for outputline in fOutput.readlines():
    print "Writing to the OutputFile"


    with open(templateFile, "r") as fTemplate:
        for templateline in fTemplate.readlines():
            fOutput.write(templateline)
            #if "def TestUntitled (self):" in templateline:
                #for line in
            if re.search("def testUntitled", templateline, re.IGNORECASE):
                print "Coming inside poo"
                fOutput.write("\t\t")
                automationline = "print (\"Testing \")\n"
                fOutput.write(automationline)
