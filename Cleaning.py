# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:33:47 2016

@author: akhou
"""
import xml.etree.cElementTree as ET
import re


street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
mapping = { "Imp2": "Impasse",
            "R.": "Rue",
            "Av":"Avenue",
            "Imp.":"Impasse"
            }    
    
def clean_street_name(name):
    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        if street_type in mapping:
            name=name.replace(street_type,mapping[street_type])
    return name

def clean_phone_number(phone_number):
    phone_number_type=re.compile(r'[^\d\+]')
    return phone_number_type.sub('',phone_number)
    
def clean_phone_numbers(phone_numbers):
    phone_number_list=phone_numbers.split('/')
    for i in range(len(phone_number_list)):
        phone_number_list[i]=clean_phone_number(phone_number_list[i])
    return phone_number_list
        
            
def clean():
#    filename='tunis_tunisia.osm'
#    osm_file = open(filename, "r")
#    for event, elem in ET.iterparse(osm_file, events=("start",)):
#        if elem.tag == "node" or elem.tag == "way":
#            for tag in elem.iter("tag"):
#                if tag.attrib['k'] == "addr:street":
#                    print tag.attrib['v'],' => ', clean_street_name(tag.attrib['v'])
   print clean_phone_numbers('+216-71.200 300 / 22883387')                
clean()