#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from xml.dom import minidom
import enhancedminidom

DOMTree = minidom.parse("test.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("measure"):
   print ("Root element : %s" % collection.getAttribute("measure"))

# 在集合中获取所有音符
notes = collection.getElementsByTagName("note")

# 打印每个音符的详细信息
for note in notes:
   print ("*****Note*****")
   if note.hasAttribute("pitch"):
      print ("Pitch: %s" % note.getAttribute("pitch"))

   type = note.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   duration = note.getElementsByTagName('duration')[0]
   print ("Duration: %s" % duration.childNodes[0].data)
   voice = note.getElementsByTagName('voice')[0]
   print ("Voice: %s" % voice.childNodes[0].data)

