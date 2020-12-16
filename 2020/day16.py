from file_lines import get_file_lines

lines = get_file_lines('day16.in')

fields = {}
my_ticket = None
nearby_tickets = []

section = 0
for line in lines:
    if line == '':
        section += 1
        continue
    elif line in ('your ticket:', 'nearby tickets:'):
        continue
    if section==0:
        field, rest = line.split(': ')
        ranges = rest.split(' or ')
        r1 = ranges[0].split('-')
        r1 = range(int(r1[0]), int(r1[1])+1)
        r2 = ranges[1].split('-')
        r2 = range(int(r2[0]), int(r2[1])+1)
        fields[field] = [r1, r2]
    elif section==1:
        my_ticket = list(map(int, line.split(',')))
    else:
        nearby_tickets.append(list(map(int, line.split(','))))

#print(fields)
result = 0

valid_tickets = []
for ticket in nearby_tickets:
    is_valid = True
    for value in ticket:
        is_in = False
        for field in fields:
            if value in fields[field][0] or value in fields[field][1]:
                is_in = True
                break
        if not is_in:
            result += value
            is_valid = False
    if is_valid:
        valid_tickets.append(ticket)
print(result)

fields_on_ticket = [list(fields.keys()) for _ in my_ticket]
for ticket in valid_tickets:
    for i,value in enumerate(ticket):
        reduced_possible_fields = []
        for field in fields_on_ticket[i]:
            if value in fields[field][0] or value in fields[field][1]:
                reduced_possible_fields.append(field)
        fields_on_ticket[i] = reduced_possible_fields

def determine_fields(possible_fields, chosen=set(), i=0):
    if i==len(possible_fields):
        return [], True
    for field in possible_fields[i]:
        if field in chosen:
            continue
        chosen.add(field)
        result, success = determine_fields(possible_fields, chosen, i+1)
        chosen.remove(field)
        if success:
            return [(field, possible_fields[i][-1])] + result, True
    return None, False

#print(fields_on_ticket)        
for i,field in enumerate(fields_on_ticket):
    field.append(i)
fields_on_ticket.sort(key=len)
set_fields = determine_fields(fields_on_ticket)

result = 1
for field in set_fields[0]:
    if 'departure' in field[0]:
        result *= my_ticket[field[1]]
print(result)
