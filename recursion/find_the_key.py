def isBox(box):
    if box:
        return True
    else:
        return False
def findTheKey(box, key):
    for item in box:
        if isBox(item):
            findTheKey(item, key)
        elif item==key:
            print("Found the key!")