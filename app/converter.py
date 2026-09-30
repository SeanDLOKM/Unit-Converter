import csv

lookup = {} # Contains all conversions specified in CSV, as well as reversed conversions.
adjacency = {} # Adjacency list for all units.
all_units = set() # Set containing every unit that appears in the CSV.

with open('unit_conversions.csv', newline='') as csvfile:
    heading = next(csvfile) # skip over heading row
    tablereader = csv.reader(csvfile)
    for row in tablereader:
        all_units.add(row[0])
        all_units.add(row[1])
        if (row[0], row[1]) not in lookup:
            lookup[(row[0], row[1])] = float(row[2])
        if (row[1], row[0]) not in lookup: # Reverse conversion from target to source.
            lookup[(row[1], row[0])] = 1/float(row[2])

for conversion, factor in lookup.items():
    if conversion[0] not in adjacency:
        adjacency[conversion[0]] = {conversion[1] : factor}
    else:
        adjacency[conversion[0]][conversion[1]] = factor

def get_unit_options(units): # Takes set of units, converts them to a list of tuples containing the value and its label (capitalised version) to be used in form
    res = []
    for unit in units:
        res.append((unit, unit.capitalize()))
    return res

def get_possible_conversions(source): # Returns all possible units that a source unit can be converted to, using BFS.
    queue = [source]
    visited = set()
    while len(queue) > 0:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            for unit, factor in adjacency[current].items():
                queue.append(unit)
    return visited - {source}

def get_conversion_factor(source, target): # Calculates and returns the conversion factor for converting between two units.
    if source == target:
        return 1
    if target not in get_possible_conversions(source):
        print("Error: Invalid conversion")
        return None
    queue = [(source, 1)] # Queue contains units and the conversion factor from the source unit as a tuple item.
    visited = set()
    while len(queue) > 0:
        current = queue.pop(0)
        if current[0] not in visited:
            visited.add(current[0])
            for unit, factor in adjacency[current[0]].items():
                if unit == target:
                    return factor * current[1]
                queue.append((unit, factor * current[1]))