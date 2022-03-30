class HashTable:

    def __init__(self):
        self._data = [list() for _ in range(1024)]

    def _get_index(self, key):
        return hash(key) % len(self._data)

    def _get_value_in_lst(self, key, lst):
        for index, el in enumerate(lst):
            if el[0] == key:
                return el[1], index
        return None, -1

    def add(self, key, value):
        index = self._get_index(key)
        v, vi = self._get_value_in_lst(key, self._data[index])
        if v is None:
            self._data[index].append((key, value))
        else:
            self._data[index][vi] = (key, value)

    def delete(self, key):
        index = self._get_index(key)
        v, vi = self._get_value_in_lst(key, self._data[index])
        if v is not None:
            del self._data[index][vi]

    def contains(self, key):
        index = self._get_index(key)
        if self._data[index]:
            return self._get_value_in_lst(key, self._data[index])[0] is not None
        return False

    def get(self, key):
        index = self._get_index(key)
        if self._data[index]:
            return self._get_value_in_lst(key, self._data[index])[0]
        return None

    def __iter__(self):
        for lst in self._data:
            for el in lst:
                yield el


ht = HashTable()
for i in range(2000):
    ht.add(i, i ** 2)  # ht[i] = i ** 2

ht.delete(99)  # del ht[99]

print(ht.contains(2000))
print(ht.contains(100))  # 100 in ht
print(ht.get(100))  # ht[100]

for el in ht:
    print(el)