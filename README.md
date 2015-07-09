xml2json
========

convert xml format data to json format

Usage:\n
with open('inputs/sample.xml', 'r') as f:
    xmlStr = f.read()
    xml = XMLParser(xmlStr)
    xml.parseToJson(xml.getRoot())
    print json.dumps(xml.getJson())

