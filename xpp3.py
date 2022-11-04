from xml.dom import minidom as md

mt=md.parse('sample.xml')


# data=open('sample.xml')
# a=md.parse(data)

# data =md.parseString('xml code')

# tagname=mt.getElementsByTagName('item')[0]
# print(tagname.attributes['name'].value)
# print(tagname.firstChild.data)


tagname=mt.getElementsByTagName('item')
# print(tagname[1].firstChild.data)4


# for x in tagname:
    # print(x.firstChild.data)

print(len(tagname))