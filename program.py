print("bobby")
#
myString = "Welcome to Programming"
#
# myList=[]
# tempString=''
# for i in myString+" ":
#     if i !=" ":
#         tempString = tempString+i
#         continue
#
#     myList.append(tempString)
#     tempString = ''
#
#
# print (myList)
#
# outputList = myList[::-1]
# outputstr=""
# for i in outputList:
#     outputstr=outputstr+" "+i
# print(outputstr)


def revstring(inputStr):
    stringList = inputStr.split(" ")
    outList = stringList[::-1]
    return " ".join(outList)

#print(revstring(myString))

def reversestring(inputStr):
    stringList=[]
    outList = []
    tempStr=''
    result =''
    for i in inputStr+' ':
        if i!=" ":
            tempStr=tempStr+i
            continue
        stringList.append(tempStr)
        tempStr=''

    for j in  stringList:
        outList.insert(0,j)
    for k in outList:
        result=result+" "+k
    return result[1::]


print(reversestring(myString))