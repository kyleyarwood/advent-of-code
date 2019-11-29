import hashlib

def get_first_md5_hash_with_n_leading_zeroes(key, n):
    result = "1"*n
    n_zeroes = "0"*n
    i = 0

    while len(result) >= n and result[:n] != n_zeroes:
        i += 1
        result = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()

    return i


def main():
    key = "yzbqklnj"

    result = get_first_md5_hash_with_n_leading_zeroes(key, 5)
    #part 1
    print(result)

    result = get_first_md5_hash_with_n_leading_zeroes(key, 6)
    #part 2
    print(result)

if __name__ == "__main__":
    main()
