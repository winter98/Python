import lxml, xml.etree.ElementTree as etree


t = etree.parse(r'E:\dropzone\src\workinprogress\xml\DLTINS_20171022_01of01\DLTINS_20171022_01of01.xml')
print(t.getroot().tag)
for n in t.getiterator('*'):
    tag = n.tag.split("}")[1]
    if tag == "Pyld":
        print(n)

