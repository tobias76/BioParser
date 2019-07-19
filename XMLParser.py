'''@author: Toby Stephen'''


import xml.etree.ElementTree
import os
import sys
import glob

class XMLParser():
    #root = xml.etree.ElementTree.parse('C:/Users/computing/Desktop/MastersProject/Corpus/ArticleData/pubmed_result3.xml').getroot()
    #root = xml.etree.ElementTree.parse('C:/Users/computing/Desktop/MastersProject/Corpus/ArticleData/B-Term Abstracts/Fibrosis.xml').getroot()
    #absPath = "E:\Abstracts"
    
    

    def readXML():
        tag = "eng"
        languageTag = ""
        titleText = ""
        fileName = ""
        
        number = 0
    
        corporaDir = r"C:\Users\computing\Desktop\UpToDateAbstracts\XML\*.xml"
        
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        absPath = os.path.join(desktop, "VasospasmCorpus")
    
        if not os.path.exists(absPath):
            os.mkdir(absPath)
        
        for file in glob.glob(corporaDir):
            root = xml.etree.ElementTree.parse(file).getroot()
        
            for child in root:    
               for childRoot in child:
                   if(childRoot.tag == 'MedlineCitation'):
                       for childChild in childRoot:
                           if (childChild.tag == "PMID"):
                               PMID = childChild.text
                           if(childChild.tag == 'Article'):
                               for secondYoungestChild in childRoot:
                                   if(secondYoungestChild.tag == 'Article'):
                                       for youngestChild in secondYoungestChild:
                                          if(youngestChild.tag == 'Language'):
                                              languageTag = youngestChild.text
                                          if(youngestChild.tag == 'ArticleTitle'):
                                              titleText = youngestChild.text
                                          if(youngestChild.tag == 'Abstract'):
                                               for baby in youngestChild:
                                                   if(baby.tag == 'AbstractText'):
                                                       if(languageTag == tag):
                                                           number += 1
                                                         
                                                           fileName = languageTag + "-" + str(PMID) + ".txt"
                            
                                                           if not os.path.isfile(absPath + "\\" + fileName):
                                                               with open(absPath + "\\" + fileName, "w+") as file:
                                                                   if baby.text is not None:
                                                                       if titleText is not None:
                                                                           file.write(str(titleText.encode("utf-8")) + "\n")
                                                                           file.write(str(baby.text.encode(sys.stdout.encoding, errors='replace')))
                                                                           file.close()
            return absPath
                                           
                                   
if __name__ == '__main__':
    XMLParser.readXML()