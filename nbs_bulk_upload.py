# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:38:35 2017

@author: Christine
"""

import xml.etree.ElementTree as ET

# input file
tree = ET.parse("C:\\Users\\chris\\Desktop\\NBSUpload\\1234567.p9.txt")
root = tree.getroot()


#get well info for each well and put into dict with index as the key and the values in another dict
def get_well_info(root):
    """
    method to get well info for each well and put into dict with index as the key and the values in another dict
    Input: root of element tree
    Return: Dictionary of dictionaries containing well information, with the index and the primary key
    """
    # create dictionary 
    d = {}
    for child in root.findall('Wells'):
       for well in child.iter('Well'):
           d1 = {}
           d1['SampleBarcode'] = well.find('SampleBarcode').text
           d1['IsBad'] = well.find('IsBad').text
           d1['RequestedDisksPerWell'] = well.find('RequestedDisksPerWell').text
           d1['PunchedDisksPerWell'] = well.find('PunchedDisksPerWell').text
           d[well.find('Index').text] = d1
    return(d)
            
test = get_well_info(root)
print(test['0']['SampleBarcode'])

