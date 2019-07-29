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

class newXMLParser():
    
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    absPath = os.path.join(desktop, "PVDCorpus19601986")  
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
            
            titleAbsPairing = outerDict[PMID]
            
            title = titleAbsPairing[0] + "\n"
            abstract = titleAbsPairing[1]
            
            fileName = str(currentPMID) + ".txt"
            
            if abstract != "No Abstract Found":
                if title != "No Title Found":
                    with open(newXMLParser.absPath + "\\" + fileName, "w+") as file:
                        file.write(str(title.encode(sys.stdout.encoding, errors='replace')))
                        file.write(str(abstract.encode(sys.stdout.encoding, errors='replace')))
                        file.close()
                        newXMLParser.i += 1
                         
if __name__ == '__main__':
    outerDict = newXMLParser.readXML()
    newXMLParser.saveAbs()