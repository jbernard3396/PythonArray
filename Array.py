class Array:
    def __init__(self):
        self.collection = ''
        self.length = 0

    def __str__(self):
        return '[' + ''.join(self.collection) + ']'

    def __repr__(self):
        return '[' + ''.join(self.collection) + ']'

    def get_length(self):
        return self.length

    @staticmethod
    def _get_deliminator_by_type(obj_type):
        if obj_type is str:
            return "'"
        elif obj_type is int:
            return ''

    def push(self, item):
        deliminator = self._get_deliminator_by_type(type(item))
        if self.get_length() != 0:
            self.collection = self.collection + ', ' + deliminator + str(item) + deliminator
        else:
            self.collection = deliminator + str(item) + deliminator
        self.length += 1


def main():
    array = Array()
    print(array)
    array.get_length()
    array.push(3)
    print(array)
    array.push(4)
    print(array)
    array.push('hello, comma test')
    print(array)
    array.push('end of test')
    print(array)
    print(array.get_length())
    list = []
    print(list)
    len(list)
    list.append(3)
    print(list)
    list.append(4)
    print(list)
    list.append('hello, comma test')
    print(list)
    list.append('end of test')
    print(list)
    print(len(list))
    # array = Array(ListArray)
    # print(array)

main()
