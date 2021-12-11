import os
from tqdm import tqdm
from Num2Roman import Num2Roman
path = "GGPoker/"
names = []
for file in os.listdir(path):
    file_path = os.path.join(file)
    if os.path.splitext(file_path)[1] == '.txt':
        names.append(file_path)

for name in tqdm(names):
    with open(path+name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        write_lines = []
        length = len(lines)
        for i in range(length):
            if lines[i] == "\n":
                write_lines.append(lines[i])
                continue
            if lines[i].split('#')[0] == u'Poker Hand ':
                if "Tournament" in lines[i]:
                    before_tournament = lines[i].split('Tournament')[0]
                    hand_id = before_tournament.split("#")[1][2:]
                    after_tournament = lines[i].split('Tournament')[1]
                    after_level = after_tournament.split("Level")[1]
                    level = after_level.split("(")[0]
                    roman_level = Num2Roman(int(level))
                    after_tournament_roman = after_tournament.replace(level, roman_level)
                    lines[i] = u"PokerStars Hand #20" + hand_id + "Tournament" + after_tournament_roman
                    # print(lines[i])
                    pass
                else:
                    # cash game
                    lines[i] = u"PokerStars Hand #20" + lines[i].split('#')[1][2:]
                # print(lines[i])
                write_lines.append(lines[i])
                continue
            if u"Dealt" in lines[i] and u'Hero' not in lines[i]:
                continue
            else:
                write_lines.append(lines[i])
                continue
            write_lines.append(lines[i])
    with open("PokerStars/"+name, 'w', encoding='utf-8') as file:
        file.writelines(write_lines)