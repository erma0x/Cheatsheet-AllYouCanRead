from mchgenalg import GeneticAlgorithm
import numpy as np
import struct

"""
Based on
https://github.com/chovanecm/python-genetic-algorithm
"""
def string_to_float(sequence):
    #64bit
    #print(sequence)
    sequence='0b'+sequence
    q = int(sequence, 0)
    b8 = struct.pack('Q', q)
    num = struct.unpack('d', b8)[0] 
    #num = struct.unpack('d', struct.pack('Q', int(sequence, 25)))[0]
    return num

def bit_array_to_string(Genome):
    sentence = [ int(i) for i in Genome]
    ''.join(str(sentence))
    sent_str = ''
    for i in sentence:
        if i in (0,1):
            sent_str += str(i)
    sent_str = sent_str[:-1]
    return(sent_str)
    
################################################
#### TO IMPLEMENT
# First, define function that will be used to evaluate the fitness
def fitness_function(genome):
    string = bit_array_to_string(genome)
    
    float_ = string_to_float(string)
    
    return intercept_number

##################################################

def backtest_buy():
    pass    

##########################
# Configure the algorithm:
population_size = 100
genome_length = 124
ga = GeneticAlgorithm(fitness_function)
ga.generate_binary_population(size=population_size, genome_length=genome_length)
# How many pairs of individuals should be picked to mate
ga.number_of_pairs = 5
# Selective pressure from interval [1.0, 2.0]
# the lower value, the less will the fitness play role
ga.selective_pressure = 3.5
ga.mutation_rate = 0.1
# If two parents have the same genotype, ignore them and generate TWO random parents
# This helps preventing premature convergence
ga.allow_random_parent = True # default True
# Use single point crossover instead of uniform crossover
ga.single_point_cross_over = False # default False
###########################




# Run 1000 iteration of the algorithm
# You can call the method several times and adjust some parameters
# (e.g. number_of_pairs, selective_pressure, mutation_rate,
# allow_random_parent, single_point_cross_over)
ga.run(1000)

best_genome, best_fitness = ga.get_best_genome()

# If you want, you can have a look at the population:
population = ga.population
# and the fitness of each element:
fitness_vector = ga.get_fitness_vector()

#################################
print(fitness_vector)
