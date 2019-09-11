arr1 = [i+1 for i in range(26)]
arr2 = [i+1 for i in range(26)]
arr3 = [i+1 for i in range(26)]
arr11 = [1,19,10,14,26,20,8,16,7,22,4,11,5,17,9,12,23,18,2,25,6,24,13,21,3,15]
arr22 = [1,6,4,15,3,14,12,23,5,16,2,22,19,11,18,25,24,13,7,10,8,21,9,26,17,20]
arr33 = [8,18,26,17,20,22,10,3,13,11,4,23,5,24,9,12,25,16,19,6,15,21,2,7,1,14]

def enciper(a):
    temp = arr11.index(arr1[ord(a)-65])
    tem = arr22.index(arr2[temp])
    temp = arr33.index(arr3[tem])
    print('{}'.format(chr(temp + 65)),end = '')

def init(a,b,c):
    for i in range(a):
        arr1.insert(0,arr1.pop())
        arr11.insert(0,arr11.pop())
    for i in range(b):
        arr2.insert(0,arr2.pop())
        arr22.insert(0,arr22.pop())
    for i in range(c):
        arr3.insert(0,arr3.pop())
        arr33.insert(0,arr33.pop())

counter = 0
a_,b_,c_ = input('请输入初始转动数（三级转轮）：').split()
init(int(a_),int(b_),int(c_))
text = input('请输入密文（大写无空格且不超过26 letter）：')
t_arr = list(text)
for i in t_arr:
    enciper(i)
    counter += 1
    arr3.insert(0,arr3.pop())
    arr33.insert(0,arr33.pop())
