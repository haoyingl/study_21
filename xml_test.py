#!/usr/bin/python3
import xml.etree.ElementTree as ET
tree = ET.parse('xml.txt')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

