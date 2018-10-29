from agent import Agent

# Initialize agent
agent = Agent()

# train for n iterations
n = 100
agent.train(n)

# Save weights of the trained model into 'weights.pkl'
agent.save()
