loopFlag = 1
from internetcountry import *

sizelist =[]
sortedDic = [()]*0
#### Menu  implementation
def printMenu():
    print("\nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    #print("Load xml:  l")
    #print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Country list: b")
    #print("Add new book: a")
    print("SearchCountry Title: e")
    print("SortByGround: s")
    print("ContinentList: w")
    #print("Make html: m")
    print("----------------------------------------")
    #print("Get book data from isbn: g")
    print("send maIl : i")
    #print("sTart Web Service: t")
    print("========Menu==========")
    
def launcherFunction(menu):
    if menu == 'q':
        QuitBookMgr()
    elif menu == 'b':
        PrintCountryList(["countryName",])
    elif menu == 'e':
        keyword = str(input ('input keyword to search :'))
        printBookList(SearchCountryName(keyword))
    elif menu == 'g': 
        isbn = str(input ('input isbn to get :'))
        #isbn = '0596513984'
        ret = getBookDataFromISBN(isbn)
        AddBook(ret)
    elif menu == 'w':
        print("----Continent List----\n","1.중동/아프리카\n"\
              ,"2.아시아/태평양\n","3.미주\n","4.유럽\n")
        keyword = str(input ('input number :'))
        continentList = ContinentNameList(keyword)
        for i in continentList:
            print(i)
    elif menu == 's':
        global sizelist,sortedDic
        countrylist,groundlist = SortToGround()
        
        for i in range(len(countrylist)):
            if groundlist[i] == '':
                sizelist.append(float('0'))
            if groundlist[i] != '':
                sizelist.append(float(groundlist[i]))
                sizelist[i] /= 1000
                sortedDic.append((countrylist[i],sizelist[i])) 
                
        sortedDic.sort(key = lambda item:item[1])
        for i in sortedDic:
            print(i[0] ,'=',i[1] ,'㎢')
        
    elif menu == 'i':
        sendMain()
    #elif menu == "t":
    #    startWebService()
    else:
        print ("error : unknow menu key")

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()
    
##### run #####
LoadXMLFromFile()
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")
