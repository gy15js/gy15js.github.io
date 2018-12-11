# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:56:50 2018

@author: gy15js
"""

#----------------------------------------------------------------------------#
##############################################################################
################################  IMPORTS  ###################################

import random as r

#----------------------------------------------------------------------------#
##############################################################################
##########################  CLASS BUILDING  ##################################

class Agent():
    
        def __init__ (self, environment, agents, r_seed, y, x):
            #explain what def__init__ is from the book
 
############################  Y & X VALUES  ##################################           
            #self._y = r.randint(0,100)
            #self._x = r.randint(0,100)
            '''removed the above to ensure the webpage values are used'''
            self._y = y
            self._x = x
            
            if (x == None):
                self._x = r.randint(0,100)
            else:
                self._x = x
                
            if (y == None):
                self._y = r.randint(0,100)
            else:
                self._y = y
 
############################  ENVIRONMENT  ###################################           
        #def __init__(environment): added the two together for init to work
            self.environment = environment
            self.store = 0
            self.agents = agents
            self.store = 0
            self.r_seed = 1
            self.store =  r.randint(5,20)
#changed the store so that the agents will be able to move from the start

##############################  MOVEMENT  ####################################
        def move(self):
            """if r.random() < 0.5:
                self._y = (self._y + 1) % 100
                self.store -= 5
            else:
                self._y = (self._y - 1) % 100
                self.store -= 5
            if r.random() < 0.5:
                self._x = (self._x + 1) % 100
                self.store -= 5
            else:
                self._x = (self._x - 1) % 100
                self.store -= 5
                
            
            if self.store <= 5:
                self._y = (self._y + 0) % 100 
                self.store + 5

            if self.store <= 5:
                self._x = (self._x + 0) % 100
                self.store + 5
                
            if self.store >= 100:
                self._y = (self._y + 2) % 100    
                self.store - 20

            if self.store >= 100:
                self._x = (self._x + 2) % 100
                self.store - 20"""
                
#updated this move function so that the store changes with each movement
#now they either move normally or in a 'boost' mode when they have loads
#of energy
                
#            print('store:'+str(self.store)) this was to test
            if self.store >= 5 and self.store < 100:
                print('normal')
                #kept these in just so the model is visably developing
                self.store -= 5
                
                if r.random() < 0.5:
                    self._y = (self._y + 1) % 100
                else:
                    self._y = (self._y - 1) % 100
                  
                if r.random() < 0.5:
                    self._x = (self._x + 1) % 100
                else:
                    self._x = (self._x - 1) % 100
                   
                    
            elif self.store > 100 :
                print('boost')
                #kept in for the same reason above
                self.store -= 10
                
                if r.random() < 0.5:
                    self._y = (self._y + 2) % 100     
                else:
                    self._y = (self._y - 2) % 100 
                if r.random() < 0.5:
                    self._x = (self._x + 2) % 100
                else:
                    self._x = (self._x - 2) % 100
#            print('store:'+str(self.store)) this was to test
                 
#added extra code so that each move takes the agent store down by 5
#also added if the store is below 5 then slower movement
#also added if high store then move quicker
                
###########################  EAT ENVIRONMENT  ################################               
        def eat(self):
#            if  self.environment[self._y][self._x] > 10:
#                self.environment[self._y][self._x] -= 10
#                self.store += 10
#EXTRA CODING

            if  self.store <= 150:
                if self.environment[self._y][self._x] > 15:
                    self.environment[self._y][self._x] -= 15
                    self.store += 15
            else:
                print('not hungry!')
                #was a test but now kept in to see when agents are full

#the above tells the agents if store is low eat more and vice versa          
            
#########################  NEIGHBOURHOOD SHARE  ##############################           
         #this method tells the agents to share with their nearby neighbours 
         #that are closest
        def share_with_neighbours (self, neighbourhood):
            for agent in self.agents:
                dist = self.distance_between(agent)
                #for agents, find the distance between them
            if dist <= neighbourhood: 
                if  self.store >= 20:
                #if the distance is lower than or equals to the neighbourhood
                    sum = self.store + agent.store
                    ave = sum/2
                    self.store = ave
                    #averaging self.store and agent.store out
                    agent.store = ave
                #print("sharing" + str(dist) + "" + str(ave)) 
                '''this is just to make sure it works, now that it does can 
                comment out'''
 
#added extra if in the distance to say only share if store is above 20          

###########################  DISTANCE BETWEEN  ###############################                
        def distance_between (self,agent):
            return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
        