COUNT = 2**8
POWER = 2**8
DAMAGE = 10
from random import randrange

class Knight:
    def __init__(self, val, idx, next=None):
        self.val = val
        self.next = None
        self.idx = idx

    def damage(self, damage):
        self.val -= damage
        if self.val < 0:
            self.val = 0
    
    def eliminated(self):
        return self.val <= 0

class Circle:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val, idx):
        new_knight = Knight(val=val, idx=idx)
        new_knight.next = self.head
        ptr = self.head

        if ptr is None:
            new_knight.next = new_knight # 1st element points to itself
            self.head = new_knight
        else:
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new_knight # insert new at the end
            new_knight.next = self.head # point new next to the head
            # optional
            # self.head = new_knight # point head to new

 
    def fight(self):
        prev = self.head
        curr = prev.next
        while curr.next != curr: # only one should remain
            if curr.eliminated():
                print(f"{curr.idx=} eliminated, {curr.val=}")
                prev.next = curr.next
            else:
                dmg = randrange(5) + 1
                print(f"{curr.idx=} {curr.val=} damaging {curr.next.idx=} {curr.next.val=} with {dmg=}")
                curr.next.damage(dmg)
                print(f"{curr.next.idx=} remaining power {curr.next.val=}")
                prev = curr
            curr = curr.next
        
    def get_winner(self):
        curr = self.head
        while curr.eliminated():
            curr = curr.next
        print(f"winner is {curr.idx=} {curr.val=}")
            
    
    def print_circle(self):
        ptr = self.head
        if ptr is not None:
            while ptr:
                print(f"{ptr.idx=} {ptr.val=} ->", end=" ")
                ptr=ptr.next
                # detect loop
                if ptr == self.head or ptr == ptr.next:
                    print(f"head {ptr.idx=} {ptr.val=}")
                    break
   
    def print_circle1(self):
        if self.head is None:
            return ""
        
        res = ""
        node = self.head
        while node:
            res += f" val={node.power} idx={node.idx}"
            node = node.next
        return res



if __name__ == "__main__":
    circle = Circle()
    for i in range(COUNT):
        circle.push(POWER, i+1)
        print("pushed")
        
    circle.print_circle()
    circle.fight()
#    circle.print_circle()
    circle.get_winner()
    circle.print_circle()

