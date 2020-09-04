"""
-> (1, 2, 3)  ,  (4,5)
---> (1, 2)  , (3, 4, 5)

-> (1, 2) (3)   (4,) (5)

-> (1) (2) (3) (4) (5)
"""
a = [1, 2, 3, 4, 5]

# b= [a]
runAgain = False
while (runAgain):
    temp_arr = []
    for _list in b:
        if (len(_list) == 1):
            temp_arr.append(_list)

        mid_index = len(_list)/2
        left_arr = _list[0:mid_index]
        right_arr = _list[mid_index:]

        runAgain = runAgain ^ len(_list) > 1

        temp_arr.append(left_arr)
        temp_arr.append(right_arr)

    b = temp_arr

# print (b)



# def split(arr):
#     # this will be base
#     if (len(arr) == 1) :
#         print (arr[0])

#     mid = len(arr)/2
#     _left = split( arr[:mid])
#     _right = split(arr[mid:])


# split(a)

"""
 a(data, next) -> b(data, next) -> c(data -> None)




def add():


def print():

doubly linked list
"""

class DoublyLinkedListStructure():

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def add(self, data):
        """[Will add the new node at the end of the linked list]

        Arguments:
            data

        Returns:
            [DoublyLinkedListStructure] -- [Returns new node]
        """
        root_copy= self
        while (root_copy.right):
            root_copy = root_copy.right
        new_node = DoublyLinkedListStructure(data, root_copy, None)
        root_copy.right = new_node
        return new_node

    def _print(self):
        """[Prints the entire linked list]
        """
        new_object = self
        iterate_further = True
        while (iterate_further):
            print (new_object.data)
            iterate_further = new_object.right != None
            new_object = new_object.right

        # print (new_object.data)

    def _insert(self, index, data):
        """
        inserts new node at the given index in the linked list
        - Does not support inserting new node in the starting
        """
        linked_list_len = 0
        current_object = self
        index_exists = False
        iterate_further = True
        while (iterate_further):

            if (linked_list_len == index):
                new_node = DoublyLinkedListStructure(data, current_object.left, current_object)
                new_node.right = current_object
                current_object.left.right = new_node
                return (True, new_node)
            linked_list_len += 1
            iterate_further = current_object.right != None
            current_object = current_object.right

        return (False, None)



root =  DoublyLinkedListStructure(1, None, None)
root.add(2) 
# 1, 2
root.add(3) 
# 1, 2, 3
root._insert(1, 4)
# 1, 4, 2, 3
root.add(5)
 # 1, 4, 2, 3, 5
root._insert(4, 6)
root._print()


"""

addresses of the user

signup
add addresses

Tables:

1. User
    - username (char)
    - fname (char)
    - lname (char)
    - email (unique) (char)
    - password (char)

2. Country
    - name (char)
    - is_active (bool)


3. State
    - name (char)
    - fk(Country)
    - is_active

4. City
    - fk(state)
    - name (char)
    - pin_code (unique)
    - is_active (bool)

5. Address
    - fk(user)
    - fk(city)
    - is_active (bool)


1. users staying in gurgaon

- select * from user
inner join with address as user_addree where user.pk = user_address.user.id
inner join with City as _city where user_addree.city = _city, _city.name = "Gurgaon";



"""