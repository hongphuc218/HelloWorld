p1 = {
    'Name': 'Huy',
    'Role': 'Waiter',
    'Hour': '12',
    'Salary per Hour ($)': '0.8',
}
p2 = {
    'Name': 'Tung',
    'Role': 'Cook',
    'Hour': '24',
    'Salary per Hour ($)': '1.5',
}
p3 = {
    'Name': 'M.Duc',
    'Role': 'Manager',
    'Hour': '20',
    'Salary per Hour ($)': '2',
}
p4 = {
    'Name': 'Don',
    'Role': 'Waiter',
    'Hour': '12',
    'Salary per Hour ($)': '0.9',
}
p5 = {
    'Name': 'H.Duc',
    'Role': 'Waiter',
    'Hour': '14',
    'Salary per Hour ($)': '0.7',
}
person_list = [p1, p2, p3, p4, p5]
person_list[0] = {
    'Name': 'Huyen',
    'Role': 'Waitress',
    'Hour': '14',
    'Salary per Hour ($)': '1',
}
person_list.pop(4)
print(person_list)
