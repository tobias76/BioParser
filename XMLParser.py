# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:14:07 2019

@author: computing
"""

import xml.etree.ElementTree
import os
import glob
import sys

outerDict = {}
entriesRemoved = {}

class newXMLParser():
    
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    absPath = os.path.join(desktop, "HematologyCorpus")  
    i = 0    
    def readXML():

        PMID = ""
        
        corporaDir = r"C:\Users\computing\Desktop\UpToDateAbstracts\XML\*.xml"
        
        if not os.path.exists(newXMLParser.absPath):
            os.mkdir(newXMLParser.absPath)
        
        for file in glob.glob(corporaDir):
            root = xml.etree.ElementTree.parse(file).getroot()
           
            for article in root.findall('.//PubmedArticle//MedlineCitation'):  
                PMID = article.find('.//PMID')
                title = article.find('.//Article//ArticleTitle')
                
                abstract = article.find('.//Article//AbstractText')
                
                if PMID is None:
                    PMIDSaved = "No PMID Found"
                else:
                    PMIDSaved = PMID.text
                    
                if title is None:
                    titleSaved = "No Title Found"
                else:
                    titleSaved = title.text
                    
                if abstract is None:
                    abstractSaved = "No Abstract Found"
                else:
                    abstractSaved = abstract.text
                    
                outerDict[PMIDSaved] = [titleSaved, abstractSaved]
        
        return outerDict                                                       
                
    def saveAbs():
        for PMID, innerDict in outerDict.items():
            currentPMID = PMID
                   
            if innerDict[0] is not None:
                title = innerDict[0] + "\n"
            else:
                title = "No Title Found"
                
            if innerDict[1] is not None:
                abstract = innerDict[1]
            else:
                abstract = "No Abstract Found"
                
            fileName = str(currentPMID) + ".txt"
            
            if abstract == None:
                    entriesRemoved[str(PMID)] = "Removed due to lack of abstract."
            if abstract ==  "No Abstract Found":
                entriesRemoved[str(PMID)] = "Removed due to lack of abstract."

            if title == None:
                if str(PMID) not in entriesRemoved:
                    entriesRemoved[str(PMID)] = "Removed due to lack of title."
            if title ==  "No Title Found":
                entriesRemoved[str(PMID)] = "Removed due to lack of title."
                

            if str(PMID) not in entriesRemoved:
                with open(newXMLParser.absPath + "\\" + fileName, "w+") as file:
                    file.write(str(title.encode(sys.stdout.encoding, errors='replace')))
                    file.write(str(abstract.encode(sys.stdout.encoding, errors='replace')))
                    file.close()
                    newXMLParser.i += 1
              
        print("Removing " + str(len(entriesRemoved)) + " abstracts or " + str(100 * float(len(entriesRemoved) / len(outerDict))) + "%")

if __name__ == '__main__':
    outerDict = newXMLParser.readXML()
    newXMLParser.saveAbs()