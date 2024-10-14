import torch

# Get the total number of GPUs available
num_gpus = torch.cuda.device_count()
print("Number of available GPUs:", num_gpus)

# Ens