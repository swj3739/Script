loopFlag = 1
from internetcountry import *

#### Menu  implementation
def printMenu():
    print("\nWelcome! Country Manager Program (xml version)")
    print("========Menu==========")
    print("xml 파일 로드:  l")
    print("xml 파일 모두 출력: p")

    print("나라이름 모두 출력: b")
    #print("Add new book: a")
    print("나라정보 검색: e")
    print("땅 크기 정렬: s")
    #print("Make html: m")
    #print("----------------------------------------")
    # print("Get book data from isbn: g")
   # print("send maIl : i")
   # print("sTart Web Service: t")
    print("프로그램 종료:   q")
    print("========Menu==========")
    
def launcherFunction(menu):
    if menu ==  'l':
        LoadXMLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'b':
        PrintCountryList(["countryName",])
    elif menu == 'e':
        keyword = str(input ('나라 이름 :'))
        printBookList(SearchCountryName(keyword))
    elif menu == 'g': 
        isbn = str(input ('input isbn to get :'))
        #isbn = '0596513984'
        ret = getBookDataFromISBN(isbn)
        AddBook(ret)
    elif menu == 'm':
        keyword = str(input ('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif menu == 's':
        #countrylist,groundlist = SortToGround()
        SortToGround()
        
    elif menu == 'i':
        sendMain()
    elif menu == "t":
        startWebService()
    else:
        print ("error : unknow menu key")

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()
    
##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")
