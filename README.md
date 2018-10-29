# MOVE-37 BipedalWalker
Using Evolution Strategies (ES) to train a bipdel robot to walk.
# Dependencies
[OpenAI Gym](https://github.com/openai/gym)
'''
pip install gym
'''
[Evostra Repository](https://github.com/alirezamika/evostra)
'''
pip install evostra
'''
# Training
The program trains standard for 100 iterations. The number of iteration could be changed in *train_agent.py*, by changing the *n* hyperparameter.
'''
python train_agent.py
'''
# Playing
The program plays 10 episode. For changing it, change *n* in *play_agent.py*.
'''
python play_agent.py
'''
