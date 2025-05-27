# This code creates an instance of the neural network with two fully connected layers, 
# defines the loss function (a measure of the model's prediction error) 
# as cross-entropy (a loss function commonly used for classification tasks), 
# and the optimizer (an algorithm that adjusts the model's parameters to minimize the loss) 
# as stochastic gradient descent (a popular optimization algorithm). 

# The code then performs a forward pass (computes the model's output) 
# to obtain the model's output, calculates the loss based on the output and target class, 
# performs a backward pass (computes gradients of the loss with respect to the model's parameters) 
# to compute gradients, updates the model's parameters using the optimizer, 
# and finally prints the updated model parameters and the loss value.

# The output displays the updated model parameters after performing a single training iteration. 
# It prints the names and values of the model's parameters that were updated 
# during the backward pass (calculating gradients for the model's parameters) 
# and optimizer step (updating the model's parameters using the gradients 
# and the chosen optimization algorithm). 

# The values represent the updated weights (parameters that adjust the strength of connections 
# between neurons) and biases (parameters that adjust the neuron activation thresholds) 
# of the neural network's layers.

# Install necessary libraries
import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(10, 5)  # First fully connected layer
        self.fc2 = nn.Linear(5, 2)    # Second fully connected layer
        # Defines a linear layer that transforms input data from 10 features to 20 features
        self.fc1 = nn.Linear(10, 20)
        # Defines a linear layer that transforms data from 20 features to 2 output classes
        self.fc2 = nn.Linear(20, 2)

        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))   # Activation function for first layer
        x = self.fc2(x)                # Output layer
        return x
    
# Create an instance of the neural network model
model = NeuralNetwork()

# Define a loss function (cross-entropy loss for classification)
criterion = nn.CrossEntropyLoss()

# Define an optimizer (stochastic gradient descent)
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy input and target for demonstration
input_data = torch.randn(1, 10)  # Random input tensor of shape (1, 10)
output = model(input_data)  # Forward pass to get model output

# Perform a backward pass and update the weights
optimizer.zero_grad()  # Zero the gradients before backward pass
loss = criterion(output, torch.tensor([1]))  # Calculate loss with target class
loss.backward()  # Backward pass to compute gradients
optimizer.step()  # Update model parameters using the optimizer

# Print updated model parameters and loss
print("Updated model parameters:")
for name, param in model.named_parameters():
    if param.requires_grad:  # Only print parameters that require gradients
        print(f"{name}: {param.data}")

print(f"Loss: {loss.item()}")  # Print the loss value


# New function to calculate accuracy
def calculate_accuracy(output, target):
    """Calculate accuracy of the model's predictions."""
    _, predicted = torch.max(output, 1)  # Get the index of the max log-probability
    correct = (predicted == target).sum().item()  # Count correct predictions
    accuracy = correct / target.size(0)  # Calculate accuracy
    return accuracy

# Calculate and print accuracy
target = torch.tensor([10])  # Assuming the target class is 10
accuracy = calculate_accuracy(output, target)
print(f"Accuracy: {accuracy * 100:.2f}%")  # Print accuracy as a percentage


# Train the model more because the model is not trained enough and yields a 0.00% accuracy

# Add more data points
input_data = torch.randn(10, 10) # 10 samples, 10 features
target = torch.randint(0, 2, (10,)) # 10 class labels (0 or 1)

# Run a training loop for multiple epochs
for epoch in range(100):  # Train for 100 epochs
    optimizer.zero_grad() # Zero the gradients before each epoch
    output = model(input_data) # Forward pass
    loss = criterion(output, target) # Use the full target batch
    loss.backward() # Backward pass

    # See traiining progress
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
    
    optimizer.step() # Update model parameters

# Check accuracy after training
accuracy = calculate_accuracy(output, target)
print(f"Final Accuracy: {accuracy * 100:.2f}%")