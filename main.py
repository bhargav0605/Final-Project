# By Sudeep kuchara and Bhargav Parmar
# Special thanks to lucas thompson's YT channel, he helped me throughout this project
# Application of the NEAT algorithm using neat-python to play the retro contra(NES)
# OpenAI environment
# bugfixes 
# Retro-gym yadayadayada

import numpy as np 
import retro
import cv2
import neat
import pickle

imgarray = []

env = retro.make('Contra-Nes', 'Level1') #initialization of the game environment
env.reset()

inx, iny, inc = env.observation_space.shape
print("The resolution of the game is", inx, iny, inc)
def eval_genome(genomes, config):
    for genome_id, genome in genomes:
        ob = env.reset()
        ac = env.action_space.sample()

        inx, iny, inc = env.observation_space.shape

        inx = int(inx/8)
        iny = int(iny/8)

        net = neat.nn.RecurrentNetwork.create(genome, config)
    
        current_max_fitness = 0 
        fitness_current = 0
        frame = 0
        counter = 0
        xpos = 0
        xpos_max=0
        xpos_end = 0
        prev_score = 0
        xscroll = 0

        done = False
        cv2.namedWindow("main",cv2.WINDOW_NORMAL)

        while not done:
            env.render()
            frame += 1
            scaledimg = cv2.cvtColor(ob, cv2.COLOR_BGR2RGB)
            scaledimg = cv2.resize(scaledimg,(iny, inx)) 
            ob = cv2.resize(ob, (inx, iny))
            ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
            ob = np.reshape(ob, (inx, iny))
            cv2.imshow("main", scaledimg)
            cv2.waitKey(1)

            for x in ob:
                for y in x:
                    imgarray.append(y)
            nnOutput = net.activate(imgarray)
            #print(len(imgarray), nnOutput)

            ob, rew, done, info = env.step(nnOutput)

            imgarray.clear()

            xpos = info['xscroll']
    
            #if info['score'] > prev_score: #increments reward if scored
            #   rew += 1
            #   fitness_current += 1
            #   prev_score = int(info['score'])

            xpos_end = int(info['level'])
            if xpos_end == 2:
                rew += 20000
                #done = True
    
            if int(info['xscroll']) > int(xpos_max):  #increment fitness and reward if the agent goes further in x-axis
                fitness_current += 1  
                rew +=  int(info['xscroll']) + int(info['score']) 
                xpos_max = int(info['xscroll'])
            #print(info['score'], rew, info['xscroll'])
            #rew += fitness_current
            #print(xpos, "reward: ", rew) finally the reward function is working/ yay
            #rew += fitness_current
            #print(rew, fitness_current)
            if fitness_current > current_max_fitness:
            #if int(info['xscroll']) > xscroll:
                current_max_fitness = fitness_current
            #   xscroll = int(info['xscroll'])
                counter = 0
            else:
                counter += 1
            if done or counter == 350:
                done = True
                print(genome_id, fitness_current, rew, info["score"])
            #if int(info['lives']) < 2:
            #   done = True
            #   print(genome_id, fitness_current, rew, info['score'])
            genome.fitness = fitness_current
            #print("actions: ", ac , "scores: ", info['score'], " fitness: ", fitness_current)
            #print(rew, xpos)


config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation, 
                    'config-feedforward') 

p = neat.Population(config)
p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-0')


p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)
p.add_reporter(neat.Checkpointer(10))

winner = p.run(eval_genome)
