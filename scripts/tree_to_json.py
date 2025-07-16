def tree_to_json(tree, JSON):
    with open(JSON, 'w') as jsonfile:
        jsonfile.write('{\n')
        
        # write nodes
        jsonfile.write('"nodes": [\n')
        jsonfile.write(",\n".join([person.to_json(indent=1) for gen in tree for person in tree[gen]]))
        jsonfile.write("\n]")

        # write parent links
        jsonfile.write(',\n"parent_child_links": [\n')
        jsonfile.write(",\n".join(
            [
                (person.link_to_json(person.p1) if person.p1 else "") + 
                (',\n' if person.p1 and person.p2 else "") + 
                (person.link_to_json(person.p2) if person.p2 else "") 
                for gen in tree for person in tree[gen] if person.p1
            ]))
        jsonfile.write("\n]")

        # write partner links
        jsonfile.write(',\n"partner_links": [\n')
        jsonfile.write(',\n'.join(
            [person.link_to_json(partner) 
             for gen in tree 
             for person in tree[gen] if person.partners
             for partner in person.partners]))
        jsonfile.write(']')

        jsonfile.write('\n}')
