# Deep-Learning-implementation-of-Chatbot

## Problem Statement:
The most effective uses of dialog systems in the recent times have been in personalized recommendation systems where the system acts as a goal-oriented personal assistant or a bot by understanding the user’s request and providing the user with the necessary information accordingly. The goal is to build a goal-driven dialogue based chat bot which has been trained for Spotify music suggestion

## Architecture:

## Requirements:

Install the following packages:
 - Gensim
 - Tensorflow 1.0
 - Python 3.5
 - CUDA (for running on GPU systems)
 
## Download data:

```bash
bash download.sh
```

## Train the model:

```bash
python3 train.py
# training stops when accuracy on dev set becomes > 0.99
#  trained model is saved to ckpt/
```

## Interact with the model:

```bash
python3 interact.py
# checkpoint from ckpt/ is loaded
#  start interaction
```

## Sample Interaction

 

