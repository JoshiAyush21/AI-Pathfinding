# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

##Prakhar Bhartiya - 1223130441 - Fall'22 CSE571

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

# from 1.search.util import manhattanDistance
import util
import time

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #print("Start: ", problem.getStartState()) #printed = (5,5)
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState())) #printed = False (Boolean)
    #print("Start's successors:", problem.getSuccessors(problem.getStartState())) #printed = Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    #time.sleep(3) #seconds sleep to see result

    closed = list()
    fringe = util.Stack() #initialise stack structure from util
    fringe.push((problem.getStartState(), ())) #push start state and empty action list

    while fringe.isEmpty()!=True: ## Run while fringe is not empty or we havent exhausted every pausibilities
        node = fringe.pop()
        curr_state = node[0]
        curr_action = node[1]
        #problem state structure = [state, actions]
        if problem.isGoalState(curr_state):
            return list(curr_action)

        if curr_state not in closed:
            closed.append(curr_state)

            for child_node in problem.getSuccessors(curr_state):
                #child_node structure = list of triples, (successor, action, stepCost)
                successor = child_node[0] #state
                action = child_node[1]
                stepCost = child_node[2]

                updated_action_list = list(curr_action)
                #add action to total actions lists
                updated_action_list.append(action)

                if successor not in closed:
                    #push a tuple to fringe
                    fringe.push((successor, (updated_action_list)))

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    """
    Algo Text book page.82

    function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure

    node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    frontier ← a FIFO queue with node as the only element
    explored ← an empty set
    loop do
        if EMPTY?(frontier) then return failure
        node←POP(frontier) /*choosestheshallowestnodeinfrontier */
        add node.STATE to explored
        for each action in problem.ACTIONS(node.STATE) do
            child ←CHILD-NODE(problem,node,action)
            if child.STATE is not in explored or frontier then
                if problem.GOAL-TEST(child.STATE) then return SOLUTION(child)
                frontier ←INSERT(child,frontier)
    """
    ## Same code as DFS just use Queue ##
    closed = list()
    fringe = util.Queue()
    fringe.push((problem.getStartState(), ()))

    while fringe.isEmpty()!=True: ## Run while fringe is not empty or we havent exhausted every pausibilities
        node = fringe.pop()
        curr_state = node[0]
        curr_action = node[1]
        #problem state structure = [state, actions]
        if problem.isGoalState(curr_state):
            return list(curr_action)

        if curr_state not in closed:
            closed.append(curr_state)

            for child_node in problem.getSuccessors(curr_state):
                #child_node structure = list of triples, (successor, action, stepCost)
                successor = child_node[0] #state
                action = child_node[1]
                stepCost = child_node[2]

                updated_action_list = list(curr_action)
                #add action to total actions lists
                updated_action_list.append(action)

                if successor not in closed:
                    #push a tuple to fringe
                    fringe.push((successor, (updated_action_list)))

    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    """
    Algo Text book page.84

    function UNIFORM-COST-SEARCH(problem) returns a solution, or failure

    node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    frontier ← a priority queue ordered by PATH-COST, with node as the only element
    explored ← an empty set
    loop do
        if EMPTY?(frontier) then return failure
        node←POP(frontier) /*choosesthelowest-costnodeinfrontier */
        if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
        add node.STATE to explored
        for each action in problem.ACTIONS(node.STATE) do
            child ←CHILD-NODE(problem,node,action)
            if child.STATE is not in explored or frontier then
                frontier ←INSERT(child,frontier)
            else if child.STATE is in frontier with higher PATH-COST then
                replace that frontier node with child
    """
    ## Same code as BFS just use PriorityQueue ##
    closed = list()
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), ()), -1) #push(self, item, priority)

    while fringe.isEmpty()!=True: ## Run while fringe is not empty or we havent exhausted every pausibilities
        node = fringe.pop()
        curr_state = node[0]
        curr_action = node[1]
        #problem state structure = [state, actions]
        if problem.isGoalState(curr_state):
            return list(curr_action)

        if curr_state not in closed:
            closed.append(curr_state)

            for child_node in problem.getSuccessors(curr_state):
                #child_node structure = list of triples, (successor, action, stepCost)
                successor = child_node[0] #state
                action = child_node[1]
                stepCost = child_node[2]

                updated_action_list = list(curr_action)
                #add action to total actions lists
                updated_action_list.append(action)

                if successor not in closed:
                    #push a tuple to fringe also action costs as priority for next node expansion
                    fringe.push((successor, (updated_action_list)), problem.getCostOfActions(updated_action_list))

    #util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """
    Algo Text book page.99 - Best-First-search ~ A* but recursive

    function RECURSIVE-BEST-FIRST-SEARCH(problem) returns a solution, or failure
        return RBFS(problem, MAKE-NODE(problem.INITIAL-STATE), ∞)

    function RBFS(problem,node,f limit) returns a solution, or failure and a new f-cost limit

    if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    successors ← [ ]
    for each action in problem.ACTIONS(node.STATE) do
        add CHILD-NODE(problem,node,action) into successors
    if successors is empty then return failure, ∞
    for each s in successors do /* update f with value from previous search, if any */
        s.f ←max(s.g + s.h, node.f))
    loop do
        best ← the lowest f -value node in successors
        if best.f > f limit then return failure, best.f
        alternative ← the second-lowest f -value among successors
        result,best.f ←RBFS(problem,best,min(f limit,alternative))
        if result ̸= failure then return result
    """

    ## Same as UCS but also add heuristic cost f(n) = g(h) + h(n)

    closed = list()
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), ()), -1) #push(self, item, priority)

    while fringe.isEmpty()!=True: ## Run while fringe is not empty or we havent exhausted every pausibilities
        node = fringe.pop()
        curr_state = node[0]
        curr_action = node[1]
        #problem state structure = [state, actions]
        if problem.isGoalState(curr_state):
            return list(curr_action)

        if curr_state not in closed:
            closed.append(curr_state)

            for child_node in problem.getSuccessors(curr_state):
                #child_node structure = list of triples, (successor, action, stepCost)
                successor = child_node[0] #state
                action = child_node[1]
                stepCost = child_node[2]

                updated_action_list = list(curr_action)
                #add action to total actions lists
                updated_action_list.append(action)

                if successor not in closed:
                    #push a tuple to fringe also action costs as priority for next node expansion
                    fringe.push((successor, (updated_action_list)), problem.getCostOfActions(updated_action_list) + (heuristic(successor,problem)))

def reverseBack(back_actions):
    #reverse the half path of back direction
    direction = {'North': 'South', 'East': 'West', 'South': 'North', 'West': 'East'}

    updated_direction = list()

    for action in back_actions:
        updated_direction.append(direction[action])

    return updated_direction[::-1]

def biDirectionalSearch_MM0(problem, heuristic=nullHeuristic):

    '''
    pr_f(n) = max(f_f(n), 2g_f(n))
    U is the cost of the cheapest solution so far

    getCostOfActions from goal does not work
    
    '''


    closed_f = list()
    closed_b = list()

    g_f = {}
    g_f[problem.getStartState()] = 0

    g_b = {}
    g_b[problem.goal] = 0

    open_f = util.PriorityQueue()
    open_f.push((problem.getStartState(), ()), -1) #push(self, item, priority)

    open_b = util.PriorityQueue()
    open_b.push((problem.goal, ()), -1) #push(self, item, priority)

    c_star = util.manhattanDistance(problem.getStartState(), problem.goal)
    u = 1000000

    # epsilon = cheapest edge ?
    epsilon = 0

    while open_f.isEmpty()!=True and open_b.isEmpty() != True: ## Run while fringe is not empty or we havent exhausted every pausibilities
        
        f_f = min([problem.getCostOfActions(f[1]) for index, (p, c, f) in enumerate(open_f.heap)])
        f_b = min([problem.getCostOfActionsGoal(f[1]) for index, (p, c, f) in enumerate(open_b.heap)])

        
        temp_f = open_f.pop()
        temp_b = open_b.pop()

        pr_f = max(problem.getCostOfActions(temp_f[1]), 2 * (heuristic(temp_f[0],problem)))
        pr_b = max(problem.getCostOfActionsGoal(temp_b[1]), 2 * (heuristic(temp_b[0],problem)))

        open_f.push(temp_f, pr_f)
        open_b.push(temp_b, pr_b)

        c = min(pr_f, pr_b)
        # print("u: ", u, " c: ", c, " f_f: ", f_f, " f_b: ", f_b, " min g: ", min(g_f.values()) + min(g_b.values()) + epsilon)

        # if u <= max(c, f_f, f_b, min(g_f.values()) + min(g_b.values()) + epsilon):
        # if temp_f[0] in closed_b or temp_b[0] in closed_f:
        #     #   get path from start + reversed path from goal somehow
        #     print("U: ", u)
        #     action_front = temp_f[1]
        #     action_back = temp_b[1]

        #     all_actions = action_front + reverseBack(action_back)

        #     return all_actions
            # pass

        if c == pr_f :

            n = open_f.pop()
            curr_state = n[0]
            curr_action = n[1]
            
            if curr_state not in closed_f:
                closed_f.append(curr_state)
                
                for child_node in problem.getSuccessors(curr_state):
                    successor = child_node[0] #state
                    action = child_node[1]
                    stepCost = child_node[2]

                    if successor in closed_f or open_f.find(successor):
                        if successor in g_f.keys() and g_f[successor] <= g_f[curr_state] + stepCost:
                            continue
                        else:
                            # remove successor from open_f union closed_f 
                            try:
                                open_f.delete(successor)
                                closed_f.remove(successor)
                            except:
                                pass

                    g_f[successor] = g_f[curr_state] + stepCost
                    updated_action_list = list(curr_action)
                    #add action to total actions lists
                    updated_action_list.append(action)
                    open_f.push((successor, (updated_action_list)), max(problem.getCostOfActions(updated_action_list), 2 * (heuristic(successor,problem))))
                    # open_f.push((successor, (updated_action_list)), max(problem.getCostOfActions(updated_action_list), 2 * (util.manhattanDistance(successor, temp_b[0]))))

                    if open_b.find(successor):
                        # print("From front")
                        u = min(u, g_f[successor] + g_b[successor])
                        all_actions = updated_action_list + reverseBack(open_b.find(successor)[1])
                        problem.isGoalState(successor, False)
                        return all_actions
    

        else:
            # print("pr_b")
            n = open_b.pop()
            curr_state = n[0]
            curr_action = n[1]
            
            if curr_state not in closed_b:
                closed_b.append(curr_state)
                
                for child_node in problem.getSuccessors(curr_state):
                    successor = child_node[0] #state
                    action = child_node[1] 
                    stepCost = child_node[2]

                    if successor in closed_b or open_b.find(successor):
                        if successor in g_b.keys() and g_b[successor] <= g_b[curr_state] + stepCost:
                            continue
                        else:
                            # remove successor from open_f union closed_f ?
                            try:
                                open_b.delete(successor)
                                closed_b.remove(successor)
                            except:
                                pass

                    g_b[successor] = g_b[curr_state] + stepCost
                    updated_action_list = list(curr_action)
                    #add action to total actions lists
                    updated_action_list.append(action)
                    open_b.push((successor, (updated_action_list)), max(problem.getCostOfActionsGoal(updated_action_list), 2 * (heuristic(successor,problem))))
                    # open_b.push((successor, (updated_action_list)), max(problem.getCostOfActionsGoal(updated_action_list), 2 * (util.manhattanDistance(successor, temp_f[0]))))

                    if open_f.find(successor):

                        # print("from back")
                        u = min(u, g_f[successor] + g_b[successor])
                        # print(open_f.find(successor))
                        all_actions = open_f.find(successor)[1] + reverseBack(updated_action_list)
                        problem.isGoalState(successor, False)
                        return all_actions



def biDirectionalSearch_MM(problem, heuristic=nullHeuristic):

    '''
    pr_f(n) = max(f_f(n), 2g_f(n))
    U is the cost of the cheapest solution so far

    getCostOfActions from goal does not work
    
    '''


    closed_f = list()
    closed_b = list()

    g_f = {}
    g_f[problem.getStartState()] = 0

    g_b = {}
    g_b[problem.goal] = 0

    open_f = util.PriorityQueue()
    open_f.push((problem.getStartState(), ()), -1) #push(self, item, priority)

    open_b = util.PriorityQueue()
    open_b.push((problem.goal, ()), -1) #push(self, item, priority)

    c_star = util.manhattanDistance(problem.getStartState(), problem.goal)
    u = 1000000

    # epsilon = cheapest edge ?
    epsilon = 0

    while open_f.isEmpty()!=True and open_b.isEmpty() != True: ## Run while fringe is not empty or we havent exhausted every pausibilities
        
        f_f = min([problem.getCostOfActions(f[1]) for index, (p, c, f) in enumerate(open_f.heap)])
        f_b = min([problem.getCostOfActionsGoal(f[1]) for index, (p, c, f) in enumerate(open_b.heap)])

        
        temp_f = open_f.pop()
        temp_b = open_b.pop()

        pr_f = max(problem.getCostOfActions(temp_f[1]), 2 * (heuristic(temp_f[0],problem)))
        pr_b = max(problem.getCostOfActionsGoal(temp_b[1]), 2 * (heuristic(temp_b[0],problem)))

        open_f.push(temp_f, pr_f)
        open_b.push(temp_b, pr_b)

        c = min(pr_f, pr_b)
        # print("u: ", u, " c: ", c, " f_f: ", f_f, " f_b: ", f_b, " min g: ", min(g_f.values()) + min(g_b.values()) + epsilon)

        # if u <= max(c, f_f, f_b, min(g_f.values()) + min(g_b.values()) + epsilon):
        # if temp_f[0] in closed_b or temp_b[0] in closed_f:
        #     #   get path from start + reversed path from goal somehow
        #     print("U: ", u)
        #     action_front = temp_f[1]
        #     action_back = temp_b[1]

        #     all_actions = action_front + reverseBack(action_back)

        #     return all_actions
            # pass

        if c == pr_f :

            n = open_f.pop()
            curr_state = n[0]
            curr_action = n[1]
            
            if curr_state not in closed_f:
                closed_f.append(curr_state)
                
                for child_node in problem.getSuccessors(curr_state):
                    successor = child_node[0] #state
                    action = child_node[1]
                    stepCost = child_node[2]

                    if successor in closed_f or open_f.find(successor):
                        if successor in g_f.keys() and g_f[successor] <= g_f[curr_state] + stepCost:
                            continue
                        else:
                            # remove successor from open_f union closed_f 
                            try:
                                open_f.delete(successor)
                                closed_f.remove(successor)
                            except:
                                pass

                    g_f[successor] = g_f[curr_state] + stepCost
                    updated_action_list = list(curr_action)
                    #add action to total actions lists
                    updated_action_list.append(action)
                    # open_f.push((successor, (updated_action_list)), max(problem.getCostOfActions(updated_action_list), 2 * (heuristic(successor,problem))))
                    open_f.push((successor, (updated_action_list)), max(problem.getCostOfActions(updated_action_list), 2 * (util.manhattanDistance(successor, temp_b[0]))))

                    if open_b.find(successor):
                        # print("From front")
                        u = min(u, g_f[successor] + g_b[successor])
                        all_actions = updated_action_list + reverseBack(open_b.find(successor)[1])
                        problem.isGoalState(successor, False)
                        return all_actions
    

        else:
            # print("pr_b")
            n = open_b.pop()
            curr_state = n[0]
            curr_action = n[1]
            
            if curr_state not in closed_b:
                closed_b.append(curr_state)
                
                for child_node in problem.getSuccessors(curr_state):
                    successor = child_node[0] #state
                    action = child_node[1] 
                    stepCost = child_node[2]

                    if successor in closed_b or open_b.find(successor):
                        if successor in g_b.keys() and g_b[successor] <= g_b[curr_state] + stepCost:
                            continue
                        else:
                            # remove successor from open_f union closed_f ?
                            try:
                                open_b.delete(successor)
                                closed_b.remove(successor)
                            except:
                                pass

                    g_b[successor] = g_b[curr_state] + stepCost
                    updated_action_list = list(curr_action)
                    #add action to total actions lists
                    updated_action_list.append(action)
                    # open_b.push((successor, (updated_action_list)), max(problem.getCostOfActionsGoal(updated_action_list), 2 * (heuristic(successor,problem))))
                    open_b.push((successor, (updated_action_list)), max(problem.getCostOfActionsGoal(updated_action_list), 2 * (util.manhattanDistance(successor, temp_f[0]))))

                    if open_f.find(successor):

                        # print("from back")
                        u = min(u, g_f[successor] + g_b[successor])
                        # print(open_f.find(successor))
                        all_actions = open_f.find(successor)[1] + reverseBack(updated_action_list)
                        problem.isGoalState(successor, False)
                        return all_actions


"""
python3 pacman.py -l smallMaze -p SearchAgent -a fn=mm
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=mm
python3 pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=mm
"""

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
mm0 = biDirectionalSearch_MM0
mm = biDirectionalSearch_MM

