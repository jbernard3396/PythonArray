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
        return str(len(str(item)) + len(Array._get_item_type(item)))

    @staticmethod
    def _get_item_type(item):
        return str(type(item))

    @staticmethod
    def _get_item_from_value_and_type(item_value, item_type):
        if item_type == 'int':  # also pull this out
            item = int(item_value)
        elif item_type == 'str':
            item = str(item_value)
        else:
            item = -1
        return item

    @staticmethod
    def _get_first_item(custom_array):  # custom_array is a string that is empty or begins with <class '???...'>
        array_copy = custom_array[:]
        item_length = Array._get_length_of_first_array_item(array_copy)
        item_type = Array._get_type_of_first_array_item(array_copy)
        item_value = Array._get_value_of_first_array_item(array_copy, item_length)
        item = Array._get_item_from_value_and_type(item_value, item_type)
        print(item)

    @staticmethod
    def _get_length_of_first_array_item(array):
        item_len_len = array.find('<')
        item_len = int(array[:item_len_len])
        return item_len

    @staticmethod
    def _get_type_of_first_array_item(array):
        extended_type_beginning = array.find('<')
        extended_type_end = array.find('>')
        extended_type = array[extended_type_beginning:extended_type_end]
        item_type = extended_type[extended_type.find("'") + 1:]  # we need to write a find and pop function that handle these next three lines
        item_type = item_type[:(item_type.find("'"))]
        return item_type

    @staticmethod
    def _get_value_of_first_array_item(array, item_length):
        item_beginning = array.find('>')+1
        item_end = item_length + len(str(item_length))
        item_value = array[item_beginning:item_end]
        return item_value

    def print_item(self):
        self._get_first_item(self.collection)

    def push(self, item):
        size = self._get_item_size(item)
        item_type = self._get_item_type(item)
        if self.get_length() != 0:
            self.collection = self.collection + ', ' + size + item_type + str(item)
        else:
            self.collection = size + item_type + str(item)
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
