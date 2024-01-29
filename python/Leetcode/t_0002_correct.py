# Chinese characters are used to write comment.
# LeetCode 第二题：将两个整数相加。整数以倒序形式存储在单链表中，返回值也应是这样的倒序单链表形式。

# Definition for singly-linked list.、
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:

        dummy = ListNode(0) # 创建一个空链表用于存储答案，头端是 dummy/无效信息，因此返回值是 dummy.next 而不是 dummy

        curr = dummy # 创建 curr 用于保存正在运算中的答案（链表形式）

        carry = 0 # 正在运算中的答案中的某一位（数字形式）
    
        while l1 or l2: # 当 l1 或 l2 没有遍历结束：

            sum = carry # 一开始是 0；开始新一轮 while 循环时 sum 会变为 carry 中进过位的数字

            if l1: # l1 没有遍历结束：
                sum += l1.val # 加上 l1 当前节点的值
                l1 = l1.next # 进入下一个节点

            if l2: # l2 没有遍历结束：
                sum += l2.val # 加上 l2 当前节点的值
                l2 = l2.next # 进入下一个节点
            
            curr.next = ListNode(sum % 10) # 将 sum 除以 10 的余数（当前数位上的数字）加入 curr 的链表节点
            curr = curr.next # 将 curr 指针指向这个新创造出来的链表节点中
            carry = sum // 10 # carry 变成进位之后的数字
    
        if carry != 0: # 如果发生了进位：
            curr.next = ListNode(carry) # 将 进位后的数字加入链表节点
            # 为什么这里会存在一个重复的进位操作：如果此时加入的是最高位，那么 while 循环将会结束，这是用于在最高位发生进位的情况下做出的保险措施
    
        return dummy.next # 由于 dummy 的头端是无效信息，因此返回的是 dummy.next