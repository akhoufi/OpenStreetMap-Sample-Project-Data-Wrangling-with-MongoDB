# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:33:47 2016

@author: akhou
"""
import xml.etree.cElementTree as ET
import re
import codecs
import json

street_type_re_1 = re.compile(r'^\S+\.?', re.IGNORECASE)
street_type_re_2= re.compile(r'^\S+\.', re.IGNORECASE)


mapping = { "Imp2": "Impasse ",
            "R.": "Rue ",
            "Av":"Avenue ",
            "Imp.":"Impasse "
            }    
    
def clean_street_name(name):
    m = street_type_re_2.search(name) or street_type_re_1.search(name)
    if m:
        street_type = m.group()
        if street_type in mapping:
            new_name=name.replace(street_type,mapping[street_type])
            name=new_name
    return name

def clean_phone_number(phone_number):
    phone_number_type=re.compile(r'[^\d\+]')
    return phone_number_type.sub('',phone_number)
    
def clean_phone_numbers(phone_numbers):
    phone_number_list=phone_numbers.split('/')
    for i in range(len(phone_number_list)):
        phone_number_list[i]=clean_phone_number(phone_number_list[i])
    return phone_number_list
        

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    node = {}
    created={}
    refs=None
    lon=None
    lat=None
    address=None
    if element.tag == "node" or element.tag == "way" :
        for attr in element.attrib:
            if attr=='lat':
               lat=element.attrib[attr]
            elif attr=='lon':
                lon=element.attrib[attr]
            elif attr in CREATED:
                created[attr]=element.attrib[attr]
            else:
                node[attr]=element.attrib[attr]
        for elem in element:
            if element.tag=='way' and elem.tag=='nd':
                if not refs:
                    refs=[]
                refs.append(elem.attrib['ref'])
            elif elem.tag=='tag':
                if 'street' in elem.attrib['k']:
                    value=clean_street_name(elem.attrib['v'])
                elif'phone' or 'fax' in elem.attrib['k']:
                    value=clean_phone_numbers(elem.attrib['v'])
                else: 
                    value=elem.attrib['v']
                m = problemchars.search(elem.attrib['k'])
                if not m:
                    m=lower_colon.search(elem.attrib['k'])
                    if m:
                        splitted_tag=elem.attrib['k'].split(':')
                        if splitted_tag[0]=='addr':
                            if not address:
                                address={}
                            address[splitted_tag[1]]=value
                        else:
                            node[splitted_tag[0]]={splitted_tag[1]:value}
                    elif lower.search(elem.attrib['v']):
                        node[elem.attrib['k']]=value
                    
        node['created']=created
        if lat and lon:
            node['pos']=[float(lat),float(lon)]
        if refs:
            node['node_refs']=refs
        if address:
            node['address']=address
                
        node['type']=element.tag
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")                       
    return data
            
def clean():
    filename='tunis_tunisia.osm'
    process_map(filename)  
              
clean()