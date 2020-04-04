#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import argparse
import time


# In[3]:


random.seed(0)


# In[4]:


class Die:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5, 6]

    def roll_a_die(self):
        random.shuffle(self.values)
        return self.values[0]


# In[5]:


class Player:
    def __init__(self):
        self.score = 0

    def increase_score(self, new_score):
        self.score += new_score

    def choice(self):
        choice = input("")
        return choice


# In[6]:


class ComputerPlayer(Player):

    def choice(self):
        h = 0
        if 25 < 100 - self.score:
            h = 25
        else:
            h = 100 - self.score

        if self.score < h:
            return "r"
        elif self.score >= h:
            return "h"


# In[7]:


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.score = 0


# In[8]:


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.die = Die()
        self.turn = 0

    def is_current_player_wins(self):
        if self.players[self.turn].score >= 100:
            return True
        else:
            return False

    def print_turn_choices_menu(self):
        print("")
        print("Player", self.turn + 1, " Score :", self.players[self.turn].score)
        print("(h) Hold Current Score\n(r) Roll a Die\nChoice:", end='')


# In[9]:


def play(self):
    while self.players[self.turn].score < 100:
        self.print_turn_choices_menu()
        choice = self.players[self.turn].choice()
        if choice == 'h':
            self.turn = (self.turn + 1) % len(self.players)
            print("You chose to Hold with score:", self.players[self.turn].score)
        else:
            print("Rolling a Die...")
            score = self.die.roll_a_die()
            print("You Get ", score)
            if score == 1:
                print("it's Next Player Turn:")
                self.turn = (self.turn + 1) % len(self.players)
            else:
                self.players[self.turn].increase_score(score)

    print('Player ', self.turn, ' is the winner')


# In[10]:


class TimedGameProxy(Game):
    def __init__(self, player1, player2, timed):
        super().__init__(player1, player2)
        self.time_start = time.time()
        if timed:
            self.play()
        else:
            super().play()


# In[11]:


def play(self):
    while self.players[self.turn].score < 100 and (time.time() - self.time_start < 60):
        self.print_turn_choices_menu()
        choice = self.players[self.turn].choice()
        if choice == 'h':
            self.turn = (self.turn + 1) % len(self.players)
            print("You chose to Hold with score:", self.players[self.turn].score)
        else:
            print("Rolling a Die...")
            score = self.die.roll_a_die()
            print("You Get ", score)
            if score == 1:
                print("it's Next Player Turn:")
                self.turn = (self.turn + 1) % len(self.players)
            else:
                self.players[self.turn].increase_score(score)

    if time.time() - self.time_start > 60:
        print("Time Out!!")

    if self.players[self.turn].score < self.players[(self.turn + 1) % len(self.players)].score:

        self.turn = (self.turn + 1) % len(self.players)
    print('Player ', self.turn, ' is the winner')


# In[12]:


class PlayerFactory:

    def get_correct_player(self, type_of_player):

        if type_of_player == "computer":
            return ComputerPlayer()

        if type_of_player == "human":
            return HumanPlayer()


# In[17]:


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--player1', help='Player 1 is Human or Computer')
    parser.add_argument('--player2', help='Player 2 is Human or Computer')
    parser.add_argument('--timed', help='to tell if game timed type timed')

    args = parser.parse_args()

    player_factory = PlayerFactory()
    player1 = player_factory.get_correct_player(args.player1)
    player2 = player_factory.get_correct_player(args.player2)
    timed = args.timed
    game = TimedGameProxy(player1, player2, timed == 'timed')


# In[18]:


main()


# In[ ]:




