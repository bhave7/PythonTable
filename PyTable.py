class Table:
    spaces = 5*' '
    indexs = -1

    
    class Coloumn:
        def __init__(self,name):
            self.nextCol = None
            self.name = name
            self.data = []
            
        def __setitem__(self,ix,value):
            self.data.append(value)
            
        def __getitem__(self,ix):
            return self.data[ix]
        
        
    def AddRows(self,values):
        rowInputFormats = (list,tuple,set)
        if type(values) in rowInputFormats:
                self.values = list(values)
                
        self.indexs+=1
        
        start = self.head
        for i in range(len(values)):
            start[self.indexs]=values[i]
            if len(str(values[i])) > len(self.spaces): self.spaces = len(values[i])*' '
            start = start.nextCol


            
    def AddCols(self,values):
        colInputFormats = (tuple,set,list)
        if type(values) is int: 
                values = [i for i in range(values)]
        elif type(values) in colInputFormats:
                self.values = list(values)
        else:
            raise ValueError('Only list,tuple,set or number allowed')
        
        for colvalue in values:
            newCol = self.Coloumn(colvalue)
            self.header[colvalue] = newCol.data
            if len(str(colvalue)) > len(self.spaces): self.spaces = len(colvalue)*' '
            if self.head is None:
                self.head = newCol
            else:
                aCol = self.head
                while True:
                    if aCol.nextCol is not None:
                        aCol = aCol.nextCol
                    else:
                        aCol.nextCol = newCol
                        break
    def Keys(self):
        spaces = ''
        print('HEAD')
        print(' | ')
        col = self.head
        while col:
            print(col.name,end= ' ')
            spaces += len(str(col.name)) * ' '
            col = col.nextCol
        print('\n',spaces,'=',sep='')
        
        
    def __init__(self,values=-1):
        self.head = None
        self.header = {}
        if values is not -1:  self.AddCols(values)
        
    def __setitem__(self,name,values):
        self.header.update(name,values)
        
    def __getitem__(self,name):
        return self.header[name]
    
    def __str__(self):
        output = '['
        for key in self.header.keys():
            output += str(key) + self.spaces
        
        output += ']\n'
        
        for i in range(self.indexs+1):
            for key in self.header.keys():
                output += str(self.header[key][i]) + self.spaces
            
            output += '\n'
                
        return output
                 

t1 = Table(3)
#t1.AddRow([1,2,3])
#t1.AddRow([8,10,11])
#t1.AddRow({12,18,19})
#t1.AddCols(['One','Two','Three'])
t1.AddRows([1,2,3])
t1.AddRows([11,22,33])
print(t1)
print(t1[0][1]*t1[1][0])
t1[0][0] = 15
print(t1)
#t1.Show()
#print(t1)



