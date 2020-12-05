from file_lines import get_file_lines

def num_valid_passports(passports):
	REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	OPTIONAL = ['cid']
	print(passports)
	return sum(all(r in passport for r in REQUIRED) for passport in passports)


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
