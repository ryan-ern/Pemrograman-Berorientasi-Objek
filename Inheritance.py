class Parent:
  def __init__(self):
    self.a=1
    self.b=1

  def function(self):
    print('Parent')

class Child(Parent):
  def __init__(self):
    self.c=3
    self.d=4

  def function(self):
    print('Child')
    
c=Child()
c.function()

'''
1.ERROR
2.Parent
3.ERRROR
4.1
'''