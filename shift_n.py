info = '''
    Jun 21, 2017 Wed [07:37 AM](GMT+5:45)
    @author Swornim Shrestha <srestaswrnm@gmail.com>

    Flash back:

    Aabartan Dhakal on June 19 at 7:01 PM posted on facebook and hash tagged 
    #ShiftThrice. 
    I knew he wants us to shift the alphabet thrice, and I was so lazy to do that. I wanted to know what he wanted to say.
    So now I am writing this python code.

    Hope this will help you
    If there is any problem feel free to mail me.

    and Please use python 3.*
''' 
alphabets = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
print(info)

def encrypt():
    encrypted = ""
    print("Enter the what you want to ecrypt")
    raw = input(">").lower()
    for r in raw:
        for index, alphabet in enumerate(alphabets) :
            if alphabet == r:
                index_new = index+3
                
                if index_new > 25 :
                   index_new -= index_new - 25 

                encrypted += alphabets[index_new]
            
        if r not in alphabets:
                encrypted += r
            
    print(encrypted)

def decrypt():
    decrypted = ""
    print("Enter the what you want to decrypt")
    hashed = input(">").lower()
    
    for h in hashed:
        for index, alphabet in enumerate(alphabets) :
            if alphabet == h:
                index_new = index -3
                
                if index_new < 0 :
                   index_new -= index_new + 2 

                decrypted += alphabets[index_new]
            
        if h not in alphabets:
                decrypted += h
            
    print(decrypted)


def main():
    print("Do you want to encrypt or decrypt?")
    job = input("\n>")
   
    if str(job).upper() == "ENCRYPT":
        encrypt()
    elif str(job).upper() == "DECRYPT":
        decrypt()
    else:
        main()

if __name__ == "__main__":
    main()
