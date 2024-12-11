def my_ord(i): return ord("0") + i

def ord_back(val): return val - ord("0")

def decode(array):
    file_id = 0
    result = ""
    for i in range(len(array)):
        if i % 2: result += int(array[i]) * "."
        else: result += int(array[i]) * chr(my_ord(file_id)); file_id += 1
    return result

def checksum(array, part):
    if part:
        array += "0"
        current_file = 0
        starting_index = 0
        id_to_space_map = {}
        position_to_id_map = {}
        space_array = []

        for i in range(0, len(array) - 1, 2):
            position_to_id_map[i] = current_file
            id_to_space_map[current_file] = starting_index
            current_file += 1
            space = int(array[i + 1])
            starting_index += int(array[i])
            space_array.append((space, starting_index))
            starting_index += space

        accumulator = 0
        for i in range(len(array) - 2, -1, -2):
            file_length = int(array[i])
            current_file = position_to_id_map[i]
            max_index = id_to_space_map[current_file]
            current_index = max_index

            for j, tup in enumerate(space_array):
                space, starting_index = tup
                if starting_index >= max_index:
                    break
                if space >= file_length:
                    current_index = starting_index
                    diff = space - file_length
                    space_array[j] = (diff, starting_index + file_length)
                    break

            for k in range(file_length):
                accumulator += current_file * (current_index + k)
        return accumulator
    else:
        array = decode(array)
        result = 0
        reverse_index = -1
        for i in range(len(array) - array.count(".")):
            while array[reverse_index] == "." and reverse_index >= -len(array): reverse_index -= 1
            if array[i] != ".": result += ord_back(ord(array[i])) * i
            else: result += ord_back(ord(array[reverse_index])) * i; reverse_index -= 1
        return result

print() 
for part in range(2): 
    print(f"Part{part + 1}:", checksum(open("input.txt", "r").readlines()[0].strip(), part)) 
print()
