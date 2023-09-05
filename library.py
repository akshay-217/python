print("------------library management system-------------")
book=[]
c=int(input("how many book you want to enter"))
for i in range (c):
    bookname=input("enter book name")
    book.append(bookname)
def displaybooks():
    print("available books=")
    for i in book:
        print(i)
    totalcount=len(book)
    print("total no of book=",totalcount)

def issuebook():
    is_bk=input("enter book name that you want to issue")
    if is_bk in book:
        book.remove(is_bk)
        print("book issued")
    else:
        print("book is not availale")

def returnbook():
    rt_bk=input("enter book which you want to return=")
    if rt_bk not in book:
        book.append(rt_bk)
        print("book returned")
    else:
        print("invaild book")

# displaybooks()
# issuebook()
# displaybooks()
# returnbook()
# displaybooks()

while True:
    print("1:displaybooks\n2:issuebook\n3:returnbook\n4:exit")
    print("enter a number of your choice ")
    ch = int(input("enter choice number="))

    if ch == 1:
        displaybooks()
    elif ch == 2:
        issuebook()
    elif ch == 3:
        returnbook()
    elif ch == 4:
        break
    else:
        print("wrong choice number")