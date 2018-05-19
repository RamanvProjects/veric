''' GridWorldMDPClass.py: Contains the GridWorldMDP class. '''

# Python imports.
from __future__ import print_function
import random
import sys
import os
import numpy as np

# Other imports.
from simple_rl.mdp.MDPClass import MDP
from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState

class GraphWorldMDP(MDP):
    ''' Class for a Graph MDP '''

    # Static constants.
    ACTIONS = ["up", "down", "left", "right"]

    def __init__(self,
                graph,
                goals={},
                start_state={},
                is_goal_terminal=True,
                gamma=0.99,
                init_state=None,
                slip_prob=0.0,
                step_cost=0.0,
                name="gridworld"):
        '''
        Args:
            height (int)
            width (int)
            init_loc (tuple: (int, int))
            goal_locs (list of tuples: [(int, int)...])
            lava_locs (list of tuples: [(int, int)...]): These locations return -1 reward.
        '''

        # Setup init location.
        self.graph = graph
        self.goals = goals

        MDP.__init__(self, self.graph.keys(), self._transition_func, self._reward_func, init_state=GraphWorldState(state=0, goals=goals), gamma=gamma)

        self.step_cost = step_cost
        self.cur_state = GraphWorldState(start_state, goals)
        self.is_goal_terminal = is_goal_terminal
        self.name = name
    
    def _transition_func(self, state, action):
        '''
        Args:
            state (State)
            action (str)

        Returns
            (State)
        '''

        # An action is an edge

        if action not in self.graph[state.state]:
            return state

        return GraphWorldState(state=action, goals=self.goals)
    
    def _reward_func(self, state, action):
        if self._transition_func(state, action).state in self.goals:
            return 1.0
        else:
            return 0.0

    def __str__(self):
        return "graph"

class GraphWorldState(object):
    def __init__(self, state, goals):
        self.state = state
        self.goals = goals
    
    def is_terminal(self):
        state = self.state
        print("="*8)
        print(state)

        return self.state in self.goals