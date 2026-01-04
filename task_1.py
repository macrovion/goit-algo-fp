class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# функція виводить список у форматі: 1 -> 2 -> 3
def print_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values) if values else "Empty List")

# функція створює зв'язний список із масиву чисел
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head


# функція реалізує реверсування однозв'язного списку, змінюючи посилання
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next   
        curr.next = prev        
        prev = curr             
        curr = next_temp       
    return prev

# алгоритм сортування вставками
def insertion_sort_list(head):
    if not head or not head.next:
        return head
        
    dummy = ListNode(0) # фіктивний початок відсортованого списку
    curr = head
    
    while curr:
        next_temp = curr.next
        
        # шукаємо місце вставки в новому списку
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
            
        # вставляємо curr між prev і prev.next
        curr.next = prev.next
        prev.next = curr
        
        curr = next_temp
        
    return dummy.next

# алгоритм сортування злиттям
def merge_sort(head):
    if not head or not head.next:
        return head
    
    # знаходимо середину
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None  # розриваємо список
    
    # рекурсивно сортуємо половини
    left = merge_sort(head)
    right = merge_sort(mid)
    
    # зливаємо відсортовані половини
    return merge_two_lists(left, right)

# об'єднання двох відсортованих списків
def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    # додаємо залишок
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
        
    return dummy.next

# тести

if __name__ == "__main__":
    print("--- 1. Тест реверсування ---")
    lst1 = create_list([1, 2, 3, 4, 5])
    print("Оригінал:", end=" ")
    print_list(lst1)
    
    reversed_lst1 = reverse_list(lst1)
    print("Реверс:  ", end=" ")
    print_list(reversed_lst1)
    print("-" * 30)

    print("--- 2. Тест сортування вставками ---")
    lst2 = create_list([4, 2, 1, 3])
    print("Вхідний: ", end=" ")
    print_list(lst2)
    
    sorted_insertion = insertion_sort_list(lst2)
    print("Вставками:", end=" ")
    print_list(sorted_insertion)
    print("-" * 30)

    print("--- 3. Тест об'єднання та сортування злиттям ---")
    # Створимо два відсортовані списки для тесту merge_two_lists
    l_a = create_list([1, 3, 5])
    l_b = create_list([2, 4, 6])
    
    merged = merge_two_lists(l_a, l_b)
    print("Об'єднання [1,3,5] та [2,4,6]:")
    print_list(merged)
    
    # тест повного Merge Sort на хаотичному списку
    lst3 = create_list([10, 1, 60, 30, 5])
    print("\nХаотичний список:", end=" ")
    print_list(lst3)
    
    sorted_merge = merge_sort(lst3)
    print("Сортування злиттям:", end=" ")
    print_list(sorted_merge)
