savepoint
=========

A context manager that creates savepoints, avoiding recalculating expensive     
parts of the code. Useful if you're running a script several times while        
developing it.                                                                  
                                                                                
An example:                                                                     
                                                                                
```python
from savepoint import SavePoint                                             
                                                                            
a = 10                                                                      
b = 20                                                                      
                                                                            
# do some expensive calculation here                                        
with SavePoint("stuff.p"):                                                  
    print "doing stuff"                                                     
    a += 10                                                                 
    c = 30                                                                  
                                                                            
print a, b, c                                                               
```

We now run the script twice:
                                                                               
```bash
$ python script.py                                                          
doing stuff                                                                 
20 20 30                                                                    
                                                                            
$ python script.py                                                          
20 20 30                                                                    
```
                                                                            
The first time the code is ran the ``with`` block is executed, and the modifed  
scope is pickled to ``stuff.p``. Subsequent runs will update the global scope   
from the pickle file, and skip the block completely.                            
                                                                                
Note that only changes in the scope are stored, but not file modifications and  
other side effects of the block. Also, if the original input is different the 
code will fail; this will be fixed in the future, so that the savepoint is 
only used if the initial scope is unchanged.
