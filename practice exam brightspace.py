
#numbers=[496, 323, 1290, 3704, 3669, 3302, 3691, 3786, 1099, 2063, 1601, 1284, 1127, 1127, 1067, 2632, 1551, 2378, 2521, 1880, 179, 1005, 531, 1514, 695, 2749, 3813, 1108, 1270, 2242, 880, 646, 852, 2557, 186, 1507, 547, 3608, 1965, 1092, 2894, 1702, 1385, 3606, 2573, 2328, 104, 434, 636, 2471, 3491, 2197, 3411, 1686, 2523, 599, 967, 787, 3422, 3369, 2799, 1068, 2728, 2791, 2107, 2373, 3372, 3180, 2627, 2146, 1317, 1328, 2602, 3802, 3406, 1447, 3003, 2827, 1435, 2465, 3014, 2559, 547, 1235, 2401, 3366, 3246, 1198, 2711, 1073, 953, 2880, 328, 2780, 3679, 1385, 1055, 1466, 671, 374, 2316, 2774, 2595, 2768, 3320, 244, 1944, 101, 1369, 3289, 267, 2525, 3153, 390, 1576, 2302, 156, 2751, 1711, 1756, 1039, 2736, 368, 2495, 2658, 2939, 96, 1774, 1137, 2400, 3202, 1356, 3275, 3663, 3265, 3782, 3309, 1970, 1409, 45, 1441, 1560, 2438, 795, 1591, 323, 121, 896, 2627, 2283, 1426, 1819, 484, 1953, 3369, 2058, 198, 665, 3804, 3374, 3169, 1516, 1139, 2987, 487, 2557, 738, 2419, 2037, 3262, 974, 691, 2709, 2886, 2405, 836, 1837, 1749, 1734, 3003, 3208, 1568, 3274, 3339, 1008, 1644, 3414, 1720,
#2106, 3507, 2780, 2686, 1171, 1943, 1112, 2167, 300, 95, 579, 1454]

#def sum_divisible_by_3_or_4(numbers):
    # Initialize the total to 0
    #total = 0
    
    # Iterate over the list of numbers
    #for number in numbers:
        # If the number is divisible by either 3 or 4, add it to the total
        #if number % 3 == 0 or number % 4 == 0:
            #total += number
    
    # Return the total
    #return total
#print(sum_divisible_by_3_or_4(numbers))
import urllib.request

def cleanup_data_string(string):
    word = string.lower()
    output = ""
    for i in range(len(word)):
        if word[i] == "\n":
            if word[i+1] == "\n":
                continue
            else:
                output += " "
        if word[i] == "-":
            output += " "
        elif word[i].isalnum() or word[i] == " " :
            output += word[i]
    return output

# Get the text from the URL

url=('https://002-text-files.glitch.me/manifesto.txt')
response = urllib.request.urlopen(url)
text=response.read().decode("utf-8")

# Clean up the text and split it into a list of words
cleaned_text = cleanup_data_string(text)
words = cleaned_text.split()

# Find the list of every word that comes before each instance of the word "class" (case-insensitive)
class_indices = [i for i, word in enumerate(words) if word.lower() == 'class']
preceding_words = [words[i-1] for i in class_indices]
print(f'Words before each instance of "class": {preceding_words}')

# Find the 3950th word in the chapter
print(f'3950th word: {words[3949]}')

# Find the total number of words that each only appear 3 times in the text
from collections import Counter
word_counts = Counter(words)
num_words_appearing_3_times = sum(1 for count in word_counts.values() if count == 3)
print(f'Number of words appearing 3 times: {num_words_appearing_3_times}')
