def generate_number(slots, allocation, free_memory, files):
    for key in slots:
        leftover = free_memory[key]
        alloc = allocation[key]
        for file in alloc:
            for i in range(files[file]):
                yield file
        while leftover > 0:
            leftover -= 1
            yield 0


if __name__ == '__main__':
    with open("./input/day9.txt", "r") as f:
        text = f.read().strip()

    slots = {i: int(text[i]) for i in range(len(text))}
    files = {i // 2: int(text[i]) for i in range(0, len(text), 2)}
    allocation = {i: [i // 2] if i % 2 ==0 else [] for i in range(len(text))}
    file_to_slot = {i // 2: i for i in range(0, len(text), 2)}
    free_memory = {i: 0 if i % 2 == 0 else int(text[i]) for i in range(len(text))}

    for id in reversed(files.keys()):
        # Find smallest slot with enough free memory
        valid_slots = [slot_id for slot_id in free_memory if free_memory[slot_id] >= files[id] and slot_id < file_to_slot[id]]
        if valid_slots:
            # Move file to new slot
            slot = valid_slots[0]
            allocation[slot].append(id)
            free_memory[slot] -= files[id]

            free_memory[file_to_slot[id]] += files[id]
            allocation[file_to_slot[id]].remove(id)
            file_to_slot[id] = slot

    gen = generate_number(slots, allocation, free_memory, files)

    total = 0
    # values = []
    for i, value in enumerate(gen):
        # values.append(value)
        total += i * value

    # print([str(v) if v else '.' for v in values])
    print(total)
