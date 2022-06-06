import torch
#Test PyTorch installation
x = torch.rand(5, 3)
print(x)

#Check if CUDA is available
print("CUDA available - ", torch.cuda.is_available())