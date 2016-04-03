# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:00:06 2016

@author: akhoufi
"""

import xml.etree.cElementTree as ET


#find what 'k' tags exists on the map
def list_tags(filename):
    tag_set=set()
    for _,element in ET.iterparse(filename):
        if element.tag=='tag':
            for tag in element.iter('tag'):
                if tag.attrib['k'] not in tag_set:
                    tag_set.add(tag.attrib['k'])
                    print  tag.attrib['k']    
    return tag_set

#check if all the way tag name are in the same language
def list_tag_names(filename):
    for _,element in ET.iterparse(filename):
        if element.tag=='tag':
            for tag in element.iter('tag'):
                if tag.attrib['k']=='name':
                    print tag.attrib['v']

                
#check phone numbers and fax numbers different formats
def list_phone_numbers(filename):
    for _,element in ET.iterparse(filename):
        if element.tag=='tag':
            for tag in element.iter('tag'):
                if 'phone' in tag.attrib['k'] or 'fax' in tag.attrib['k'] or 'tel' in tag.attrib['k']:
                    print tag.attrib['v']
                    

               
#check emails different formats
def list_emails(filename):
    for _,element in ET.iterparse(filename):
        if element.tag=='tag':
            for tag in element.iter('tag'):
                if 'email' in tag.attrib['k']:
                    print tag.attrib['v']
                
#check address housenumber for anything different than numbers
def list_housenumbers(filename):
    for _,element in ET.iterparse(filename):
        if element.tag=='tag':
            for tag in element.iter('tag'):
                if 'addr:housenumber' in tag.attrib['k']:
                    print tag.attrib['v']

#Check for postal codes formats
def list_postcodes(filename):
    for _,element in ET.iterparse(filename):
        if element.tag=='tag':
            for tag in element.iter('tag'):
                if 'addr:postcode' in tag.attrib['k']:
                    print tag.attrib['v']
            
#check if number of governorate is right
def count_governorate(filename):
    governorate_set=set([])
    for _,element in ET.iterparse(filename):
        for tag in element.iter('tag'):
            if 'governorate' in tag.attrib['k'] and tag.attrib['v'] not in governorate_set:
                governorate_set.add(tag.attrib['v'])
    return governorate_set              
                
def list_country(filename):
    governorate_set=set([])
    for _,element in ET.iterparse(filename):
        for tag in element.iter('tag'):
            if 'governorate' in tag.attrib['k'] and tag.attrib['v'] not in governorate_set:
                governorate_set.add(tag.attrib['v'])
    return governorate_set  
    
def list_country(filename):
    governorate_set=set([])
    for _,element in ET.iterparse(filename):
        for tag in element.iter('tag'):
            if 'governorate' in tag.attrib['k'] and tag.attrib['v'] not in governorate_set:
                governorate_set.add(tag.attrib['v'])
    return governorate_set
    
def list_street_names(filename):
    street_names_set=set()
    for _,element in ET.iterparse(filename):
        for tag in element.iter('tag'):
            street_name=tag.attrib['v'].split()[0]
            if 'street' in tag.attrib['k'] and street_name not in street_names_set:
                street_names_set.add(street_name)
    return street_names_set
    
def audit():
    filename='tunis_tunisia.osm'
#    list_tags(filename)
#    print('#################################################')
#    list_tag_names(filename)
#    print('#################################################')
#    list_phone_numbers(filename)
#    print('#################################################')
#    list_emails(filename)
#    print('#################################################')
#    list_housenumbers(filename)
#    print('#################################################')
#    list_postcodes(filename)
#    print('#################################################')
#    governorate=count_governorate(filename)
#    print 'Number of governorates',len(governorate)
#    print governorate
    streets=list_street_names(filename)
    print len(streets)
    print streets
audit()
    