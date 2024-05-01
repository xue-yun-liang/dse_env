import yaml
import torch

def read_config(filename):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    

def sample_index_from_2d_array(array):
    sampled_indices = []
    for sub_array in array:
        probabilities = torch.tensor(sub_array, dtype=torch.float)
        probabilities /= torch.sum(probabilities)  # softmax
        sampled_index = torch.multinomial(probabilities, 1).item()  # sample using multinomial
        sampled_indices.append(sampled_index)
    return sampled_indices