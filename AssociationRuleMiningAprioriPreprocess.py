# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:01:21 2020

@author: Santosh Sah
"""

from AssociationRuleMiningAprioriUtils import (importAssociationRuleMiningAprioriDataset, saveAssociationRuleMiningAprioriDataset)

def preprocess():
    
    associationRuleMiningAprioriDataset = importAssociationRuleMiningAprioriDataset("Market_Basket_Optimisation.csv")
    
    saveAssociationRuleMiningAprioriDataset(associationRuleMiningAprioriDataset)

if __name__ == "__main__":
    preprocess()