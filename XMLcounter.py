# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 18:12:09 2018

@author: FURBUTT
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

urltype = input("enter URL:")

urlreq = urllib.request.urlopen(urltype)

urlopn = urlreq.read()
sum = 0
tree = ET.fromstring(urlopn)

"""
change the './/comment' to whatever tags are the parent tags
of the tags you need data from
"""
results = tree.findall('.//comment')


for i in results:
    numb = i.find('count').text
    '''change 'count' to whichever tag you need data from'''
    sum = sum + int(numb)
    
print(sum)
