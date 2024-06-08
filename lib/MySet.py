class MySet:
    def __init__(self ,enumerable = []):
        self.dictionary ={}
        for value in enumerable:
            self.dictionary[value]=True

    def has(self,value):
        return value in self.dictionary
    
    def add(self,value):
        self.dictionary[value]=True
        return self
    
    def delete(self,value):
        self.dictionary.pop(value,None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()

    def __str__(self):
        elements = sorted(self.dictionary.keys())
        elements_str = ', '.join(str(elem) for elem in elements)
        return f'MySet: {{{elements_str}}}'
    


    
