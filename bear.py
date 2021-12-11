import os
path = "GGPoker"
names = []
for file in os.listdir(path):
    file_path = os.path.join(file)
    if os.path.splitext(file_path)[1] == '.txt':
        names.append(file_path)

for name in names:
    with open("GGPoker/"+name, 'r',encoding='utf-8') as file:
        lines = file.readlines()
        length = len(lines)
        i = 0
        while(i<length):
            if i == len(lines):
                break
            if lines[i] == "\n":
                i=i+1
                continue
            if lines[i][0] == u"P" and lines[i].split('#')[0] == u'Poker Hand ':
                lines[i] = u"PokerStars Zoom Hand #" + lines[i].split('#')[1][2:]


            if u"Dealt" in lines[i] and u'Hero' not in lines[i]:
                # print(lines[i])
                del lines[i]
                i=i-1

            # if u"SHOWDOWN" in lines[i]:
            #     del lines[i]
            #     i = i-1
                # del lines[i+1]
                # i = i-1

            # if u"SUMMARY" in lines[i]:
            #     lines[i+1] = lines[i+1][:-1] + " | Rake $0\n"
            i= i+1

    # for i in range(len(lines)):
    #     print(lines[i])

    with open("PokerStars/"+name ,'w',encoding='utf-8') as file:
        file.writelines(lines)