class Table:
    def __init__(self, name):
        self.name = name
        self._rows = []
        self._next_id = 1

    def insert(self, **kwargs):
        row = {'id': self._next_id, **kwargs}
        self._rows.append(row)
        self._next_id += 1
        return row

    def select(self, **filters):
        if not filters:
            return list(self._rows)
        result = []
        for row in self._rows:
            if all(row.get(k) == v for k, v in filters.items()):
                result.append(row)
        return result

    def delete(self, **filters):
        before = len(self._rows)
        self._rows = [
            row for row in self._rows
            if not all(row.get(k) == v for k, v in filters.items())
        ]
        return before - len(self._rows)

    def __repr__(self):
        return f"Table('{self.name}', rows={len(self._rows)})"


if __name__ == '__main__':
    users = Table('users')
    users.insert(name='Максим', age=20)
    users.insert(name='Анна', age=22)
    users.insert(name='Иван', age=20)

    print("Все пользователи:", users.select())
    print("Возраст 20:", users.select(age=20))
    users.delete(name='Иван')
    print("После удаления:", users.select())
