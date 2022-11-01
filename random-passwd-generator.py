import random
import string

print()
r = int(input ("Enter the password lenghth you wish: "))
rd = (random.choices(string.ascii_letters, k=r)) #create a random letters
symlist = (['!', '@', '#', '$', '%','^','&','*','(',')','-','_',"+","=",'/'])#symble variable
synlist_rdom = random.sample(symlist, 1) #random symble variable

nu = random.randint(0, 200) #random number variable
rdcan = ("".join((rd))) #create a combined letters string

print (f"Your random number: {nu}") #print the random number
print (f"Your random letters: {(rd)}") #print the random letters
print(f"Your random symbol: {synlist_rdom[0]}") ##print the random character
print ()

combo = str(synlist_rdom[0])+(rdcan)+str(synlist_rdom[0])+str(nu) #combine the password string numbers and letters
leng = len(combo) #combined letters and numbers to create passwd
print ()
nu_char_rem = (leng-r) #determining the number of characters to be removed from the passwd string

short_leng = combo[nu_char_rem:] #removing the extra characters
print (f"Your random combined password is: {short_leng}")
print ()
