import xml.etree.ElementTree
import os
import sys

root = xml.etree.ElementTree.parse('C:/Users/computing/Desktop/MastersProject/Corpus/ArticleData/pubmed_result3.xml').getroot()

number = 0


absPath = os.path.join(str(os.getcwd()), "Abstracts")

print(absPath)
if not os.path.exists(absPath):
    os.mkdir(absPath)
    
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
                                   if(youngestChild.tag == 'Abstract'):
                                       for baby in youngestChild:
                                           if(baby.tag == 'AbstractText'):
                                               number += 1
                                               
                                               fileName = str(PMID) + ".txt"
                                               
                                               with open(absPath + "\\" + fileName, "x") as file:
                                                   file.write(str(baby.text.encode(sys.stdout.encoding, errors='replace')))
                                                   file.close()
                                               
                                       