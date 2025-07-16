from person import Person

def row_to_person(row):
    data = row.split(',')
    data.extend([None for i in range(8 - len(data))])
    person = Person()
    person.idx = int(data[0]) if data[0] else None
    person.name = data[1]
    person.birth_death = data[2]
    person.p1 = int(data[3]) if data[3] else None
    person.p2 = int(data[4]) if data[4] else None
    person.partners = [int(partner_id) for partner_id in data[5].split(' ')] if data[5] else None
    person.gen = int(data[6]) if data[6] else None
    person.notes = data[7]

    return person

def csv_to_people(CSV):
    people = []
    with open(CSV) as csvfile:
        csvfile.readline()
        for row in csvfile:
            people.append(row_to_person(row))

    return people
