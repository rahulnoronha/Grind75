#Class for linked list node.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


#function to create Linked List
def createLinkedList(listarg):
    #Creating Linked List from the Python list
    if(len(listarg)==0):#If the length of the list is 0, return None
        listhead = None
        return listhead
    else:
        listhead = ListNode(listarg[0])    
        curr = listhead
        for i in range(1,len(listarg)):
            newnode = ListNode(listarg[i],None)
            curr.next = newnode
            curr = newnode
        return listhead


def displayLinkedList(head: ListNode):#Function to display a Singly Linked List given it's head node
    curr = head
    while(curr!=None):
        print(curr.val,end="->")
        curr = curr.next
    print(curr)    


#Function to merge the two sorted linked lists
def mergeTwoLists(list1: list, list2: list) -> ListNode:
    #First sort the lists in ascending order
    list1.sort(reverse=False)
    list2.sort(reverse=False)
    #Creating first Linked List from the Python list
    list1head = createLinkedList(list1)
    print("Linked List 1:")
    displayLinkedList(list1head)

    #Creating second Linked List from the Python list
    list2head = createLinkedList(list2)
    print("Linked List 2:")
    displayLinkedList(list2head)
    print('Merged Linked List:')
    list1 = list1head
    list2 = list2head
    if(list1!=None and list2!=None):#Case when both the lists are not empty
        dummyLinkedListNode = ListNode()
        curr = dummyLinkedListNode
        while list1 and list2:               
            if list1.val < list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2
                
        if list1 or list2:
            curr.next = list1 if list1 else list2
            
        return dummyLinkedListNode.next
    elif(list1==None and list2!=None):#Case when list1 is empty
        return list2head
    elif(list1!=None and list2==None):#Case when list2 is empty
        return list1head
    else:#Case when both lists are empty
        return None
        

displayLinkedList(mergeTwoLists(list1 = [1,3,4], list2 = [1,3,4]))
print('----------------------')
displayLinkedList(mergeTwoLists(list1 = [], list2 = []))
print('----------------------')
displayLinkedList(mergeTwoLists(list1 = [], list2 = [0]))
print('----------------------')