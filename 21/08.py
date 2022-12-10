def get_number(chars, cipher_dict):
    imm_len = {2: 1, 4: 4, 3: 7, 7: 8}
    if len(chars) in imm_len.keys():
         return imm_len[len(chars)]
    zero = [x for x in cipher_dict if x != cipher_dict[3]]
    two = [x for x in cipher_dict if x != cipher_dict[1] and x != cipher_dict[5]]
    three = [x for x in cipher_dict if x != cipher_dict[1] and x != cipher_dict[4]]
    five = [x for x in cipher_dict if x != cipher_dict[2] and x != cipher_dict[4]]
    six = [x for x in cipher_dict if x != cipher_dict[2]]
    nine = [x for x in cipher_dict if x != cipher_dict[4]]
    num_dict = {0: zero, 2: two, 3: three, 5: five, 6: six, 9: nine}
    return int([key for key, value in num_dict.items() if (sorted(list(chars)) == sorted(value))][0])


def decipher_digits(digits):
    decipher = [''] * 7
    # the only char of the 3 chars digit not in the two chars digit is the top 1
    decipher[0] = ''.join(list(set(digits[0]) ^ set(digits[1])))
    # The only char in the 4 digits and all the 5 digits is the middle horizontal one
    decipher[3] = ''.join(x for x in set.intersection(*map(set, [digits[2], digits[3], digits[4], digits[5]])))
    # The other of the 2 chars of the 4 char digits not in the 2 char digits is decipher[1]
    chars_dig4 = ''.join(list(set(digits[2]) ^ set(digits[0])))
    decipher[1] = chars_dig4[0] if decipher[3] != chars_dig4[0] else chars_dig4[1]
    # If the decipher[3] (middle horizontal char) is present in a 6 digits num but one of the
    # 2 chars number (digits[0]) is missing, it's num 6 and allows to confirm the missing one as decipher[2]
    # and the decipher[5] as not missing. Comparison between 0, 6 and 9. 0 and 9 have 1's digits. 6 doesn't.
    six_chars_nums = [digits[6], digits[7], digits[8]]
    mid_six_chars_nums = [x for x in six_chars_nums if decipher[3] in x]
    decipher[2] = ''.join([char for char in digits[0] if not all(char in elem for elem in mid_six_chars_nums)])
    decipher[5] = digits[0][0] if decipher[2] != digits[0][0] else digits[0][1]
    # The char that is in 6 chars nums but not in decipher is the bottom one
    decipher[6] = ''.join([x for x in set.intersection(*map(set, six_chars_nums)) if x not in decipher])
    # The last char (decipher[4]) is in the last digit but not in decipher.
    decipher[4] = ''.join(set(digits[9]) ^ set(decipher))
    return decipher


with open("08.txt") as entry:
    part1 = [0, 0, 0, 0]
    part2 = 0
    for line in entry.readlines():
        digits, cipher = [x.strip().split() for x in line.strip().split('|')]
        digits = sorted(digits, key=len)
        decipher = decipher_digits(digits)
        # Translate each string into a number
        num_str = "".join(map(str, [get_number(number, decipher) for number in cipher]))
        for i, num in enumerate(['1', '4', '7', '8']):
            part1[i] += num_str.count(num)
        part2 += int(num_str)
    print(f'Part 1: {sum(part1)}\nPart 2: {part2}')