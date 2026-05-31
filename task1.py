from typing import Optional


class Node:
    def __init__(self, data: Optional[int] = None) -> None:
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def insert_at_beginning(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data: int) -> None:
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int) -> None:
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Optional[Node]:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def bubble_sort(self) -> None:
        if self.head is None:
            return
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        for curr_count in range(count, 0, -1):
            current = self.head
            for _ in range(curr_count - 1):
                next_node = current.next
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                current = next_node

    def merge(self, other: "LinkedList") -> "LinkedList":
        merged_list = LinkedList()
        current1 = self.head
        current2 = other.head

        while current1 and current2:
            if current1.data < current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next

        while current1:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next

        while current2:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

        return merged_list


def main() -> None:
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(10)

    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    # Додаємо кільа вузлів в початок
    llist.insert_at_beginning(30)
    llist.insert_at_beginning(35)
    llist.insert_at_beginning(40)

    print("\nЗв'язний список після додавання кількох вузлів в початок:")
    llist.print_list()

    # Реверс зв'язного списку
    llist.reverse_list()

    print("\nЗв'язний список після реверсу:")
    llist.print_list()

    llist.bubble_sort()

    print("\nЗв'язний список після сортування бульбашкою:")
    llist.print_list()

    llist2 = LinkedList()
    llist2.insert_at_end(1)
    llist2.insert_at_end(9)
    llist2.insert_at_end(5)
    llist2.insert_at_end(7)
    llist2.insert_at_end(3)

    llist2.bubble_sort()

    print("\nДругий зв'язний список після сортування бульбашкою:")
    llist2.print_list()

    merged_list = llist.merge(llist2)
    print("\nОб'єднаний зв'язний список:")
    merged_list.print_list()


if __name__ == "__main__":
    main()
