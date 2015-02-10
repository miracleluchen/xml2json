xml2json
========

convert xml format data to json format

Usage:
 with open('inputs/sample.xml', 'r') as f:
     xmlStr = f.read()
     xml = XMLParser(xmlStr)
     xml.parseToJson(xml.getRoot())
     print json.dumps(xml.getJson())

Please note that when doing the conversion, the attribute in xml tag will be ignored.
