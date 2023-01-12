#here conftest file had the setUp function defined so no need to place it here

#to use fixture add it as argument
def testAddItemtoCart(setUp):
    print("Item added successfully")

def testRemoveItemfromCart(setUp):
    print("Item removed successfully")