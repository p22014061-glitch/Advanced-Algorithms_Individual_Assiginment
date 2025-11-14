class HashTableLinked:
    class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):

        return hash(key) % self.capacity

    def insert(self, key, value):

        index = self._hash(key)
        head = self.table[index]

        cur = head
        while cur:
            if cur.key == key:
                cur.value = value
                return
            cur = cur.next

        new_node = self.Node(key, value)
        new_node.next = head
        self.table[index] = new_node

    def search(self, key):

        index = self._hash(key)
        cur = self.table[index]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None

    def delete(self, key):

        index = self._hash(key)
        cur = self.table[index]
        prev = None
        while cur:
            if cur.key == key:
                if prev:
                    prev.next = cur.next
                else:
                    self.table[index] = cur.next
                return True
            prev, cur = cur, cur.next
        return False


class Product:
    def __init__(self, pid: str, name: str, price: float, stock: int):
        self.pid = pid
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def __str__(self):
        return f"{self.pid} - {self.name} (RM{self.price:.2f}, Stock: {self.stock})"



def create_sample_products():

    return [
        Product("P001", "Baby Bottle", 25.9, 50),
        Product("P002", "Baby Diaper Pack", 48.5, 80),
        Product("P003", "Baby Lotion", 32.0, 30),
        Product("P004", "Baby Wipes", 15.5, 120),
        Product("P005", "Baby Shampoo", 22.3, 40),
    ]


def print_products(products):

    if not products:
        print("(No products)")
        return
    print("\nPID      Name                  Price        Stock")
    print("------------------------------------------------")
    for p in products:
        print(f"{p.pid:<8} {p.name:<20} RM{p.price:>7.2f} {p.stock:>10}")


def inventory_system():

    table = HashTableLinked(capacity=11)
    products = create_sample_products()

    # preload data into hash table
    for p in products:
        table.insert(p.pid, p)

    while True:
        print("\n=== Baby Products Inventory System ===")
        print("1. View Inventory")
        print("2. Insert Product")
        print("3. Search Product")
        print("4. Delete Product ")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print_products(products)

        elif choice == "2":
            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter Price (RM): ").strip())
                stock = int(input("Enter Stock: ").strip())
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            prod = Product(pid, name, price, stock)
            table.insert(pid, prod)
            # update or add product
            for i, p in enumerate(products):
                if p.pid == pid:
                    products[i] = prod
                    break
            else:
                products.append(prod)
            print("Product inserted or updated successfully.")

        elif choice == "3":
            pid = input("Enter Product ID to search: ").strip()
            result = table.search(pid)
            print(result if result else "Product not found.")

        elif choice == "4":
            pid = input("Enter Product ID to delete: ").strip()
            ok = table.delete(pid)
            if ok:
                products = [p for p in products if p.pid != pid]
                print("Product deleted successfully.")
            else:
                print("Product not found.")

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    inventory_system()
