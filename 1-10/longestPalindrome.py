# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 07:26:23 2018

@author: Osman Akar
Leetcode, P4

Given a string s, find the longest palindromic substring in s. You may assume 
that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

from math import floor
#import math.floor as floor

#helper functions
def reverse(s):
    return s[::-1]
 
def isPalindrome(s):  
    if s == "":
        return False
    #input should be string
    # Calling reverse function
    rev = reverse(s)
    # Checking if both string are equal or not
    if (s == rev):
        return True
    else:
        return False

def type1(s,index,radii):
    return s[index-radii:index+radii+1]

def type2(s,index,radii):
    return s[index-radii:index+radii]
    
def longestPalindrome(s):
    maxLen = 1
    localLen = 0
    maxLenIndex = -1
    maxLenType = -1
    lenS=len(s)
    
    #search in the first half
    #for i in range(0,floor((lenS+1)/2)):
    for i in range(0,lenS):
        #type1 search
        firstRadii = floor((maxLen+1)/2)
        if i >= firstRadii and i + firstRadii< lenS and isPalindrome(type1(s,i,firstRadii)) is True:
            j = firstRadii + 1
            while i >= j and i + j < lenS and s[i-j] == s[i+j]:
                j = j+1
            maxLen = 2 * j - 1
            maxLenIndex = i
            maxLenType = 1
        #type2 search
        firstRadii = floor(maxLen/2) + 1
        if i >= firstRadii and i + firstRadii - 1< lenS and isPalindrome(type2(s,i,firstRadii)) is True:
            j = firstRadii + 1
            while i >= j and i + j -1 < lenS and s[i-j] == s[i+j-1]:
                j = j + 1
            maxLen = 2 * j - 2
            maxLenIndex = i
            maxLenType = 2
            
    if maxLenType is 1:
        return type1(s, maxLenIndex, floor((maxLen-1)/2)), maxLen
    else:
        return type2(s, maxLenIndex, floor((maxLen)/2)), maxLen
    
#%%
#test:
t1 = "abacdef"
t2 = "abababccccccedde"
t3 = "abcdede"
    
    
    
    
    
    
    
    
    
    
    
    