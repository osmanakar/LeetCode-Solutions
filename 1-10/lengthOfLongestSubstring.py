# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:06:02 2018

@author: Osman
leetcode
P3

Given a string, find the length of the longest substring without repeating 
characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence
             and not a substring.

"""
k="abcaaab"

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    lenS = len(s)
    maxLen = 0
    #maxLenIndex = 0
    localLen = 0
    subset=set(s[0])
    j=1
    for i in range(lenS):
        #subset = set(s[i:j])
        #j = i + 1
        while j < lenS and s[j] not in subset:
            subset.add(s[j])
            j = j + 1
        localLen = j - i  
        subset.discard(s[i])
        if maxLen < localLen:
            maxLen = localLen
            #maxLenIndex = i
    return maxLen    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        