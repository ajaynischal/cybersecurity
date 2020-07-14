import hashlib
import binascii
import time
from itertools import permutations, combinations
import tkinter
import matplotlib as plt
from matplotlib import style


def read_file(filename):
    """ Reads in a file and returns a list with the contents
    @param filename: name of file being taken in
    @return: a list with all words in the dictionary file
    """
    dict_list = []
      
    with open(filename) as f:
        new_line = [line.strip('\n') for line in f]
        for item in new_line:
            dict_list.append(item)
          
    return dict_list

      
def hash_sha256(password):
    """ Hashes the user input to sha256
    @param password: the user inputted password
    @return: sha256 hashed password
    """
    hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 'saltPhrase'.encode('utf-8'), 100000)
    return binascii.hexlify(hashed_pw)

def hash_sha512(password):
    """ Hashes the user input to sha512
    @param password: the user inputted password
    @return: sha512 hashed password
    """
    
    hashed_pw = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 'saltPhrase'.encode('utf-8'), 100000)
    return binascii.hexlify(hashed_pw)

def dict_attack(dict_list, pw, hash_type):
    """ Implements a dictionary attack on the hashed password
    @param dict_list: the list of dictionary contents
    @param: pw: user inputted password
    @param: hash_type: the type of hash chosen to encrypt
    @return: returns a tuple with the number of guesses and true if found
    """
    
    perms = permutations(dict_list)
    
    hashed_result = ''
    result = ''
    is_found = False
    found = ''
    guess_count = 0
    
    for perm in perms:
        result = ''
        for element in perm:
            result += str(element)
            if hash_type == "sha256":
                hashed_pw = hash_sha256(pw)
                hashed_result = hash_sha256(result)
                print("Currently Searching")
            elif hash_type == "sha512":
                hashed_pw = hash_sha512(pw)
                hashed_result = hash_sha512(result)
                print("Currently Searching")

            guess_count += 1
            if hashed_result == hashed_pw:
                is_found = True
                found = str(result)
                if is_found:
                    print("Found match: " + str(found) + " in " + str(guess_count) + " guesses")
                    return guess_count, is_found
                else:
                    print("Not Found")
                    
              
            

def graph(hash_type, dict_list, guess_time, start_time, num_guess):
    dict_size = len(dict_list)
    
    root = tkinter.Tk()
    root.title("Dictionary Attack on SHA" + str())
    root.configure(width = 500, height = 300, background = 'lightyellow')
    
    label = tkinter.Label(root, text = 'Dictionary Attack')
    label2 = tkinter.Label(root, text = "Hash Type is: " + hash_type)
    label3 = tkinter.Label(root, text = "Dictionary size is: " + str(dict_size))
    label.pack()
    label2.pack()
    label3.pack()
    plt.plot(start_time, num_guess)
    plt.plot(guess_time, num_guess)
    plt.xlabel("Run Time")
    plt.ylabel("Number of Guesses")

    plt.show()
     
    root.mainloop()

    return 0
        
def main():
    
    dict_list = read_file("Dictionary.txt")
    hash_type = input("Please input hash type: ")
    pw = input("Please input pw: ")
    
    # start time for guess time
    start_time = time.time()
    # returns number of guess and true if found in a tuple (guess, found)
    attack_list = dict_attack(dict_list, pw, hash_type)
    #take first element from attack_list tuple for number of guesses
    num_guess = attack_list[0]
    # end time for guess time after dictionary attack
    end_time = time.time()
    guess_time = end_time - start_time
    print("Time elapsed: " + str(guess_time) + " seconds.")
    
    # Start of the graphing 
    graph(hash_type, dict_list, guess_time, start_time, num_guess)

    
    
if __name__ ==  "__main__":
    main()
