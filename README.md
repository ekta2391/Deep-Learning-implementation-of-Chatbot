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
Download the English Wikipedia dump data for training the word2vec model. Exceute the following command to download the data

```bash
bash download.sh
```

## Train the model:
To train the model on Spotify dialogue based data, run the below command. The accuarcy threshold has been set to 0.94 after which the model's training is stopped and the model is saved to a checkpoint folder ckpt.

```bash
python3 train.py

```

## Interact with the model:
Once the model has been trained on the Spotify dataset, you can now interact with the bot by running the below command. The checkpoint is loaded from the ckpt folder. 
```bash
python3 interact.py

```

## Sample Interaction


 
  
 
 
  
  
 



 

