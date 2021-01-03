class Node:
    def __init__(self,data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def printForward(self):
        if self.head is None:
            print("Emty doubly List")
            return
        
        itr = self.head
        forwardll = ""
        while itr:
            forwardll += str(itr.data) + "--->"
            itr = itr.next
        
        print(forwardll)
    
    def printBackWard(self):
        if self.lastNode() is None:
            print("Empty doubly List")
            return

        backwardll= ""
        itr =self.lastNode()
        while itr:
            backwardll += str(itr.data) + "-->"
            itr = itr.prev

        print("Reverse Linked List:",backwardll)

    def lastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insertLinkedList(self, dataList):
        self.head = None
        for data in dataList:
            self.insertAtEnd(data)

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data,None,None)
            return

        itr = self.head

        while itr.next:
            itr= itr.next
            
        itr.next = Node(data,None,itr)

    def inserAtBeginning(self,data):
        if self.head is None:
            node = Node(data,self.head,None)
            self.head = Node
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node

    def insertAtIndex(self, index, value):
        if index < 0 or index > self.getLength():
            raise Exception("invalid index")
        
        if index == 0:
            self.inserAtBeginning(value)
            return

        itr = self.head
        count = 1
        while itr:
            if count == index:
                node = Node(value,itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

def main():
    ll = DoublyLinkedList()
    ll.insertLinkedList(["banana","mango","grapes","orange"])
    # ll.printForward()
    # print(ll.getLength())
    # ll.printBackWard()
    ll.insertAtEnd("figs")
    # ll.printForward()
    # ll.printBackWard()
    ll.insertAtIndex(4,"kiwi")
    ll.insertAtIndex(0,"jackfruit")
    ll.insertAtIndex(6,"dates")
    ll.printForward()
    ll.printBackWard()

if __name__ == "__main__":
    main()