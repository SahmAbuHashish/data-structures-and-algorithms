from linked_list_insertions import LinkedList

if __name__ == "__main__":
    
    linked_list1 = LinkedList()

    linked_list1.insert("a")
    linked_list1.insert("b")
    linked_list1.insert("c")

    linked_list1.append("a")
    linked_list1.append(False)
    linked_list1.insert_before("a", "A")
    linked_list1.insert_after("c", "C")


    print(linked_list1)

    linked_list1.delete_node('c')
    print(linked_list1.includes("a"))