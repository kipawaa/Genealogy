# Genealogy
This project generates a simple HTML website from a CSV file of genealogical data.
The key advantage of this project over other available services is that this project does not require a common ancestor (root node).
The submitted data can have any graph shape.
The custom sorting algorithm automatically places children beneath their parents, partners adjacent to one another, and places siblings in groups.
Generations are visually separated for clarity.

## Features
- No common ancestor (root) required
- Automatic sorting - no need to order the CSV entries
- Different coloured links for parent-child connections and partner connections
- Capable of handling multiple partners
- Zooming and panning
- Clear generational gaps
- Simple CSV input format

## Sample:
Input data:

|ID |Name|Parent 1|Parent 2|Partner IDs|
|---|----|--------|--------|-----------|
1|John Doe|||2|
2|Jane Doe|||1|
3|Jim Doe|1|2||
4|Jill Doe|1|2|

Output Graph:
![graph image](/images/example.png)

## More Complicated:
Input Data:


|ID |Name|Parent 1|Parent 2|Partner IDs|
|---|----|--------|--------|-----------|
1|Queen Elizabeth II|||2
2|Prince Philip||1
3|Princess Diana|||4
4|King Charles|1|2|3 5
5|Camilla Parker Bowles|||4
6|Sophie Rhys-Jones|||7
7|Prince Edward|1|2|6
8|Kate Middleton|||9
9|Prince William|3|4|8
10|Prince Harry|3|4|11
11|Meghan Markle|||10
12|James Windsor|6|7
13|Louise Windsor|6|7
14|Princess Anne|1|2|15 16
15|Mark Phillips|||14
16|Timothy Laurence|||14
17|Prince Andrew|1|2|18
18|Sarah Ferguson|||17
19|Peter Phillips|14|15|20
20|Autumn Phillips||||19
21|Zara Tindall|14|15|22
22|Mike Tindall|||21
23|Princess Eugenie|17|18|24
24|Jack Brooksbank|||23
25|Princess Beatrice|17|18|26
26|Edoardo Mapelli Mozzi|||25

Result:
![royal family](/images/royal_family.png)

## Non-Tree Example
|ID |Name|Parent 1|Parent 2|Partner IDs|
|---|----|--------|--------|-----------|
1|Grandparent 1|||2
2|Grandparent 2|||1
3|Grandparent 3|||4
4|Grandparent 4|||3
5|Parent 1|1|2|6
6|Parent 2|3|4|5
7|You|5|6|8
8|Your Partner|||7
9|Your Child|7|8|
10|Your Child|7|8

Result:
![no root](/images/no_root.png)
