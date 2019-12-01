BANNED_CHARS = set(['i', 'o', 'l'])

def increasing_straight(password):
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2:
            return True

    return False

def no_banned_chars(password):
    global BANNED_CHARS

    for char in password:
        if char in BANNED_CHARS:
            return False

    return True

def two_nonoverlapping_pairs(password):
    overlapping = []

    for i in range(len(password) - 1):
        if password[i] == password[i+1] and password[i] not in overlapping:
            overlapping.append(password[i])
            if len(overlapping) == 2:
                return True

    return False

def is_good_password(password):
    return increasing_straight(password) and no_banned_chars(password) and two_nonoverlapping_pairs(password)

def increment_password(password):
    first_non_z = len(password) - 1

    while password[first_non_z] == 'z':
        if first_non_z == 0:
            return 'a'*len(password)
        first_non_z -= 1

    new_password = password[:first_non_z]
    new_password += chr(ord(password[first_non_z]) + 1)
    new_password += 'a'*(len(password) - 1 - first_non_z)

    return new_password

def get_next_password(password):
    password = increment_password(password)

    while not is_good_password(password):
        password = increment_password(password)

    return password

def main():
    result = get_next_password("hxbxwxba")
    #part 1
    print(result)

    result = get_next_password(result)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
