import pickle
file_name = "./dataset/birds/text/char-CNN-RNN-embeddings1.pickle"

data = []
with open(file_name, 'rb') as f:
    x = pickle.load(f, encoding='bytes')
print("nhap so:")
n = int(input())

print(x[10])
# gg = open('./input/input6.pickle','wb')
# pickle.dump(x[n:n+3],gg)
# gg.close()