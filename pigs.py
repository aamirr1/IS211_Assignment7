#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 7"""


import random
import sys


class Game():
    """Pig Game."""
    def __init__(self, player1, player2, dice):
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0
        self.player1.name = 'PLAYER 1'
        self.player2.name = 'PLAYER 2'
        self.dice = dice
        self.score_turn = 0
        flip = random.randint(1, 2) 
        if flip == 1:
            self.cur_player = player1 
            print 'The coin flip determined PLAYER 1 will begin.'
        elif flip == 2:
            self.cur_player = player2 
            print 'The coin flip determined PLAYER 2 will begin.'
        else:
            print 'There was an Error, please try again.'
        self.player_turn()

    def next_turn(self):
        """Players next turn at rolling & total scores."""
        self.score_turn = 0
        if self.player1.score >= 100:
            print 'Player 1 has WON! The score is: ', self.player1.score
            sys.exit()
            newGame()
        elif self.player2.score >= 100:
            print 'Player 2 has WON! The score is: ', self.player2.score
            sys.exit() 
            newGame()
        else:
            if self.cur_player == self.player1:
                self.cur_player = self.player2 
            elif self.cur_player == self.player2:
                self.cur_player = self.player1 
            else:
                print 'Error!!'
        print self.cur_player.name, 'WILL NOW PLAY.' 
        self.player_turn()

    def player_turn(self):
        """A players turn at rolling."""
        print 'The total score for Player 1: ', self.player1.score
        print 'The total score for Player 2: ', self.player2.score
        self.dice.roll()
        if self.dice.val == 1:
            print 'You rolled a ''1'', No points earned, & you lost your turn'
            self.turn_score = 0 
            self.next_turn() 
        else:
            self.score_turn = self.score_turn + self.dice.val 
            print 'You rolled a number: ', self.dice.val 
            print 'You score this turn is: ', self.score_turn
            self.cur_player.choice()
            if self.cur_player.hold == True and self.cur_player.roll == False:
                self.cur_player.score = self.cur_player.score + self.score_turn
                self.next_turn()
            elif self.cur_player.hold == False and self.cur_player.roll == True:
                self.player_turn()

class Players():
    """ Players """
    def __init__(self):
        self.roll = True
        self.hold = False
        self.turn = False
        self.score = 0

    def choice(self):
        """ Game choices"""
        decide = str(raw_input('Do you want to Roll (r) or Hold (h)? '))
        if decide == 'r':
            self.roll = True
            self.hold = False
        elif decide == 'h':
            self.roll = False
            self.hold = True
        else:
            print 'Invalid Entry. Do you want to Roll (r) or Hold (h)? '
            self.choice()

class Dice():
    """ A constructor """
    def __init__(self):
        self.val = int()
        seed = 0 

    def roll(self):
        self.val = random.randint(1, 6)

def newGame():
    """ Game start"""
    start = raw_input('Do you want to play? Y/N ')
    if start == 'Y'.lower():
        player1 = Players()
        player2 = Players()
        dice = Dice()
        new = Game(player1, player2, dice)
    elif start == 'N'.lower():
        print 'Have a nice day!'
        sys.exit()
    else:
        print 'Invalid entry, please try again. Enter ''y'' or ''n'''
        newGame()


def instructions():
    """A function for rules of game."""
    print '\nWelcome to the Pig Dice Game'
    print '-----------------------------''\n'
    print 'How to Play: 2 Players Only'
    print ' ''\n'
    print 'Each turn, a player can roll the dice  to accumulate points. '
    print 'Any number rolled between 2-6 counts towards the total score. '
    print 'If a "1" is rolled points and turn is lost. Each player can choose. '
    print 'to roll or hold at any time unless a "1" is rolled; which at that'
    print 'moment you lose your turn and points.'
    print 'The player who totals 100 points WINS!'
    print ' ''\n'


if __name__ == '__main__':
    instructions()
    newGame()
