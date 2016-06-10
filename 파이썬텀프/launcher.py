loopFlag = 1
from internetcountry import *
from country_ui import *

sizelist =[]
sortedDic = [()]*0
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

class MyForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.list = []
        self.buf = ""

        self.item1 = "중동/아프리카"
        self.item2 = "아시아/태평양"
        self.item3 = "미주"
        self.item4 = "유럽"
        self.ui.comboBox.addItem(self.item1)
        self.ui.comboBox.addItem(self.item2)
        self.ui.comboBox.addItem(self.item3)
        self.ui.comboBox.addItem(self.item4)
    def slot1_click(self): # 프린트
        self.ui.textEdit.clear()
        self.list = PrintCountryList(["countryName",])
        for i in self.list:
            self.ui.textEdit.append(i)
        self.list = []
    def slot2_click(self): # 땅정렬
        global sizelist,sortedDic
        self.ui.textEdit.clear()
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
            self.buf = (str(i[0]) +' '+ '='+' '+str(i[1])+'㎢')
            self.ui.textEdit.append(self.buf)
            #print(i[0] ,'=',i[1] ,'㎢')
        self.buf = ''   
    def slot3_click(self): # 대륙별 나라
        self.ui.textEdit.clear()
        #self.ui.textEdit.append("----Continent List----\n1.중동/아프리카\n2.아시아/태평양\n3.미주\n4.유럽\n")   
        if self.ui.comboBox.currentIndex() == 0:
            self.list = ContinentNameList('1')
        elif self.ui.comboBox.currentIndex() == 1:
            self.list = ContinentNameList('2')
        elif self.ui.comboBox.currentIndex() == 2:
            self.list = ContinentNameList('3')
        elif self.ui.comboBox.currentIndex() == 3:
            self.list = ContinentNameList('4')
        for i in self.list:
            self.ui.textEdit.append(i)
        self.list=[]
    def slot4_click(self): # 나라검색
        self.ui.textEdit.clear()
        self.list = SearchCountryName(self.ui.lineEdit.text())
        for i in self.list:
            self.ui.textEdit.append(i)
        self.list=[]
    #여기서 이메일 연동하렴 우진아
    def slot6_click(self): #Send 버튼을 눌렀을 때
        self.ui.textEdit.clear()
        self.ID = self.ui.lineEdit_2.text()
         #함수 사용()   //이메일 주소
        self.message = 'Mail sending complete!!!'
        self.list = self.ui.lineEdit_3.text()
        global host, port
        html = ""
        title = 'countryName'
        senderAddr = 'swj1718@gmail.com'
        recipientAddr = self.ID 
        msgtext = 'countryName'
        passwd = 'tlsdnwls3739'
        msgtext = 'y'
        if msgtext == 'y' :
            keyword = self.list 
            html = MakeHtmlDoc(SearchCountryName(keyword))
    
        import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
    
    #Message container를 생성합니다.
        msg = MIMEMultipart('alternative')

    #set message
        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
    
        msgPart = MIMEText(msgtext, 'plain')
        bookPart = MIMEText(html, 'html', _charset = 'UTF-8')
    
    # 메세지에 생성한 MIME 문서를 첨부합니다.
        msg.attach(msgPart)
        msg.attach(bookPart)
    
        print ("connect smtp server ... ")
        s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, passwd)    # 로긴을 합니다. 
        s.sendmail(senderAddr , [recipientAddr], msg.as_string())
        s.close()
    
        print ("Mail sending complete!!!")  
        self.ui.textEdit.append(self.message)
        self.list=[]
        #self.ui.lineEdit_3.Line함수 사용()   //나라이름
        #pass
    #여기까
    
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

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
app.exec_()
#while(loopFlag > 0):
    #printMenu()
    #menuKey = str(input ('select menu :'))
    #launcherFunction(menuKey)
#    loopFlag = 0
#else:
#    print ("Thank you! Good Bye")
