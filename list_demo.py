#The List class provides amutable sequence of elements
empty_list = list()
print('empty_list ->', empty_list)
list_str = list('hello')
print('list_str ->', list_str)
list_tup = list((1, 2, (3, 5, 7)))
print('list_tup ->', list_tup)
empty_list = []
print('list_syn ->', list_syn)
print("'a' in list_syn ->", 'a' in list_syn)
empty_list.append(5)
print('empty_list ->', empty_list)
empty_list.append([6, 7])
print('last_elem ->', last_elem)
last_elem = empty_list.pop()
print('last_elem ->', last_elem)
print(empty_list ->', empty_list)
empty_list.append([6, 7])
print('empty_list ->', empty_list)
first_elem = empty_list.pop(0)
print('first_elem ->', first_elem)
print('empty_list ->', empty_list)
empty_list.insert(0, 10)
print('empty_list ->', empty_list)
empty_list.insert(3, 100)
print('empty_list ->', empty_list)
empty_list.remove(7)
print('empty_list ->', empty_list)


















