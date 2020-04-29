#Code strongly inspired from: https://hackernoon.com/hashing-passwords-in-python-bcrypt-tutorial-with-examples-77dh36ef

import bcrypt

def hashPassword(password):
    pwdHashed = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
    return pwdHashed

if __name__ == "__main__":
    pdw = input("pwd")
    print(hashPassword(pdw))

