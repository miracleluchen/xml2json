try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import simplejson as json

class XMLParser():
    tree = None
    jsonObj = {}

    def __init__(self, xmlStr):
        self.tree = ET.fromstring(xmlStr)

    def parseToJson(self, elements, jsonDict=None):
        if jsonDict is None:
            jsonDict = self.jsonObj[self.tree.tag]
        for child in elements:
            if len(child) == 0:
                jsonDict[child.tag] = child.text
            else:
                if child.tag in jsonDict:
                    tmpList = [jsonDict[child.tag]]
                    tmpList.append(jsonDict[child.tag].copy())
                    self.parseToJson(child, jsonDict[child.tag])
                    jsonDict[child.tag] = tmpList
                else:
                    jsonDict[child.tag] = {}
                    self.parseToJson(child, jsonDict[child.tag])

    def getRoot(self):
        self.jsonObj[self.tree.tag] = {}
        return self.tree

    def getJson(self):
        return self.jsonObj

with open('inputs/sample.xml', 'r') as f:
    xmlStr = f.read()
    xml = XMLParser(xmlStr)
    xml.parseToJson(xml.getRoot())
    print json.dumps(xml.getJson())
