import json

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
class linkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data,self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
    
    def printLinkedList(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr =itr.next
        
        print(llstr)

    def inserValues(self, dataList):
        self.head =None
        for data in dataList:
            self.insertAtEnd(data)

    def getLength(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def removeItem(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1 :
                itr.next = itr.next.next

            itr = itr.next
            count += 1

    def insertAt(self, index, value):
        if index < 0 or index >= self.getLength():
            raise Exception("invalid index")

        if index == 0:
            self.insertAtBeginning(value)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1 :
                node = Node(value,itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insertAfterValues(self, currentData, insertValue):
        count = 0
        itr = self.head
        while itr:
            if currentData == itr.data:
                node = Node(insertValue,itr.next)
                itr.next = node
                break

            itr = itr.next 
            count += 1

    def removeValue(self,value):
        if self.head is None:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return

        count = 0 
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
            
            itr = itr.next
            count += 1

def main():
    ll = linkedList()
    # print(ll.getLength())
    # ll.inserValues(['tung','trang','erererer'])
    # print(ll.getLength())
    # ll.printLinkedList()
    # ll.removeItem(0)
    # ll.printLinkedList()
    # ll.insertAt(1,"hot boi")
    # ll.printLinkedList()
    ll.inserValues(["banana","mango","grapes","orange"])
    ll.printLinkedList()
    ll.insertAfterValues("orange","apple") # insert apple after mango
    ll.printLinkedList()
    ll.removeValue("orange") # remove orange from linked list
    ll.removeValue("banana") # remove orange from linked list
    ll.printLinkedList()


if __name__ == "__main__":
    main()
