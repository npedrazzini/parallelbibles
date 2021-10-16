import pandas as pd
langs = ["eng", "deu", "rus","bul"]
sent_id1 = ["eww","weev","vvvrgv"]
sent_id2 = ["eeee","w333eev","4"]
sent_id3 = ["f","wer2fev","vvvr4gv"]

listofdic = {}
listofdic["sent_id"] = []


for lang in langs:
    listofdic['{}'.format(lang)] = []
for id in sent_id1:
    listofdic["sent_id"].append(id)
for lang in langs:
    listofdic['{}'.format(lang)].append('caracaracara')
    listofdic['{}'.format(lang)].append('caracaracara')
    listofdic['{}'.format(lang)].append('caracaracara')
for id in sent_id2:
    listofdic["sent_id"].append(id)
for lang in langs:

    listofdic['{}'.format(lang)].append('piripiri')
    listofdic['{}'.format(lang)].append('caracaracara')
    listofdic['{}'.format(lang)].append('caracaracara')

for id in sent_id3:
    listofdic["sent_id"].append(id)
for lang in langs:
    listofdic['{}'.format(lang)].append('ddddd')
    listofdic['{}'.format(lang)].append('caracaracara')
    listofdic['{}'.format(lang)].append('caracaracara')

print(listofdic)
for i in listofdic:
    print(i)
    print(len(i))
df = pd.DataFrame(listofdic)
df.to_csv('trial.csv')