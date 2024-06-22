# tuple = ("aam", "jam", "kala", "lichu", "pepe", "jamrul", "lebu", "peyara")
# print(tuple)

# fruits = ("aam", "jam", "kala", "lichu", "pepe", "jamrul", "lebu", "peyara")
# list = list(fruits)
# list[1] = "kola"
# fruits = tuple(list)
# print(fruits)

# tuple1 = ("aam", "jam", "kala", "lichu", "pepe", "jamrul", "lebu", "peyara")
# tuple2 = ("Ford", "BMW", "Volvo")
# tuple1 += tuple2
# print(tuple1)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
# fruits = (green, *tropic, red) 

print(green)
print(tropic)
print(red)