import torch

tensor = torch.rand(size=(2, 3, 4))

print(tensor.size())
print(tensor.size(0))
print(tensor.size(1))
print(tensor.size(2))
print('==')
print(tensor)
print(tensor.shape)
print('-')
print(tensor[0])
print(tensor[0].shape)
print('-')
print(tensor[1][2])
print(tensor[1][2].shape)
print('-')
print(tensor[0][1][3])
print(tensor[0][1][3].shape)