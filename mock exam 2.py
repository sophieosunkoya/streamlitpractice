
#sum3=0
#sum4=0


#the_list = [496, 323, 1290, 3704, 3669, 3302, 3691, 3786, 1099, 2063, 1601, 1284, 1127, 1127, 1067, 2632, 1551, 2378, 2521, 1880, 179, 1005, 531, 1514, 695, 2749, 3813, 1108, 1270, 2242, 880, 646, 852, 2557, 186, 1507, 547, 3608, 1965, 1092, 2894, 1702, 1385, 3606, 2573, 2328, 104, 434, 636, 2471, 3491, 2197, 3411, 1686, 2523, 599, 967, 787, 3422, 3369, 2799, 1068, 2728, 2791, 2107, 2373, 3372, 3180, 2627, 2146, 1317, 1328, 2602, 3802, 3406, 1447, 3003, 2827, 1435, 2465, 3014, 2559, 547, 1235, 2401, 3366, 3246, 1198, 2711, 1073, 953, 2880, 328, 2780, 3679, 1385, 1055, 1466, 671, 374, 2316, 2774, 2595, 2768, 3320, 244, 1944, 101, 1369, 3289, 267, 2525, 3153, 390, 1576, 2302, 156, 2751, 1711, 1756, 1039, 2736, 368, 2495, 2658, 2939, 96, 1774, 1137, 2400, 3202, 1356, 3275, 3663, 3265, 3782, 3309, 1970, 1409, 45, 1441, 1560, 2438, 795, 1591, 323, 121, 896, 2627, 2283, 1426, 1819, 484, 1953, 3369, 2058, 198, 665, 3804, 3374, 3169, 1516, 1139, 2987, 487, 2557, 738, 2419, 2037, 3262, 974, 691, 2709, 2886, 2405, 836, 1837, 1749, 1734, 3003, 3208, 1568, 3274, 3339, 1008, 1644, 3414, 1720, 2106, 3507, 2780, 2686, 1171, 1943, 1112, 2167, 300, 95, 579, 1454]
#for value in the_list:
    #if value%3==0:
        #sum3+=value
    #if value%4==0:
        #sum4+=value


#print(sum3)
#print(sum4)
#rint(sum3+sum4)

#my_dict = {'HH': 742, 'R': 504, 'VVV': 2690, 's': 44, 'YY': 3988, 'ppp': 4441, 'Y': 4059, 'KKKK': 979, 'BBBBB': 3780, 'mmmm': 2850, 'b': 3028, 'HHHH': 1581, 'PPPPP': 3493, 'jjjj': 4402, 'J': 3466, 'rrrrr': 4226, 'W': 2419, 'TT': 2247, 'RRRR': 3783, 'ZZZ': 3787, 'xxxx': 1831, 'bbbbb': 26, 'cc': 325, 'QQQQQ': 4547, 'c': 2776, 'WWW': 3964, 'kk': 2686, 'CCCC': 3355, 'bbb': 287, 'jjj': 3657, 'C': 1398, 'dddd': 4531, 'pppp': 4227, 'TTT': 4528, 'tt': 1432, 'yyyy': 4654, 'XXX': 619, 'r': 1250, 'ssss': 4556, 'FF': 149, 'ww': 2840, 'HHH': 2615, 'MM': 3741, 'mm': 1286, 'RRR': 237, 'q': 4546, 'VV': 2074, 'mmmmm': 3295, 'sssss': 3694, 'ttttt': 1101, 'yyy': 1074, 'kkkk': 68, 'KKKKK': 2220, 'LL': 842, 'JJ': 2156, 'SSS': 899, 'S': 393, 'CCC': 191, 'ttt': 2973, 'ZZZZZ': 1527, 'VVVV': 3779, 'hhhhh': 967, 'PP': 2759, 'QQQ': 2189, 'qqqqq': 3415, 'YYYY': 1431, 'DDDDD': 2143, 'YYYYY': 4640, 'LLLLL': 1614, 'LLLL': 3260, 'kkk': 1644, 'tttt': 4042, 'YYY': 735, 'K': 3155, 'DD': 3845, 'WWWWW': 4009, 'PPP': 4484, 'rrrr': 1004, 'FFFFF': 3457, 'TTTTT': 1377, 'JJJ': 912, 'D': 1658, 'DDD': 3322, 'BBBB': 2433, 'ccccc': 2651, 'cccc': 1594, 'hh': 607, 'ddddd': 2372, 'XXXXX': 1234, 'M': 2691, 'ZZZZ':
            #3665, 'PPPP': 1474, 'ss': 3361, 'jj': 2587, 'fff': 1883, 'www': 390, 'vvvvv': 2382, 'wwwww': 1553, 'MMMM': 69, 'wwww': 1906}


#total = 0

# loop through all the keys in the dictionary
#for key in my_dict:
  # find the number of characters in the key
  #key_length = len(key)
  
  # if the number of characters is odd, add the corresponding value to the running total
  #if key_length % 2 == 1:
    #total += my_dict[key]

#print(total)
def is_armstrong(n):
  # Convert the number to a string and get the number of digits
  num_str = str(n)
  num_digits = len(num_str)

  # Calculate the sum of the digits raised to the power of the number of digits
  sum = 0
  for digit in num_str:
    sum += int(digit) ** num_digits

  # Return True if the sum is equal to the original number, otherwise False
  return sum == n

# Start with the largest possible number of digits and work our way down
for num_digits in range(6, 0, -1):
  # Calculate the maximum number with the current number of digits
  max_num = int('9' * num_digits)

  # Check each number in descending order to find the largest Armstrong number
  for n in range(max_num, 0, -1):
    if is_armstrong(n):
      print(n)
      break
#print(is_armstrong(1000000))
