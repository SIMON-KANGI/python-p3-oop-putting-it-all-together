#!/usr/bin/env python3

class Shoe:
    condition="New"
    def __init__(self, brand, size):
        self._size=size
        self._brand=brand
        self.condition="Used"
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        if isinstance(size,int):
            self._size=size
        else:
            print("size must be an integer")
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,brand):
        self._brand=brand
        
    def cobble(self):
        self.condition="New"
        print("Your shoe is as good as new!")
        