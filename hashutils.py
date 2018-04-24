import hashlib   #the hash library
import random    
import string

def make_salt(): 
    # empty string. join a list with a random choice from acsii for 5 times.
    return ''.join([random.choice(string.ascii_letters) for x in range(5)])


def make_pw_hash(password, salt=None):
# take in the user typed information, or a check of previous. Salt defaults to none if not passed.
#the first time through we need to make the salt.     
    if not salt:
        salt = make_salt()
    #the hash itself, wants bytecode, pass both, when done .hexdi to turn back into a string
    hash = hashlib.sha256(str.encode(password + salt)).hexdigest()
    #keep both as a str with a comma , so you can check both separately
    return '{0},{1}'.format(hash, salt)

def check_pw_hash(password, hash): #hash here is not hash from above. Hash is the output of make_pw_hash
    #we are keeping a str with comma, split at comma, then give index 1 (salt)
    salt = hash.split(',')[1]
    #then we pass it back to make password, the way it should have been during the first encoding
    # meaning the output should be the same:
    if make_pw_hash(password, salt) == hash:
        return True

    return False







# How you check in the python main if they match.
#if user and check_pw_hash(password, user.pw_hash):