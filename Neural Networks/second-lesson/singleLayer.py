from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs
        random.seed(1)

        # We model a single neuron, with 3 input connections and 1 output connection.
        # We assign random weights to a 3 x 1 matric with values in the range -1 to 1
        # and mean 0
        self.synaptic_weights = 2 * random.random((3, 1))-1

    # The sigmoid function, which describes an s shaped curve
    # we pass the weighted sum of the inputs through this function
    # to normalize them between 0 and 1
    def __sigmoid(self, x):
        return 1/(1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Pass the training set through the neural network (single neuron)
            output = self.think(training_set_inputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output)
            error = training_set_outputs - output

            # Multiply the error by the input and again by the gradient of the Sigmoid curve
            # Less confident weights are adjusted more
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Adjust the weights.
            self.synaptic_weights += adjustment

    # The brain of the network
    def think(self, inputs):
        # Pass inputs through the neural network
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == 'main':

    # neural network
    neural_network = NeuralNetwork()

    print("Random startinc synaptic weights ")
    print(neural_network.synaptic_weights)

    # The training set. 4 total examples, each with 3 inputs and 1 output
    training_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_outputs = array([[0, 1, 1, 0]]).T

    # Train the neural network using the training set
    # Do it 10,000 times and make small adjustments each time
    neural_network.train(training_inputs, training_outputs, 10000)

    print("New syaptic weights after training: ")
    print(neural_network.synaptic_weights)

    # Test the network
    print("Considering new situation [1, 0, 0] -> ?: ")
    print(neural_network.think(array([1, 0, 0])))