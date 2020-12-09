from file_lines import get_file_lines

def byr(s):
    return len(s)==4 and 1920 <= int(s) <= 2002

def iyr(s):
    return len(s)==4 and 2010 <= int(s) <= 2020

def eyr(s):
    return len(s)==4 and 2020 <= int(s) <= 2030

def hgt(s):
    mn, mx = 59, 76
    if s[-2:] == 'cm':
        mn, mx = 150, 193
    return mn <= int(s[:-2]) <= mx

def hcl(s):
    hex = list(map(str, range(10))) + ['a','b','c','d','e','f']
    return len(s)==7 and s[0]=='#' and all(c in hex for c in s[1:])

def ecl(s):
    colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return s in colours

def pid(s):
    return len(s)==9 and all(c in map(str, range(10)) for c in s)

valid_fns = {'byr': byr, 'iyr': iyr, 'eyr': eyr, 'hgt': hgt, 'hcl': hcl,
            'ecl': ecl, 'pid': pid}

def num_valid_passports(passports):
    REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    OPTIONAL = ['cid']
    print(passports)
    return sum(all(r in passport and valid_fns[r](passport[r]) for r in REQUIRED) for passport in passports)


def get_passports(inp):
    passports = []
    curr_passport = {}
    for line in inp:
        if line == '':
            passports.append(curr_passport)
            curr_passport = {}
            continue
        for kvp in line.split():
            key,val = kvp.split(':')
            curr_passport[key] = val
    passports.append(curr_passport)
    return passports

def main():
    inp = [line.strip() for line in get_file_lines('day4.in')]
    result = num_valid_passports(get_passports(inp))
    print(result)

if __name__ == "__main__":
    main()
