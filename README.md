# 南華大學資料結構-期中報告
11124213 張芮瑜
# 第一題 Python實現單項鏈表的最全教程
## 概述
單向鏈結串列（英語：singly linked list）是鏈結串列的一種，其特點是鏈結串列的鏈結方向是單向的，對鏈結串列的存取要通過從頭部開始，依序往下讀取。

一個單向鏈結串列的節點被分成兩個部分。第一個部分儲存或者顯示關於節點的資訊，第二個部分儲存下一個節點的位址。單向鏈結串列只可向一個方向節點走訪。

![image](https://github.com/user-attachments/assets/c9b9791b-0b2c-4668-aba5-b06199dced74)
## 新增節點
```
class Node(object):
    """節點"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
```
## 單項鏈結串列的操作
```
is_empty() 鏈結串列是否為空

length() 鏈結串列長度

travel() 遍歷整個鏈結串列

add(item) 鏈結串列頭部添加元素

append(item) 鏈結串列尾部添加元

insert(pos,item) 指定位置添加元素

remove(item) 刪除節點

search(item) 查找節點是否存在
```
## 單項鏈結串列的實現
```
class SingleLinkList(object):
    """單鏈表"""
    def __init__(self, node=None):
        self.__head = node
```
![202301070844302](https://github.com/user-attachments/assets/7fbc1524-f6eb-47f5-81f7-fa0e22293045)
## 判斷鏈結串列是否為空 (is_empty)
```
def is_empty(self):
        """鏈表是否為空"""
        return self.__head == None
```
![202301070844313](https://github.com/user-attachments/assets/ed3410ab-cef4-49c5-93d1-b1b1e425a1f0)
## 鏈結串列長度 (length)
```
 def length(self):
        """鏈表長度"""
        cur = self.__head
        # count紀錄數量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
```
![202301070844314](https://github.com/user-attachments/assets/cc56b2c9-e29a-41f7-aeab-eaeb574d9999)
## 遍歷整個鏈結串列 (travel)
```
def travel(self):
        """遍歷整個鏈表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")
```
![202301070844315](https://github.com/user-attachments/assets/8542edef-d848-4719-a0dd-3f325b75f768)
## 鏈結串列尾部添加元素(尾插法 append)
```
def append(self, item):
        """尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
```
![202301070844316](https://github.com/user-attachments/assets/fe1bac09-17a8-4f5f-b875-beb7806a8c94)
## 鏈結串列頭部添加元素(頭插法 add)
```
   def add(self, item):
        """頭插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
```
![202301070844317](https://github.com/user-attachments/assets/cb181a67-b1b9-456b-a2f5-c06ca674f7ec)
## 指定位置插入元素 (insert)
```
def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 循環結束後，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node
```
![202301070844318](https://github.com/user-attachments/assets/9dda2c35-d5e5-40a3-accc-268817bbec68)
## 刪除節點 (remove)
```
    def remove(self, item):
        """刪除節點"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判斷此節點是否為頭節點
                # 頭節點
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
```
![202301070844319](https://github.com/user-attachments/assets/d1a50194-076f-44c8-9b4a-42337cbab6ff)
## 查找節點是否存在 (search)
```
 def search(self, item):
        """查找節點是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
```
![2023010708443110](https://github.com/user-attachments/assets/5c2cf842-ded7-42bb-a737-44159b094645)
## 完整代碼及測試
```
# coding:utf-8

class Node(object):
    """節點"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    """單鏈表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """鏈表是否為空"""
        return self.__head == None

    def length(self):
        """鏈表長度"""
        cur = self.__head
        # count紀錄數量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍歷整個鏈表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """頭插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 循環結束後，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """刪除節點"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判斷此節點是否為頭節點
                # 頭節點
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找節點是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False



if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())


    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9) # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100) # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200) # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
```
# 結果展示
```
True
0
False
1
9 8 1 2 3 4 5 6 
9 8 1 100 2 3 4 5 6 
9 8 1 100 2 3 4 5 6 200 
9 8 1 2 3 4 5 6 200 
8 1 2 3 4 5 6 200 
8 1 2 3 4 5 6
```
![結果](https://github.com/user-attachments/assets/6a29ac99-0865-43b9-8a2c-bc841a426ce5)
