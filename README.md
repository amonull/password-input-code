# password-input-code
this is a code i created that uses csv files that are already created to add, delete, edit and search for passwords you have put in. this file also encrypts and dcrypts using a key from cryptography.fernet library. the general layout for the input data is Site name, UserName, Password.

IMPORTANT:
Encryption->
to use this code for the first time make sure if you do have a key file generated from cryptograhy library you put this code in the same directory as the main.py file and if you are running this code for the first time make sure you generate a key first so that you can use encryption and dcryption and the code doesnt give any errors.

csv file->
make sure you have a csv file before hand with the name pswrds.csv (the code can be modified to take in user imput for what csv file to search for or automatically start searching for a csv file in the directory).
