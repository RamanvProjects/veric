# Imports
from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.tasks import GridWorldMDP
from simple_rl.agents import QLearningAgent

from vivek import ascii_to_graph
import randh
import networkx as nx
from GraphMDP import GraphWorldMDP

# Run Experiment


graph = ascii_to_graph('gridworld.txt')
print graph
levels = randh.hierarchy(nx.Graph(graph), sizes=[8,4,2,1])

#for level in levels:
#    abstract_G, classes, subgraphs = levels[level]
#    print subgraphs

mdp = GraphWorldMDP(graph, goals=set([9]), start_state=0)
agent = QLearningAgent(mdp.get_actions())
run_agents_on_mdp([agent], mdp)





