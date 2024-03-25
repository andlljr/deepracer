# Deep Racer

## Configurações utilizadas para a elaboração da atividade

**Action space type:**
Continuous

**Action space:**
Speed: [ 1 : 4 ] m/s
Steering angle: [ -20 : 20 ] °

**Framework:**
Tensorflow

**Reinforcement learning algorithm:**
PPO

**Hyperparameter/Value**

* Gradient descent batch size:	64
* Entropy:	0.03
* Discount factor:	0.80
* Loss type:	Mean squared error
* Learning rate:	0.0001
* Number of experience episodes between each policy-updating iteration:	30
* Number of epochs:	10
