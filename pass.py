# password manager
print("WELCOME to Shubham's Password management System")
import random
import string
import array
def store_password():
    # username
    username = str(input("Your username: "))
    # website
    website = str(input("Website: "))
    # generate randome password
    i = int(input("How many digit password you want :- "))
    MLEN = i

# declare arrays of the character that we need in out password

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LCHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UCHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UCHARACTERS + LCHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rdigit = random.choice(DIGITS)
    rupper = random.choice(UPCASE_CHARACTERS)
    rlower = random.choice(LOCASE_CHARACTERS)
    rsymbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rdigit + rupper + rlower + rsymbol


    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MLEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
            password = password + x

    # print password
    print(password)
    f = open("Password.txt", "a")
    f.write(f"{username}-{website}-{str(password)}\n")
    f.close()

    print(f"here's your password: {password}")
####
def search():
    username_or_website = str(input("Do you want to search for a username or website ? "))
    value = str(input("What Value ? "))
    f = open("Password.txt", "r")
    for line in f:
        info = line.split("-")
        if username_or_website == "username":
            if value == info[0]:
                return info[2]
        # search by username
        else:
        # search by website
            if value == info[1]:
                return info[2]
i = int(input("For creating password enter 1 /n for searching password enter 2 :-> "))
if i == 1:
    store_password()
else:
    print(search())
