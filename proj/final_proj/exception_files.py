# -*- coding: utf-8 -*-
"""User defined Exception
"""

class NotValidForm(Exception):
    def __init__(self,rep):
        self.rep=rep
    def __str__(self):
        return "{} is not a valid input. Correct input should in the format of ([a,b],c)".format(self.rep)



    