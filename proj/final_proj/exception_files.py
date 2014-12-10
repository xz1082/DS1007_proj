# -*- coding: utf-8 -*-
"""User defined Exception
"""

class NotValidForm(Exception):
    def __init__(self,rep):
        self.rep=rep
    def __str__(self):
        return "{} is not a valid input. Correct input should in the format of ([a,b],c)".format(self.rep)


class EmptyError(Exception):
     pass
 
        
class NotValidFeature(Exception):
     def __init__(self,feature):
         self.feature=feature
     def __str__(self):
         return "{} is not a valid feature in this program".format(self.feature)
         
class NotValidCategory(Exception):
    def __init__(self,c):
        self.c=c
    def __str__(self):
        return "{} is not a valid category in this program".format(self.c)

class ReadFileError(Exception):
     pass