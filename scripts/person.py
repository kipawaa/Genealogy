class Person:
    def __init__(
            self,
            idx=None,
            name=None,
            birth_death=None,
            p1=None,
            p2=None,
            partners=None,
            gen=None,
            notes=None):
        self.idx = idx
        self.name = name
        self.birth_death = birth_death
        self.p1 = p1
        self.p2 = p2
        self.partners = partners
        self.gen = gen
        self.notes = notes

        self.group = None
        self.x = 0 
        self.y = 0

    def __repr__(self):
        return f"{self.name}: idx: {self.idx}, b/d: {self.birth_death}, p1: {self.p1}, p2: {self.p2}, partners: {self.partners}, gen: {self.gen}, group: {self.group}"

    def to_json(self, indent=0):
        return ('\t' * indent + '{\n' + 
                '\t' * (1 + indent) + f'"idx": {self.idx},\n' +
                '\t' * (1 + indent) + f'"name": "' + ''.join([char if char != '"' else '\\"' for char in self.name]) + '",\n' +
                '\t' * (1 + indent) + f'"birth_death": "{self.birth_death if self.birth_death else "null"}",\n' +
                '\t' * (1 + indent) + f'"p1": {self.p1 if self.p1 else "null"},\n' +
                '\t' * (1 + indent) + f'"p2": {self.p2 if self.p2 else "null"},\n' +
                '\t' * (1 + indent) + f'"partners": {self.partners if self.partners else "null"},\n' +
                '\t' * (1 + indent) + f'"gen": {self.gen},\n' +
                '\t' * (1 + indent) + '"notes": ' + (('"' + self.notes.strip() + '"') if self.notes else "null") + ',\n' +
                '\t' * (1 + indent) + '"targ_x": ' + str(self.x) + '\n' +
                '\t' * indent + '}')

    def link_to_json(self, idx):
        return '{' + f'"source": {self.idx}, "target": {idx}' + '}'
