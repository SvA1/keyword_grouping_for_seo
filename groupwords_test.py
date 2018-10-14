import re


def groups_function(filename):
   res_list = []
   for word in filename.readlines():
       work_list = word.strip().split(":")
       res_list.append([work_list[0], work_list[1].strip().split(",") ])
   return res_list


filename_group = "groups"

file_group_source = open( filename_group + ".txt")
group_tuple = groups_function(file_group_source)

filename_word = "words"
file_word_source = open( filename_word + ".txt")
file_res = open( filename_word +"2.txt", "w")

for word in file_word_source.readlines():
    res = []
    str = word.strip()
    for w in str.split():
        for gr_word in group_tuple:
            for g_word in gr_word[1]:
                if re.match(g_word.strip().lower(), w.lower()):
                    res.append(gr_word[0])

    res = list(set(res))
    res_str = ",".join(res)
    file_res.writelines(word.strip() + "|" + res_str + "\n")

    print ("Файл" + filename_word + "2.txt сформирован в исходной директории")