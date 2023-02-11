class Fruits :
    def __init__( self, ele):
        self.__ele = ele
    def __contains__( self, ele):
        return ele in self.__ele
    def __len__( self ):
        return len( self.__ele)
Fruits_list = Fruits([ "Apple", "Banana", "Orange" ])
# protocol to get size
print(len(Fruits_list))
# protocol to get container
print("Apple" in Fruits_list)
print("Mango" in Fruits_list)
print("Orange" not in Fruits_list)