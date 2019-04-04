# Putting It All Together
So if you still have confusion, here is what is essentially happening when you run ```cart_pole_pytorch.py```

After initializing our: Neural Network, Optimizer, Loss-Function, and Environment we enter into **inference** training. 

That is, we train our Neural Network at inference. As the Agent navigates and plays the game it is learning. *Close to how actual AGI will work*. 

In the very beginning our Agent's NN is initialized with random weights. Therefor it will perform badly, and will end an episodes very quickly. 

The first function that is called (called on loop) is ```iterate_batches()``` which will return a batch. Since we use ```enumerate``` it will return a batch & iteration number to keep track. 

In our example a batch is composed of **16 episodes**. Remember an episode is essentially an entire game played. 

We then take this batch (we process one batch at a time) and run it through ```filter_batch()``` which in our case will return **top 30%** episodes (observations and associated actions). 

We will then use what ```filter_batch()``` returns: ```obs_v, acts_v, reward_b, reward_m```. Most important we will use: ```obs_v``` as our input to our neural network. ```acts_v``` as the **true labels** to the input. 

So now that we have these variables, we will first run ```obs_v``` into our (at first = untrained neural network) to give us a prediction (softmax) of actions to take. 

Running ```obs_v``` into our neural network will return ```action_scores``` which is predicted actions to take. 

We will then use ```nn.CrossEntropyLoss(action_scores, acts_v)``` to compare: **predicted**: ```action_scores``` to **actual**: ```acts_v``` to calculate our loss. 

With our loss calculated we will do (as you usually do for NN training):
* calculate gradients: ```loss_v.backward()```
* call optimizer step: ```optimizer.step()```

Then we repeat! 

What happens is: every iteration is an iteration of **16 batches**. As the loss goes down, the agent last longer and keeps track of the obervations and actions. 

With gradient descent it will eventually learn the steps to take in order to achieve the goal! 