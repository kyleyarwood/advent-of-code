from file_lines import get_file_lines

lines = get_file_lines('day10.in')

jolts = [int(line) for line in lines]
jolts.sort()

def get_result(jolts):
    num_1, num_3 = 0, 1
    prev = 0
    for jolt in jolts:
        if jolt - prev == 3:
            num_3 += 1
        elif jolt - prev == 1:
            num_1 += 1
        prev = jolt
    return num_1, num_3

def get_resultb(jolts,dp,i=0):
    if i not in dp:
        j = i+1
        result = 0
        while j < len(jolts) and j <= i+3:
            if jolts[j]-jolts[i]<=3:
                result += get_resultb(jolts,dp,j)
            j += 1
        dp[i] = result
    return dp[i]

r = get_result(jolts)
print(r)

dp = {len(jolts)-1: 1}
r = get_resultb(jolts, dp)
if jolts[1]<=3:
    r += get_resultb(jolts, dp, 1)
if jolts[2]<=3:
    r += get_resultb(jolts, dp, 2)
print(r)
