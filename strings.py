a = 'hello'
print(len(a))
b = 'hello world'
print(len(b))
print(b[5])
c = "This is a new string"
print(c[-2])
print(c[2:])
print(b[:3])
print(a[1:3])
d = "Just another new string"
print(d[::2])
print(d[1:8:3])
e = "The last new string probably"
print(e[::-1])
print(e[::-2])
# e[2] = "y"
print(e)
print(e*10)
f = "This is the last maybe, who knows"
print(f.upper())
print(f.lower())
print(f.split())
print(f.split('i'))
g = "Another {} string for formatting {} {} {}"
print(g.format("new", "maybe", "who", "knows"))
h = "Just {0} more formatting {2} and then I'm {1}"
print(h.format("some", "done", "testing"))
i = "HAHA HAH {1} {0} {0} bleh"
print(i.format("bleh", "haha", "hmm"))
print("I'm {j} of creating variables {k} I can go all day".format(j="tired", k="but"))
j = 100/777
print(j)
k = "Now, I'm doing float formatting, the result was {r:1.3f}"
print(k.format(r=j))
l = "Now, I'm using f-string formatting"
name = "AbstractGhoul05"
age = "confidential"
print(f"Hello, his name is {name} and his age is {age}")