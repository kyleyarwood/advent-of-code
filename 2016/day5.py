from hashlib import md5

inp = 'cxdnnyjw'

def get_password(door_id, num_zeroes=5):
    prefix = '0'*num_zeroes
    i = 0
    password = []
    new_password, to_fill = list(range(8)), set(range(8))
    while to_fill:
        my_hash = md5((door_id + str(i)).encode()).hexdigest()
        while my_hash[:num_zeroes]!=prefix:
            i += 1
            my_hash = md5((door_id + str(i)).encode()).hexdigest()
        print(my_hash)
        if len(password) < 8:
            password.append(my_hash[num_zeroes])
        posn = my_hash[num_zeroes]
        if '0' <= posn < '8':
            posn = int(posn)
            if posn in to_fill:
                to_fill.remove(posn)
                new_password[posn] = my_hash[num_zeroes+1]
        i += 1
    return ''.join(password), ''.join(new_password)

pw = get_password(inp)
print(pw)

