# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:00:06 2016

@author: akhoufi
"""

import xml.etree.cElementTree as ET

filename='tunis_tunisia.osm'

#find what 'k' tags exists on the map
#k_set=set([])
#for _,element in ET.iterparse(filename):
#    if element.tag=='tag':
#        for tag in element.iter('tag'):
#            if tag.attrib['k'] not in k_set:
#                k_set.add(tag.attrib['k'])
#                print  tag.attrib['k']      

#check if all the way tag name are in the same language
for _,element in ET.iterparse(filename):
    if element.tag=='tag':
        for tag in element.iter('tag'):
            if tag.attrib['k']=='name':
                print tag.attrib['v']
                
#check phone numbers and fax numbers different formats
#for _,element in ET.iterparse(filename):
#    if element.tag=='tag':
#        for tag in element.iter('tag'):
#            if 'phone' in tag.attrib['k'] or 'fax' in tag.attrib['k'] or 'tel' in tag.attrib['k']:
#                print tag.attrib['v']
#                
##check emails different formats
#for _,element in ET.iterparse(filename):
#    if element.tag=='tag':
#        for tag in element.iter('tag'):
#            if 'email' in tag.attrib['k']:
#                print tag.attrib['v']