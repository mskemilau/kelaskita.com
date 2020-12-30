def sentence_reversing(sentence):
    str_list = sentence.split()
    for index in range(len(str_list)):
        str_list[index] = str_list[index][::-1]
    return " ".join(str_list)


sentence_list = "italem irad irigayaj\n" \
                "iadab itsap ulalreb\n" \
                "nalub kusutret gnalali"

for sente in sentence_list.splitlines():
    print(sentence_reversing(sente))