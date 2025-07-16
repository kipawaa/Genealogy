from itertools import groupby

def get_avg_parent_position(gens, idx_to_person, people):
    return (
            sum([(gens[idx_to_person[person.p1].gen].index(idx_to_person[person.p1]) if person.p1 else 0) + (gens[idx_to_person[person.p2].gen].index(idx_to_person[person.p2]) if person.p2 else 0) for person in people])
        / sum([sum([1 if person.p1 else 0, 1 if person.p2 else 0]) for person in people])) if any([any([person.p1, person.p2]) for person in people]) else -1

def sort_tree(people):
    # create id map
    idx_to_person = {}
    for person in people:
        idx_to_person[person.idx] = person

    # assign generations
    gens = {}
    for person in people:
        if person.gen not in gens:
            gens[person.gen] = []
        gens[person.gen].append(person)

    # use partner bfs to assign a group
    for gen in gens:
        group = 1
        for person in gens[gen]:
            if person.partners:
                visited = []
                unvisited = [person.idx]
                while unvisited:
                    current = idx_to_person[unvisited[0]]
                    visited.append(current.idx)
                    unvisited = unvisited[1:]
                    current.group = group
                    if current.partners:
                        for partner_id in current.partners:
                            if partner_id not in visited and partner_id not in unvisited:
                                unvisited.append(partner_id)
            else:
                person.group = group
            group += 1

    # sort
    for gen in sorted(gens.keys()):
        # sort generations by group
        gens[gen].sort(key=lambda person: person.group if person.group else -1)

        # use itertools to properly group by group 
        grouped = groupby(gens[gen], key=lambda person: person.group if person.group else -1)

        group_list = [list(group) for _, group in grouped]
        # sort group members by (number of partners, average parent position) then re-arrange to put most connected in the center
        for i, group in enumerate(group_list):
            group.sort(key=lambda person: (
                len(person.partners) if person.partners else -1, 
                get_avg_parent_position(gens, idx_to_person, [person])
                ))
            if len(group) > 2:
                group_list[i] = group[len(group)//2:] + group[:len(group)//2]
        
        # sort groups by average parent position
        group_list.sort(key=lambda group: get_avg_parent_position(gens, idx_to_person, group))
        gens[gen] = [person for group in group_list for person in group]

    return gens
