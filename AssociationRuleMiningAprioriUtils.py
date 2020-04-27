# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:00:55 2020

@author: Santosh Sah
"""

"""
importing the libraries
"""

import pandas as pd
import pickle

"""
Import dataset and read specific column. Split the dataset in training and testing set.
"""
def importAssociationRuleMiningAprioriDataset(associationRuleMiningAprioriDatasetFileName):
    
    associationRuleMiningAprioriDataset = pd.read_csv(associationRuleMiningAprioriDatasetFileName, header = None)
    
    #the raw dataset has a record in such a way that each row is considered as a transaction doen by a user.
    #apriori algorithms expects input as list of lists
    #all the data is in list and all the transaction will be as a list.
    #dataset has 7501 row and 20 columns
    aprioriTransaction = []
    
    for i in range(0, 7501):
        
        aprioriTransaction.append([str(associationRuleMiningAprioriDataset.values[i, j]) for j in range(0,20)])
        
    return aprioriTransaction

"""
save AssociationRuleMiningAprioriDataset as a pickel file
"""
def saveAssociationRuleMiningAprioriDataset(associationRuleMiningAprioriDataset):
    
    #Write AssociationRuleMiningAprioriDataset in a picke file
    with open("AssociationRuleMiningAprioriDataset.pkl",'wb') as AssociationRuleMiningAprioriDataset_Pickle:
        pickle.dump(associationRuleMiningAprioriDataset, AssociationRuleMiningAprioriDataset_Pickle, protocol = 2)

"""
read AssociationRuleMiningAprioriDataset from pickel file
"""
def readAssociationRuleMiningAprioriDataset():
    
    #load AssociationRuleMiningAprioriDataset object
    with open("AssociationRuleMiningAprioriDataset.pkl","rb") as AssociationRuleMiningAprioriDataset:
        associationRuleMiningAprioriDataset = pickle.load(AssociationRuleMiningAprioriDataset)
    
    return associationRuleMiningAprioriDataset

"""
save AssociationRuleMiningAprioriRules as a pickel file
"""
def saveAssociationRuleMiningAprioriRules(associationRuleMiningAprioriRules):
    
    #Write AssociationRuleMiningAprioriRules in a picke file
    with open("AssociationRuleMiningAprioriRules.pkl",'wb') as AssociationRuleMiningAprioriRules_Pickle:
        pickle.dump(associationRuleMiningAprioriRules, AssociationRuleMiningAprioriRules_Pickle, protocol = 2)

"""
read AssociationRuleMiningAprioriRules from pickel file
"""
def readAssociationRuleMiningAprioriRules():
    
    #load AssociationRuleMiningAprioriRules object
    with open("AssociationRuleMiningAprioriRules.pkl","rb") as AssociationRuleMiningAprioriRules:
        associationRuleMiningAprioriRules = pickle.load(AssociationRuleMiningAprioriRules)
    
    return associationRuleMiningAprioriRules

