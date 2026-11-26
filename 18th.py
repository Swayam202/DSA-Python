class node:
    def __init__(self,val):
        self.data=val
        self.next=None
class linkedlist:
        def __init__(self):
            self.head=None
        def append(self,new_node):
            if (self.head==None):
                self.head=new_node
            else:
                temp=self.head
                while(temp.next):
                    temp=temp.next
                temp.next=new_node #append new node
        def insert(self, new_node, pos):
            if pos==1:
                new_node.next=self.head
                self.head=new_node
            else: #inserting fron 2nd to last position
                p=1
                while(p!=pos-1 and temp.next!=None):
                    temp=temp.next
                    p+=1
                new_node.next=temp.next
                temp.next=new_node
                
        def print(self):
            sum=0
            temp=self.head
            while temp:
                sum+=temp.data
                print(temp.data)
                temp=temp.next
            print("count:",sum)
list=linkedlist()
n1=node(10)
n2=node(20)
n3=node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(node(40))
list.append(node(40))
list.print()
list.insert(node(100),1)
list.print()