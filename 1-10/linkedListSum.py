# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 00:04:51 2018

@author: Osman
LeetCode: P2

2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
 digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):        
        ans=ListNode(0)
        traveller=ans
        #while both digits exists
        while l1 != None and l2 != None:
            traveller.next=ListNode(0)
            traveller=traveller.next                        
            #no carrying
            if l1.val + l2.val < 10:
                traveller.val = l1.val + l2.val
            #carrying
            else: 
                traveller.val = l1.val + l2.val - 10
                if l1.next != None:
                    l1.next.val = l1.next.val + 1
                else:
                    l1.next=ListNode(1)     
            l1=l1.next
            l2=l2.next
        
        if l1 is None and l2 is None:
            return ans
        
        if l1 is None:
            l3 = l2
        else:
            l3 = l1
        
        while l3 != None:
            if l3.val<10:
                traveller.next=List(l3.val)
            else:
                traveller.next=List(l3.val-10)
                if l3.next is None:
                    l3.next=ListNode(1)
                else:
                    l3.next.val=l3.next.val + 1
                
            
        return ans.next
    
             

        
        
        
        
        
        