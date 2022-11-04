import xml.etree.ElementTree as et


data='''<?xml version="1.0" encoding="utf-8"?>
<metadata>
<food>
    <item name="breakfast">Idly</item>
    <price>$2.5</price>
    <description>Idly sambar</description>
    <calories>600</calories>
</food>
<food>
    <item name="breakfast">Bisi bel bath</item>
    <price>$4.50</price>
    <description>Bisi bel bath with sev</description>
    <calories>400</calories>
</food>
<food>
    <item name="breakfast">Kesari bath</item>
    <price>$1.95</price>
    <description>Sweet rava with saffron</description>
    <calories>950</calories>
</food>
</metadata>'''

mt =et.fromstring(data)
print(mt.tag)