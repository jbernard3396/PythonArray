class Array:
    def __init__(self, collection=0):
        try:
            len(collection)
        except TypeError:
            collection = []
        self.collection = collection

    def __str__(self):
        return ' '.join(self.collection)

    def __repr__(self):
        return ' '.join(self.collection)

def main():
    array = Array()
    print(array)
    listArray = ['hi', 'good job']
    array = Array(listArray)
    print(array)

main()
