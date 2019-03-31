# About This Repository
The purpose of this Repository is mainly for reference and educational purposes only. This will be a combination of both **Jupyter Notebooks** & **Python Scripts** describing the algorithms that go into **Deep Reinforcement Learning** & **Game Optimization**. 

Each **Notebook** Should have a set of examples, math description & more. 

You can simply go through each notebook to learn more about said subject and algorithms, or you can run the scripts to run some of these fun agents!

## Installing
My suggestion would be to simply clone this repository:
```
$ git clone https://github.com/dmbernaal/Deep-Reinforcement-Learning-Algorithms.git
```
and run each notebook locally on your computer. The code has been made simple to understand and should have several of examples and comments! 

## Setup 
It's good practice to have a virtual enviromment when running Machine Learning / Datascience experiments. Most of the time when learning something from a course/book you will be using various dependencies/libraries. Sometimes not all align with eachother using various versions of the same or different libraries. So I setup a ```config.sh``` shell script to install the right dependencies! 

If you are going to run scripts and individual agents. I suggest you do the following:
### Setting up Environment
First, you will need to install Virtual Enviroment. Learn more about this here: https://docs.python-guide.org/dev/virtualenvs/ 
```
$ pip install virtualenv
```

Now, run the following command to activate your virtual enviroment! 
```
$ source venv/bin/activate
```

Now that our virtual enviroment is both installed and setup, we will run our config.sh file. Run the following command:
```
$ ./config.sh
```

IF this is giving you 'permission denied' simply run: 
``` 
$ chmod +x ./config.sh
```

Here is the list of dependencies you have installed:
```
numpy==1.14.2
atari-py==0.1.1
gym==0.10.4
ptan==0.3
opencv-python==3.4.0.12
torch 
fastai
torchvision
tensorboard-pytorch==0.7.1
tensorflow==1.7.0
tensorboard==1.7.0
tqdm
```
### Finishing Session
Once you are finished! make sure you deactive this session running the following command:
```
$ deactive
```

## Practice Agent
Run the following command to see an agent at work!
```
$ python3 ./Practice_Agents/agent_one.py
```

MORE TO COME!