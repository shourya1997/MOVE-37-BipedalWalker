from agent import Agent

# Initialize agent
agent = Agent()

# Load in trained model
agent.load('weights.pkl')

# play n episodes
n = 10
agent.play(n)
