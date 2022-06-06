import torch
import numpy as np

# Create a tensor from data
data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)

# Create a tensor from NumPy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# Initialize tensor with random data
tensor = torch.rand(3,4)

# We move our tensor to the GPU if available
if torch.cuda.is_available():
    tensor = tensor.to("cuda")

# Print tensor attributes
print(f"Shape of tensor: {tensor.shape}")
print(f"Dimension of a tensor: {tensor.ndim}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

# Standard numpy-like indexing and slicing:
tensor1 = torch.ones(4, 4)
print(f"First row: {tensor1[0]}")
print(f"First column: {tensor1[:, 0]}")
print(f"Last column: {tensor1[..., -1]}")
tensor[:,1] = 0
print(tensor1)

# Concatenate tensors
t1 = torch.cat([tensor1, tensor1, tensor1], dim=1)
print(t1)

# Computes the matrix multiplication between two tensors. y1, y2, y3 will have the same value
y1 = tensor1 @ tensor1.T
y2 = tensor1.matmul(tensor1.T)

y3 = torch.rand_like(tensor1)
torch.matmul(tensor1, tensor1.T, out=y3)


# This computes the element-wise product. z1, z2, z3 will have the same value
z1 = tensor1 * tensor1
z2 = tensor1.mul(tensor1)

z3 = torch.rand_like(tensor1)
torch.mul(tensor1, tensor1, out=z3)

# Single-element tensors 
agg = tensor1.sum()
agg_item = agg.item()
print(agg_item, type(agg_item))

