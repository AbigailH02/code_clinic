from terminaltables import AsciiTable

event_table = [
    ['Booked', 'Volunteered'],
    ['row1column1', 'row1column2'],
    ['row2column1', 'row2column2'],
    ['row3column1', 'row3column2']
]

table = AsciiTable(event_table)
print(table.table)