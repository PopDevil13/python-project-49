def group_by(listd, key):
    grouped = {}
    for d in listd:
        group_value = d.get(key)
        if group_value not in grouped:
            grouped[group_value] = []
        grouped[group_value].append(d)
        return grouped 

  







students = [
    {'name': 'Tirion', 'class': 'B', 'mark': 3},
    {'name': 'Keit', 'class': 'A', 'mark': 3},
    {'name': 'Ramsey', 'class': 'A', 'mark': 4},
]

print(group_by([], ''))  # => {}
print(group_by(students, 'mark'))

# => {
# =>   3: [
# =>     {'name': 'Tirion', 'class': 'B', 'mark': 3},
# =>     {'name': 'Keit', 'class': 'A', 'mark': 3},
# =>   ],
# =>   4: [
# =>     {'name': 'Ramsey', 'class': 'A', 'mark': 4},
# =>   ],
# => }