import os
import glob

# datas = glob.glob(r'/home/yangna/deepblue/OCR/EAST2/ICDAR_2015/ch4_training_localization_transcription_gt/*.txt')
path = os.environ.get('TRAIN_TXT', 'D:/DocumentAI/SinhalaOCR/train_1.txt')
alphabet = []

with open(path) as f:
    perdata = f.readlines()

for pd in perdata:
    pd = pd.rstrip().split()
    alphabet += pd[-1]

temp = ''.join(set(alphabet))

with open('baidu_alphabet.txt', 'w') as outf:
    outf.write(temp)