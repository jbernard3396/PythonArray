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

    @staticmethod
    def _get_item_size(item):
        return str(len(str(item)))

    @staticmethod
    def _get_item_type(item):
        return str(type(item))

    @staticmethod
    def _get_first_item(custom_array):  # custom_array is a string that is empty or begins with <class '???...'>
        mutated_array = custom_array[:]
        extended_type_len = mutated_array.find('>')
        extended_type = mutated_array[:extended_type_len]
        item_type = extended_type[extended_type.find("'")+1:] # we need to write a find and pop function that handle these next three lines
        item_type = item_type[:(item_type.find("'"))]
        mutated_array = mutated_array[extended_type_len+1:]
        item_len_len = mutated_array.find(' ')
        item_len = int(mutated_array[:item_len_len])
        mutated_array = mutated_array[item_len_len+1:]
        item_value = mutated_array[:item_len]
        if item_type == 'int':  # also pull this out
            item = int(item_value)
        elif item_type == 'str':
            item = str(item_value)
        else:
            item = -1
        print(item)

    def print_item(self):
        self._get_first_item(self.collection)

    def push(self, item):
        size = self._get_item_size(item)
        item_type = self._get_item_type(item)
        if self.get_length() != 0:
            self.collection = self.collection + ', ' + item_type + size + ' ' + str(item)
        else:
            self.collection = item_type + size + ' ' + str(item)
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
    array.print_item()
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
    print(list[0])
    # array = Array(ListArray)
    # print(array)

main()
