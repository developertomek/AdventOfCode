import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

content = file[0]
content_arr = content.split(',')

sum_ids = 0


def split_word(word, char_range):
    return [word[i:i + char_range] for i in range(0, len(word), char_range)]


for ids in content_arr:
    l_str, r_str = ids.split('-')
    l,r = int(l_str.strip()), int(r_str.strip())

    for id in range(l, r + 1):
        len_id = len(str(id)) 
        is_true = False
        i = 1
        while i <= len_id // 2:
            words = split_word(str(id), i)
            is_true = all(word == words[0] for word in words)
            
            if is_true:
                sum_ids += id
                break
            i += 1

print(sum_ids)