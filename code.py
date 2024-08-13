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
