def search(mylist, number):
    def search_recursive(lst, num):
        if lst[0] == num:
            return 0
        return 1 + search_recursive(lst[1:], num)

    try:
        return search_recursive(mylist, number)
    except IndexError:
        return -1


search_list = [1, 2, 3, 4, 5, 6]
res = search(search_list, 3)
# print(search_list[res])
