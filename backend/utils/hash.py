# Code strongly inspired from: https://hackernoon.com/hashing-passwords-in-python-bcrypt-tutorial-with-examples-77dh36ef

import bcrypt


def hashPassword(password):
    pwdHashed = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
    return pwdHashed


def checkPassword(providedPassword, passwordHashed):
    return bcrypt.checkpw(providedPassword.encode("utf8"), passwordHashed.encode("utf8"))
