import torch 
import torch.nn as nn



class FeedforwardNeuralNetModel(nn.Module):
    def __init__(self, layers): 
        super(FeedforwardNeuralNetModel, self).__init__()
        self.fc=nn.ModuleList()
        self.sigmoid=nn.ModuleList()
        self.activationValue = 
        self.layers = layers
        for i in range(len(layers)-1):
            self.fc.append(nn.Linear(layers[i],layers[i+1]))
            self.sigmoid.append(nn.Sigmoid())

    def forward(self, x):

        for i in range(len(self.fc)):
            out=self.fc[i](out)
            out = self.sigmoid[i](out)
        return out    