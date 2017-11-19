# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:38:35 2017

@author: Christine
"""

import xml.etree.ElementTree as ET

# input file
tree = ET.parse("C:\\Users\\chris\\Desktop\\NBSUpload\\1234567.p9.txt")
root = tree.getroot()

    # Loop for find children under fixed_annotation
d = {}
    
for child in root.find('Wells'):
    for well in child.iter():
        print(well.tag, well.attrib)
    
        # Find genomic sequence child
  #      genomic = child.find('sequence').text
  #  return genomic

   #   <Index>0</Index>
    #  <SampleBarcode>170872101</SampleBarcode>