# File: LinkedList.py
# Date: April 20, 2020
# Author: COMP 120
# Description: Contains linked list classes

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e
    
        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
    
        self.__size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    # return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    # Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Check if lists are equal to one another
    def __eq__(self, otherList):
        if self.getSize() != otherList.getSize():
            return False
        else:
            cur_self = self.__head
            cur_other = otherList.__head
            while cur_self:
                if cur_self.element != cur_other.element:
                    return False
                else:
                    cur_self = cur_self.next
                    cur_other = cur_other.next
            return True

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return true if this list contains the element o 
    def contains(self, e):
        cur = self.__head
        while cur != None:
            if e == cur.element:    
                return True
            else:
                cur = cur.next
        return False

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        if self.__size == 0:
            return False
        elif self.__head.element == e:
            self.__head = self.__head.next
            self.__size -= 1
            return True
        else:
            cur = self.__head
            while cur.next != None:
                if e == cur.next.element:  
                    cur.next = cur.next.next  
                    self.__size -= 1
                    return True
                else:
                    cur = cur.next
            return False

    # Return the element from this list at the specified index 
    def get(self, index):
        print("Implementation left as an exercise")
        return None

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Return the index of the last matching element in this list
    # Return -1 if no match. 
    def lastIndexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Replace the element at the specified position in this list
    # with the specified element. */
    def set(self, index, e):
        print("Implementation left as an exercise")
        return None
    
    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    
# The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element

class MyLinkedList(LinkedList):
    """
    Extends the capabilities of the LinkedList class.
    """
    
    def __init__(self):
        """
        Initialize the MyLinkedList object.
        """
        super().__init__()

    # An example of the methods in MyLinkedList
    def addNew(self, otherList): 
        """
        Adds to the front of the self list all elements of 
        otherList that are not already in the self list.
        
        Returns True if the self list is changed as a result
        of the method call, and False otherwise.
        """
        changed = False
        for item in otherList:
            if not self.contains(item):
                self.addFirst(item)
                changed = True
        return changed

    def addAll(self, otherList): 
        """
        Appends (to the end) all elements of otherList to 
        the self list.  self might contain duplicates,
        so each element of otherList is appended to self,
        regardless of whether the element already exists
        in self.
        
        Returns True if the self list is changed as a result
        of the method call, and False otherwise.
        """
        pass #  you will replace this with your method implementation

    def removeAll(self, otherList):
        """
        Removes all instances of otherList from the
        self list.  (If an element of otherList appears  
        multiple times in self, then all instances are removed,
        not just the first one.)
        
        Returns True if the self list is changed as a result
        of the method call, and False otherwise.
        """

        pass #  you will replace this with your method implementation


    def retainAll(self, otherList):
        """
        Removes all elements in self that do not appear
        in otherList. 
        
        Returns True if the self list is changed as a result
        of the method call, and False otherwise.
        """

        pass #  you will replace this with your method implementation


