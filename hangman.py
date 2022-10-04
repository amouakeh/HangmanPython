#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:10:45 2021

@author: abdulkarimmouakeh
"""
import random
def loadWords():
   
    print("Loading word list from file...") 
    with open("words.txt","r") as inFile:    # words.txt is a file containing random words 
        line=inFile.read()
    wordlist=line.split()
   
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist=loadWords()

def chooseWord(wordlist):
    return random.choice(wordlist)

secretword=chooseWord(wordlist).lower()

def isWordGuessed(secretword,lettersGuessed):
    for i in secretword:
        if i not in lettersGuessed:
            return False
        else:
            y=True
    return y

def getGuessedWord(secretword,lettersGuessed):
    x=secretword
    x=list(x)
    s=""
    for i in  range(len(x)):
        if x[i] not in lettersGuessed:
            x[i]="_"
    for e in x:
        s+=e
    return s

def getAvailableLetters(lettersGuessed):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    l=list(alphabet)
    s=""
    for i in lettersGuessed:
        if i in l:
            l.remove(i)
    for e in l:
        s+=e
    return s

def hangman(secretword):
    print("welcome to the game, Hangman!")
    print("i am thinking of",len(secretword)," letter word")
    guesses=8
    lettersGuessed=[]
    while guesses>=1:
        print("you have",guesses,"guesses left")
        print("available letters:",getAvailableLetters(lettersGuessed))
        y=input("please guess a letter:")
        if y in lettersGuessed:
            print("Oops! You've already guessed that letter")
        
        if y in secretword:
            if y not in lettersGuessed:
                lettersGuessed.append(y)
                print("Good guess:",getGuessedWord(secretword, lettersGuessed))
        if y not in (secretword and lettersGuessed) :
            lettersGuessed.append(y)
            print("Oops! that letter is not in my word",getGuessedWord(secretword, lettersGuessed))
            guesses-=1
        if isWordGuessed(secretword, lettersGuessed):
            print("Congrats you won!")
            return
    print("Sorry you ran out of guesses,the word was",secretword)

hangman(secretword)
    
        
            
            
    
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    


