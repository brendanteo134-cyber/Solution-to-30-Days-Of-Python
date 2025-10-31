#Exercise: Day 7 of 30 Days of Python! (Sets)

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]# sets

print(len(it_companies))
it_companies.add("twitter")
print(it_companies)

it_companies.update(["AMD", "Nivdia", "Intel"])
print(it_companies)
it_companies.remove("Facebook")
print(it_companies)

#The difference between remove() and discard() are as followed. If the item is not found, remove() will raise errors where as discard() method doesn't raise any errors

#Exercises: Level 2

C = A.union(B)
print(C)
D = A.intersection(B)
print(D)
E = A.issubset(B)
print(E)
F = A.isdisjoint(B)
print(F)
G = A.update(B)
print(G)
H = B.update(B)
print(H)
J = A.symmetric_difference(B)
print(J)

#del A
#del B

#Exercise: Level 3

set_age = set(age)
print(set_age)
if len(set_age) > len(age):
    print("Length of set is bigger")
else:
    print("Length of list is bigger")

sentence = "I am a teacher and I love to inspire and teach people"
lst = sentence.strip().split()
words = set(lst)
print(len(words))