if __name__ == "__main__":
    # Initialize lists
    lista = ['red', 'green', 'red', 'black']
    listb = ['red', 'black', 'yellow']
    listc = ['black', 'red', 'green', 'purple']
    list2 = MyLinkedList()
    for s in listb:
        list2.add(s)
    list3 = MyLinkedList()

    # test addAll method
    print("Testing addAll method")
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    ans = ['red', 'green', 'red', 'black', 'red', 'black', 'yellow']
    correct_list = MyLinkedList()
    for s in ans:
        correct_list.add(s)
    print("list1 is ", list1)
    print("list2 is ", list2)
    print("list1.addAll(list2) should be ", correct_list)
    ret_val = list1.addAll(list2)
    print("After list1.addAll(list2), list1 is", list1)
    is_list_correct = list1 == correct_list
    if is_list_correct:
        print("Your returned list is correct")
    else:
        print("Your returned list is incorrect")
    is_return_val_correct = ret_val == True
    print("addAll returned", ret_val)
    if is_return_val_correct:
        print("Your returned value is correct")
    else:
        print("Your returned value is incorrect (should be True)")

    # test addAll method
    print("\nTesting addAll method")
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    ans = ['red', 'green', 'red', 'black']
    correct_list = MyLinkedList()
    for s in ans:
        correct_list.add(s)
    print("list1 is ", list1)
    print("list3 is ", list3)
    print("list1.addAll(list3) should be ", correct_list)
    ret_val = list1.addAll(list3)
    print("After list1.addAll(list3), list1 is", list1)
    is_list_correct = list1 == correct_list
    if is_list_correct:
        print("Your returned list is correct")
    else:
        print("Your returned list is incorrect")
    is_return_val_correct = ret_val == False
    print("addAll returned", ret_val)
    if is_return_val_correct:
        print("Your returned value is correct")
    else:
        print("Your returned value is incorrect (should be False)")

    # test removeAll
    print("\nTesting removeAll method")
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    ans = ['green']
    correct_list = MyLinkedList()
    for s in ans:
        correct_list.add(s)
    print("list1 is ", list1)
    print("list2 is ", list2)
    print("list1.removeAll(list2) should be ", correct_list)
    ret_val = list1.removeAll(list2)
    print("After list1.removeAll(list2), list1 is", list1)
    is_list_correct = list1 == correct_list
    if is_list_correct:
        print("Your returned list is correct")
    else:
        print("Your returned list is incorrect")
    is_return_val_correct = ret_val == True
    print("removeAll returned ", ret_val)
    if is_return_val_correct:
        print("Your returned value is correct")
    else:
        print("Your returned value is incorrect (should be True)")

    # test removeAll
    print("\nTesting removeAll method")
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    ans = ['red', 'green', 'red', 'black']
    correct_list = MyLinkedList()
    for s in ans:
        correct_list.add(s)
    print("list1 is ", list1)
    print("list3 is ", list3)
    print("list1.removeAll(list3) should be ", correct_list)
    ret_val = list1.removeAll(list3)
    print("After list1.removeAll(list3), list1 is", list1)
    is_list_correct = list1 == correct_list
    if is_list_correct:
        print("Your returned list is correct")
    else:
        print("Your returned list is incorrect")
    is_return_val_correct = ret_val == False
    print("removeAll returned ", ret_val)
    if is_return_val_correct:
        print("Your returned value is correct")
    else:
        print("Your returned value is incorrect (should be False)")

    # test retainAll
    print("\nTesting retainAll method")
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    ans = ['red', 'red', 'black']
    correct_list = MyLinkedList()
    for s in ans:
        correct_list.add(s)
    print("list1 is ", list1)
    print("list2 is ", list2)
    print("list1.retainAll(list2) should be ", correct_list)
    ret_val = list1.retainAll(list2)
    print("After list1.retainAll(list2), list1 is", list1)
    is_list_correct = list1 == correct_list
    if is_list_correct:
        print("Your returned list is correct")
    else:
        print("Your returned list is incorrect")
    print("retainAll returned ", ret_val)
    is_return_val_correct = ret_val == True
    if is_return_val_correct:
        print("Your returned value is correct")
    else:
        print("Your returned value is incorrect (should be True)")

    # test retainAll
    print("\nTesting retainAll method")
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    correct_list = MyLinkedList()
    print("list1 is ", list1)
    print("list3 is ", list3)
    print("list1.retainAll(list3) should be ", correct_list)
    ret_val = list1.retainAll(list3)
    print("After list1.retainAll(list3), list1 is", list1)
    is_list_correct = list1 == correct_list
    if is_list_correct:
        print("Your returned list is correct")
    else:
        print("Your returned list is incorrect")
    print("retainAll returned ", ret_val)
    is_return_val_correct = ret_val == True
    if is_return_val_correct:
        print("Your returned value is correct")
    else:
        print("Your returned value is incorrect (should be True)")

    # test retainAll
    print("\nTesting retainAll method")
    list1 = MyLinkedList()
    for s in lista:
        list1.add(s)
    list4 = MyLinkedList()
    for s in listc:
        list4.add(s)
    ans = ['red', 'green', 'red', 'black']
    correct_list = MyLinkedList()
    for s in ans:
        correct_list.add(s)
    print("list1 is ", list1)
    print("list4 is ", list4)
    print("list1.retainAll(list4) should be ", correct_list)
    ret_val = list1.retainAll(list4)
    print("After list1.retainAll(list4), list1 is", list1)
    is_list_correct = list1 == correct_list
    if is_list_correct:
        print("Your returned list is correct")
    else:
        print("Your returned list is incorrect")
    print("retainAll returned ", ret_val)
    is_return_val_correct = ret_val == False
    if is_return_val_correct:
        print("Your returned value is correct")
    else:
        print("Your returned value is incorrect (should be False)")