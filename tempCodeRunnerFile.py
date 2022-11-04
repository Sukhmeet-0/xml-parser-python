from xml.dom import minidom as md

mt=md.parse('sample.xml')


# data=open('sample.xml')
# a=md.parse(data)

# data =md.parseString('xml code')

tagname=mt.getElementByTagName('item')[0]
print(tagname)