import xml.etree.ElementTree as et
mt=et.parse("sample.xml")
mr=mt.getroot()
# print(mr)
# print(mr.tag)
# print(mr[0].tag)
# print(mr.attrib)
# for x in mr[0]:
#     print(x.tag,x.attrib,x.text)


# printing
# for x in mr.findall('food'):
#     item=x.find('item').text
#     price=x.find('price').text
#     print(item,price)


#adding string 

# for x in mr.iter('description'):
#     a=str(x.text)+' description has been added'
#     x.text=str(a)
#     x.set('updated','yes')
# mt.write('new.xml')


# adding tag

# et.SubElement(mr[0],'speciality')
# for x in mr.iter('speciality'):
#     b='south indian special'
#     x.text=str(b)
# mt.write('new2.xml')

# deleting attribute

# mr[0][0].attrib.pop('name')
# mt.write('new3.xml')

# deleting attribute
# mr[0].remove(mr[0][0])
# mt.write('new4.xml')

# deleting whole tage
# mr[0].clear()
# mt.write('new5.xml')

