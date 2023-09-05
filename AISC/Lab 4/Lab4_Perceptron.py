import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, max_epochs=100):
        self.input_size = input_size
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.weights = np.random.rand(input_size + 1)  # Random initialization of weights
        self.errors = []

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        # Add a bias term (1) to the inputs
        inputs = np.insert(inputs, 0, 1)
        # Compute the dot product of weights and inputs
        net_input = np.dot(self.weights, inputs)
        # Apply the activation function to get the output (0 or 1)
        return self.activation(net_input)

    def train(self, X, y):
        for epoch in range(self.max_epochs):
            errors = 0
            for i in range(X.shape[0]):
                prediction = self.predict(X[i, :])
                error = y[i] - prediction
                errors += int(error != 0)
                # Update weights using the Perceptron learning rule
                self.weights += self.learning_rate * error * np.insert(X[i, :], 0, 1)
            self.errors.append(errors)
            # Stop training if all examples are classified correctly
            if errors == 0:
                print(f"Converged at epoch {epoch + 1}.")
                break

# Example usage:

# Define the training data (OR gate)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])

# Create a Perceptron with 2 input nodes (for the 2 features of the input data)
perceptron = Perceptron(input_size=2)

# Train the Perceptron
perceptron.train(X, y)

# Test the Perceptron
print("Testing the Perceptron:")
for i in range(X.shape[0]):
    prediction = perceptron.predict(X[i, :])
    print(f"Input: {X[i, :]} --> Prediction: {prediction}")
