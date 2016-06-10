from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

##### global
xmlFD = -1
CountrysDoc = None

#### xml 관련 함수 구현
def LoadXMLFromFile():
    global xmlFD, BooksDoc
    try:
        xmlFD = open('country.xml',encoding="utf-8")
    except IOError:
        print ("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print ("loading fail!!!")
        else:
            print ("XML Document loading complete")
            BooksDoc = dom
            return dom
    return None

def BooksFree():
    if checkDocument():
        BooksDoc.unlink()
        
def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc.toxml())

def SortToGround(): #땅크기정
    global CountrysDoc
    retlist = []
    namelist = []
    strinfo = ''
    count = 0
    if not checkDocument():
       return None
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    countryElements = tree.getiterator("item")
    
    for item in countryElements:
        strCountryEnglish = item.find("countryEnName")
        strInfo = item.find("basic")
        namelist.append(strCountryEnglish.text)
        retlist.append(strInfo.text)

    strinfo = str(''.join(retlist))
    sub = "면"
    buf = ''
    sizeList = []
    di = {}
    isNotEmpty = False
    #print('len = ',len(retlist))
    #print(retlist[1]) 
    for i in range(len(retlist)):
        if retlist[i].find((sub)): #해당문자가 있으면
            isNotEmpty = False
            for j in range(len(retlist[i])):
                if len(retlist[i])-1 == j:
                    sizeList.append('')
                    #print("끝일떄추가")
                    break
                if retlist[i][j] == ' ':
                    continue
                if (retlist[i][j] == '㎢' or retlist[i][j] == 'K' or\
                   retlist[i][j] == 'k' or retlist[i][j] == '제' or \
                   retlist[i][j] == '평') and isNotEmpty == True:
                    buf += '000'
                    sizeList.append(buf)
                    buf = ''
                    break
                if retlist[i][j] == '㎡':
                    sizeList.append(buf)
                    buf = ''
                    break
                if retlist[i][j] == ',':
                    continue
                if retlist[i][j] == '면':
                    for z in range(30):
                        if retlist[i][j+z] == '적' or retlist[i][j+z] == ' ' or \
                           retlist[i][j+z] == ',' or retlist[i][j+z] == '약' or\
                           retlist[i][j+z] == ':':
                            continue
                        if retlist[i][j+z] == '만' :
                            buf += '0000'
                            break
                        if retlist[i][j+z] == '제' or retlist[i][j+z] == '㎢' or\
                           retlist[i][j+z] == 'K' or retlist[i][j+z] == 'k' or\
                           retlist[i][j+z] == '.' or retlist[i][j+z] == '평':
                            break
                        if 48 > ord(retlist[i][j+z]) :
                            continue
                        if ord(retlist[i][j+z])>57:
                            continue
                        buf += retlist[i][j+z]
                        isNotEmpty = True
                    
    #print(len(namelist))
    #print(len(sizeList))
    #for i in range(len(namelist)):
    #    print(namelist[i] ,'=', sizeList[i])
    return namelist, sizeList

def PrintCountryList(tags):
    global CountrysDoc
    count = 0
    if not checkDocument():
       return None

    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    
    countryElements = tree.getiterator("item")
    for item in countryElements:
        count+=1
        strCountry = item.find("countryName")
        print("Name = ",strCountry.text)
    print(count)       

def SearchCountryName(keyword):
    global CountrysDoc
    retlist = []
    if not checkDocument():
        return None
        
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    
    #get Book Element
    countryElements = tree.getiterator("item")  # return list type
    
    for item in countryElements:
        strCountry = item.find("countryName")
        strCountryEnglish = item.find("countryEnName")
        strInfo = item.find("basic")
        #print(type(str(strCountryEnglish)))
        strImageURL = item.find("imgUrl")
        strContinent = item.find("continent")
        if (strCountry.text.find(keyword) >=0 ):
            retlist.append(strCountry.text)
            retlist.append(strCountryEnglish.text)
            retlist.append(strContinent.text)
            retlist.append(strInfo.text)
            retlist.append(strImageURL.text)
            return retlist
        
    #for item in countryElements:
    #    strCountry = item.find("countryName")
    #    if (strCountry.text.find(keyword) >=0 ):
    #        retlist.append((item.attrib["id"], strCountry.text))
    
    return retlist

def ContinentNameList(keyword):
    global CountrysDoc
    namelist = []
    if not checkDocument():
        return None
        
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    
    countryElements = tree.getiterator("item")  # return list type
    for item in countryElements:
        strContinent = item.find("continent")
        strCountryName = item.find("countryEnName")
        if (keyword == '1' and strContinent.text == '중동/아프리카'):
            namelist.append(strCountryName.text)
        if (keyword == '2' and strContinent.text == '아시아/태평양'):
            namelist.append(strCountryName.text)
        if (keyword == '3' and strContinent.text == '미주'):
            namelist.append(strCountryName.text)
        if (keyword == '4' and strContinent.text == '유럽'):
            namelist.append(strCountryName.text)
            
    return namelist

def MakeHtmlDoc(BookList):
    from xml.dom.minidom import getDOMImplementation
    #get Dom Implementation
    impl = getDOMImplementation()
    
    newdoc = impl.createDocument(None, "html", None)  #DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for bookitem in BookList:
        #create bold element
        b = newdoc.createElement('b')
        #create text node
        ibsnText = newdoc.createTextNode(bookitem)
        b.appendChild(ibsnText)

        body.appendChild(b)
    
     
    top_element.appendChild(body)
    
    return newdoc.toxml()


def printBookList(blist):
    for res in blist:
        print (res)
    
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True
