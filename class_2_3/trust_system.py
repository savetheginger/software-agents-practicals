import random
import networkx as nx
import time

from class_2_3.agent import Agent
from class_2_3.environment import Environment


NUM_AGENTS = 10  # Number of agents

random.seed(0)  # set the random seed
a = []
for i in range(0, NUM_AGENTS):
    a.append(Agent(random.random()))

# create a complete graph,
# see https://networkx.github.io/documentation/stable/reference/generators.html for other generators
G = nx.complete_graph(NUM_AGENTS)
E = Environment(G)
E.add_agents(a)

# random.seed(time.time()) #uncomment if you want different experiments on same graph
for i in range(0, 100):  # run for 100 rounds
    score = [0, 0]
    for a in E.nodes:
        s = a.delegate()
        if s:
            score[0] += 1
        else:
            score[1] += 1
    print(score)