my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

length = len(my_dna)

a_count = my_dna.count('A')

t_count = my_dna.count('T')

print("length: " + str(length))

print("A count: " + str(a_count))

print("T count: " + str(t_count))

test_dna = "ATGC"

length = len(test_dna)

a_count = test_dna.count('A')

t_count = test_dna.count('T')

print("length: " + str(length))

print("A count: " + str(a_count))

print("T count: " + str(t_count))

test_dna = "ATGC"

length = len(test_dna)

a_count = test_dna.count('A')

t_count = test_dna.count('T')

at_content = a_count + t_count / length

print("AT content is " + str(at_content))

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

length = len(my_dna)

a_count = my_dna.count('A')

t_count = my_dna.count('T')

at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))
