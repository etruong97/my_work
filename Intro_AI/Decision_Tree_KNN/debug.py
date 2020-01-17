from a5 import *

import numpy as np
import csv

##################################################
#                 Debug Class
#
# This is for you to check if your entropy, information gain, and classify implementations produce the
# intended results. Further debugging is encouraged to be done on your own, but the grading tool will also provide some
# feedback as to what you might be missing.
#
# Simply run the main function at the bottom of the file to check your results compared to the intended answers.
#
##################################################

# Loads the data file, does some preprocessing, returns numpy arrays for points and labels
def load_data(filename):
    # Create list to hold raw data
    data_raw = []
    with open(filename, 'r') as f:
        data_raw = list(csv.reader(f, delimiter=','))

    # Remove empty list from final line
    data_raw.remove([])

    # Only consider continuous values for data points
    # age: 0, fnlwgt:2, education-num: 4, capital-gain: 10, capital-loss: 11, hours-per-week: 12
    # fnlwgt is a continuous-valued census estimate of demographic background
    data_points = np.array([[x[0], x[2], x[4], x[10], x[11], x[12]] for x in data_raw], dtype='float32')

    # A point is labelled positive if its final column is ">50K"
    data_labels = np.array([1 if x[14] == ' >50K' else 0 for x in data_raw], dtype='int')

    return data_points, data_labels

class debug:
    def __init__(self):
        self.classifications = [1, 1, 1, 2, 2, 2, 2, 2]
        self.test_node = Node(attribute=3, children={
            OTHER: Node(attribute=None, children={}, classification=0),
            'size': Node(attribute=2, children={
                OTHER: Node(attribute=None, children={}, classification=1),
                'length': Node(attribute=1, children={
                    'width': Node(attribute=None, children={}, classification=1),
                    OTHER: Node(attribute=None,children={},classification=0)})})})

        self.fruit_tree = Node(attribute='appetite', children={
            'famished': Node(attribute='thirst', children={
                'quenched': Node(attribute='preference', children={
                    'spicy': Node(classification='banana'),
                    OTHER: Node(classification='peach'),
                }),
                'neutral': Node(classification='peach'),OTHER: Node(classification='peach'),}),
            'neutral': Node(attribute='thirst', children={'neutral': Node(classification='berry'),
                                                          OTHER: Node(classification='apple'),
                                                          }),
            'full': Node(classification='berry'),
            OTHER: Node(classification='apple'),})


    def debug_entropy(self):
        test1 = [self.classifications[i] for i in (0, 1, 3)]
        entropy_test = entropy(test1)
        print(entropy_test)

        test2 = [self.classifications[i] for i in [2, 4, 5, 6, 7]]
        entropy_test = entropy(test2)
        print(entropy_test)

        test3 = [self.classifications[i] for i in list(range(8))]
        entropy_test = entropy(test3)
        print(entropy_test)

    def debug_informationGain(self):
        parent_classifications = self.classifications
        child1_classifications = [self.classifications[i] for i in (0, 1, 3)]
        child2_classifications = [self.classifications[i] for i in [2, 4, 5, 6, 7]]
        ig_test = information_gain(parent_classifications, {1:child1_classifications, 2:child2_classifications}, {1:3, 2:5})
        print(ig_test)

    def debug_classify(self):
       test_point_1 = {1:'b', 2:'color', 3:'money'}
       classification_test_1 = self.test_node.classify(test_point_1)
       print(classification_test_1)
       test_point_2 = {1: 'width', 2: 'length', 3: 'size'}
       classification_test_2 = self.test_node.classify(test_point_2)
       print(classification_test_2)
       test_point_3 = {1: 'weight', 2: 'color', 3: 'size'}
       classification_test_3 = self.test_node.classify(test_point_3)
       print(classification_test_3)
       fruit_test = {'appetite': 'famished', 'thirst': 'neutral', 'preference': 'spicy'}
       classification_test_4 = self.fruit_tree.classify(fruit_test)
       print(classification_test_4)

    def debug_knn_classifier(self):

        DATA_SIZE = 28000 # our given data includes 28,000 points

        ## set the below to 25,000 & 3,000 respectively to test on the entire data set
        ## the 2000/500 setup takes the instructor solution ~45 seconds to complete all tests.
        TRAINING_LENGTH = 2000 # we'll train on 2,000 points
        VALIDATION_LENGTH = 500 # we'll us 500 points as validation data

        income_points, income_labels = load_data('income.data')
        train_points, train_labels = income_points[:TRAINING_LENGTH], income_labels[:TRAINING_LENGTH]
        validation_points, validation_labels = income_points[TRAINING_LENGTH:TRAINING_LENGTH + VALIDATION_LENGTH], income_labels[TRAINING_LENGTH:TRAINING_LENGTH + VALIDATION_LENGTH]

        basic_1nn = KNN_Classifier(k=1)
        basic_3nn = KNN_Classifier(k=3)

        basic_1nn_correct = 0
        basic_3nn_correct = 0

        for point, label in zip(validation_points, validation_labels):
            if basic_1nn.classify(point, train_points, train_labels) == label:
                basic_1nn_correct += 1
            if basic_3nn.classify(point, train_points, train_labels) == label:
                basic_3nn_correct += 1

        print(f'1NN classifier got {basic_1nn_correct} correct!')
        print(f'3NN classifier got {basic_3nn_correct} correct!')

        print(f'1NN classifier accuracy: {basic_1nn_correct/float(len(validation_labels)) * 100.0}%')
        print(f'3NN classifier accuracy: {basic_3nn_correct/float(len(validation_labels)) * 100.0}%')


if __name__ == '__main__':
    d = debug()
    print("\nYour entropy values: ")
    d.debug_entropy()
    print("\nExpected entropy values: \n0.9182958340544896\n0.7219280948873623\n0.954434002924965")
    print("\nYour information gain value: ")
    d.debug_informationGain()
    print("\nExpected information gain value: \n0.15886800584993")
    print("\nYour classify values: ")
    d.debug_classify()
    print("\nExpected classify values: \n0 \n1 \n1 \npeach\n")

    ## You might find it useful to read this debug method
    ##  and to change some of the debug values once you have a 
    ##  working classifier!
    d.debug_knn_classifier()