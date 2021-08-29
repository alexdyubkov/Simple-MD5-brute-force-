# Simple-MD5-brute-force  
There are 2 python scripts:  
a)MD5 brute force when we don't know anything abouth a MD5 password.py  
b)MD5 brute force when we know length of MD5 pass and know what symbols were used.py  
  
Logis is simple:  
In string original_password="aabh1" we assign the password->script make a hash of it-> we put info about symbols if we know what symbols were uses -> script tries to find the original password  
  
Example output: 
...  
Password: aabcc is incorrect  
Password: aabcf is incorrect  
Password: aabch is incorrect  
Password: aabc1 is incorrect  
Password: aabff is incorrect  
Password: aabfh is incorrect  
Password: aabf1 is incorrect  
Password: aabhh is incorrect  
The original password is:aabh1  
It's hash:c7c6fbf03a77b5674e5c6078ba2c86a6  
