from numpy import *

def compute_error_for_line_given_points(b, m, points):

def gradient_descent_runner


def run():

    # 1 - Collect data
    points = genfromtxt('data.csv', delimiter=',')

    # 2 - Define hyper parameter
    # how fast should the model converge?
    learning_rate = 0.001

    # y = mx + b
    # y intercept
    initial_b = 0

    # slope
    initial_m = 0

    num_iterations = 1000


    # 3 - Train the model
    print 'Starting gradient descent at b = {0}, m = {1}, error = {2}'.format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    [b, m] = gradient_descent_runner(points, intial_b, initial_m, learning_rate, num_iterations)

    print 'Ending point at b = {1}, m = {2}, error = {3}'.format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))


if __name__ == '__main__':
    run()