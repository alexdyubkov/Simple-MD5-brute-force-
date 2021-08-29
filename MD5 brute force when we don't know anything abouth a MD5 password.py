#when we don't know the length of MD5 password, and what symbols to use. It starts from bruting 1 symbols - till infinit number of symbols
import hashlib
import itertools
#create encrypted password
original_password="aabh1"
hash=hashlib.md5(original_password.encode('utf-8')).hexdigest()
#print(hash)
#decrypt
j=1
while True:
    generator=itertools.combinations_with_replacement('abcfh1',j) #1st argument-what symbols to use, you can add special symbols like # _ ! @ etc
                                                                  #2nd argument - cycle. It starts from brute forcing 1 symbol and then increases by 1
    for i in generator:
            password=''.join(i)
            brut_hash=hashlib.md5(password.encode('utf-8')).hexdigest()
            if hash==brut_hash:
                print('The original password is:' + password )
                print("It's hash:" + hash)
                exit()
            else:
                print('Password: ' + password +' is incorrect')
    j+=1