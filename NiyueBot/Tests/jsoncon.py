import json

# Чтение первого JSON файла
with open('Z:\DiscordBot\messages2.json', 'r', encoding="utf-8") as f1:
    data1 = json.load(f1)

# Чтение второго JSON файла
with open('Z:\DiscordBot\mes2.json', 'r', encoding="utf-8") as f2:
    data2 = json.load(f2)


merged_data = {**data1, **data2}


with open('Z:\DiscordBot\messages3.json', 'w') as f:
    json.dump(merged_data, f)