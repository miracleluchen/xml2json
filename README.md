xml2json
========

convert xml format data to json format

Usage:\n
 with open('inputs/sample.xml', 'r') as f: \n
     xmlStr = f.read() \n
     xml = XMLParser(xmlStr) \n
     xml.parseToJson(xml.getRoot()) \n
     print json.dumps(xml.getJson()) \n

Please note that when doing the conversion, the attribute in xml tag will be ignored.
