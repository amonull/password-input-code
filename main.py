import cryptography.fernet as fernet
import csv
import pandas as pd
import pathlib
import sys
from sys import platform
import warnings

class encryption(): #encrypt and dcrypt
    #probaly doesnt need this section of code to run on linux or windows as python can work with both \ and / so paths are compatible on both systems. only reason to add this is to for learning purposes
    #checks if computer is using linux or windows or another os
    def find_path(self, file_name):
        raw_path = pathlib.Path(__file__).parent.absolute()#gets the path of current directory
        if platform == "linux" or platform == "linux2":
            file_path = pathlib.PurePosixPath(raw_path)
            file_name = f"/{file_name}"
        elif platform == "win32":
            file_path = pathlib.PureWindowsPath(raw_path)
            file_name = f"\{file_name}"
        else:
            sys.exit("your operating system is not compatible. use linux or windows.")
        return f"{file_path}{file_name}"
    
    #only run this function if you do not already have a key you wish to load.
    def key_generation(self):
        key = fernet.generate_key()

    def open_key(self):
        path_of_file = self.find_path('key.key')
        with open(f"{path_of_file}", "rb") as filekey:
            key = filekey.read()
            f = fernet.Fernet(key)
            return f
    
    def encrypt(self):
        encryption_key = self.open_key()
        path_of_file = self.find_path('pswrds.csv')
        with open(f"{path_of_file}", "rb") as file:
            original = file.read()
        encrypted = encryption_key.encrypt(original)
        with open(f"{path_of_file}", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt(self):
        decryption_key = self.open_key()
        path_of_file = self.find_path('pswrds.csv')
        with open(f"{path_of_file}", "rb") as encrypted_file:
            encrypted = encrypted_file.read()
        decrypted = decryption_key.decrypt(encrypted)
        with open(f"{path_of_file}", "wb") as decrypted_file:
            decrypted_file.write(decrypted)

class app(encryption):
    enc = encryption()
    file_path = enc.find_path('pswrds.csv')

    try:
        enc.decrypt() #if file is not encrypted it will throw an error which is why we need a try except here
    except fernet.InvalidToken:
        print("already decrypted\n")

    csv_df = pd.read_csv(f'{file_path}', names=('SITE', 'USERNAME', 'PASSWORDS'))

    def view_file(self):
        print(f"\n{self.csv_df}\n")

    def check_if_exist(self, col, value):
        if (self.csv_df[col] == value).any():
            return True
        else:
            return False

    def search(self, column, value):
        if self.check_if_exist(column, value) == True:
            index_num = self.csv_df.index[self.csv_df[column]==value].tolist()
            print(f"{self.csv_df.iloc[index_num]}\n")
        else:
            print("this value does not exist.\n")

    def append(self, **field):
        #tell user to leave section blank if they want it to not enter it in
        data = [field['SITE'], field['USERNAME'], field['PASSWORDS']]
        pswrds_file = open(f'{self.file_path}', 'a', newline='')
        appending = csv.writer(pswrds_file)
        appending.writerow(data)
        print("Data Appended\n") #ERRORS data appended when showing from view data will be one cycle late as csv_df doesnt get updated within the append cycle
        self.csv_df

    #if delete code now doesnt work it is because of warning labled below that has been SUPPRESSED but not fixed
    def delete(self, *del_item): #ERRORS(FUTURE_WARNING)FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
        try:
            warnings.simplefilter(action='ignore', category=FutureWarning)
            self.csv_df = self.csv_df.drop(self.csv_df.index[[*del_item]])#removing the second [] around index for *args does not fix the issue but creates more. it needs second [] to work properly
            print(f"{self.csv_df}\nHow The File Will Look After Deleting")
            if input("Are you sure you want to delete this data y/n: ").lower() == "y":
                self.csv_df.to_csv(f'{self.file_path}', header=False, index=False)
                print("\nFile Changed\n")
            else:
                print("\nFile Not Changed\n")
        except IndexError:
            print("\nERROR:\nthe file may not have refreshed try veiwing file which should refresh it. if that doesnt work use index number one smaller\n")

    def edit(self, index, col, change): #the {iat[index, col] = change} can be put inside a {while != 3} loop so that i can iterate through all columns and if user leaves it empty it can just stay as it is this will allow the user to not input the column name.
        try:
            int_index = int(index)
        except ValueError:
            print("wrong INDEX number")
        else:
            if col == 'SITE':
                col = 0
            elif col == 'USERNAME':
                col = 1
            elif col == 'PASSWORDS':
                col = 2
            else:
                print("this column does not exist or is misspelled.")
                return
            self.csv_df.iat[int_index,col] = change #index and col have to be in number format index works as usual and col is SITE=0 USERNAME=1 PASSWORDS=2
            print(f"\n{self.csv_df}\nThis Is What It Will Look Like After.")
            if input("\nDo You Wish To Save y/n: ").lower() == "y":
                self.csv_df.to_csv(f'{self.file_path}', header=False, index=False)
                print("\nFile Changed\n")
            else:
                print("\nFile Not Changed\n")

    def shut_down(self):
        self.enc.encrypt()
        sys.exit("\nfile encrypted.\nany changes not saved when specified will not be saved.")

app = app()