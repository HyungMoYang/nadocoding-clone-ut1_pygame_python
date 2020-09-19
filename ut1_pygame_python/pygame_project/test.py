# tests = [[0, 0]]
# tests = [[i[0], i[1]-1] for i in tests]

tests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]

print(tests)
for index, test in enumerate(tests):
    if test[1] == 1:
        print("삭제")
        del tests[index]
tests = [[test[0], test[1]] for test in tests if test[1] != 1]
print(tests)

# tests = [ [test[0],test[1]] for test in tests if test[1] != 1 ]
