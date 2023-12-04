def count_the(l: list) -> int:
    count = 0             # 1 create, 1 assignment
    for s in l:           # repeat: len(l) times
        if s == 'the':        # 1 (short) comparison
            count += 1        # 1 add, 1 assignment
    return count          # 1 return
 # worst case: 3 + (3*len(l))
 # linear in len(l)





# How many "basic operations" in the worst and best case?
def is_member(l: list, ele) -> bool:
    for x in l:          # repeat: len(l)
        if x == ele:     # 1 comparison (*)
            return True  # 1 return
    return False         # 1 return

# worst: 1 + len(l)     LINEAR in len(l)
# best:  1 + 1          CONSTANT




def distinct(l: list) -> set:
    seen = set()
    for x in l:        
        seen.add(x)
    return seen
# best case linear (?)
# worst case = *quadratic* in len(l)


if __name__ == '__main__':
    import sys
    if(len(sys.argv) < 2):
        raise ValueError('When running this script, please give the name of the file to open.')
    file_to_open = sys.argv[1]
    opened_file = open(file_to_open, 'r', encoding='utf8')
    text = opened_file.read()
    #count = count_the(text.split())
    #print(f'That file had {count} appearances of the word "the".')   
    uniques = distinct(text.split())
    print(f'That file had {len(uniques)} unique words (including caps, punctuation, etc).')




