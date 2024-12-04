
values = [1,2,3,4,5,6,7,8,9]
for value in values:
    print(value)
print(f'is this still around? {value}')

def helper(val):
    # beware...
    return value + 1

print([helper(v) for v in values])