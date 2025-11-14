from time import perf_counter_ns
import random


class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = float(price)
        self.stock = int(stock)



class HashTableLinked:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=2000):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = self.Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None



def create_products(n):
    products = []
    for i in range(1, n + 1):
        pid = f"P{str(i).zfill(4)}"
        products.append(Product(pid, f"Product {i}", i * 2.5, 100))
    return products



def array_search(arr, pid):
    for p in arr:
        if p.pid == pid:
            return p
    return None



def main():
    n = 1000
    rounds = 1000
    products = create_products(n)
    table = HashTableLinked(capacity=2000)

    for p in products:
        table.insert(p.pid, p)

    test_ids = [p.pid for p in products]


    t0 = perf_counter_ns()
    for _ in range(rounds):
        random.shuffle(test_ids)
        for pid in test_ids:
            table.search(pid)
    t1 = perf_counter_ns()
    hash_total_ms = (t1 - t0) / 1_000_000
    hash_avg = hash_total_ms / (rounds * n)


    t2 = perf_counter_ns()
    for _ in range(rounds):
        random.shuffle(test_ids)
        for pid in test_ids:
            array_search(products, pid)
    t3 = perf_counter_ns()
    array_total_ms = (t3 - t2) / 1_000_000
    array_avg = array_total_ms / (rounds * n)

    # --- Output results ---
    print("=== Performance Comparison  ===")
    print(f"Records (n): {n} | Rounds: {rounds} | Total Lookups: {rounds * n}")
    print(f"HashTable capacity: {table.capacity}")
    print(f"Total Time - Hash Table: {hash_total_ms:.3f} ms")
    print(f"Total Time - Array     : {array_total_ms:.3f} ms")
    print(f"Average per lookup - Hash Table: {hash_avg:.6f} ms")
    print(f"Average per lookup - Array     : {array_avg:.6f} ms")

    if hash_avg < array_avg:
        print("Conclusion: Hash Table is faster overall.")
    else:
        print("Conclusion: Array is faster (but usually Hash Table wins).")

    print("\nReason:")
    print("- Hash Table ≈ O(1) on average, direct access by key.")
    print("- Array search = O(n), must check one by one, slower when n is large.")


if __name__ == "__main__":
    main()
