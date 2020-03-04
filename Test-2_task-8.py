#counting repeated alphabets
string='thequickbrownfoxjumpsoverthelazydog'
d={}
for character in string:
    if character in d:
        d[character]+=1
    else:
        d[character]=1
for ch in d:
    if(d[ch] != 1):
        print(ch,'=', d[ch])
