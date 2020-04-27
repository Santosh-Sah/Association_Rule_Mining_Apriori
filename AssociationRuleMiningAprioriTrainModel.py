# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:01:43 2020

@author: Santosh Sah
"""
from apyori import apriori
import pandas as pd

from AssociationRuleMiningAprioriUtils import (readAssociationRuleMiningAprioriDataset)

"""
Train AssociationRuleMiningApriori model 
"""
def trainAssociationRuleMiningApriori():
    
    associationRuleMiningAprioriDataset = readAssociationRuleMiningAprioriDataset()
    
    #first argument of the apriori method is transaction whichis in the for of list of lists.
    #Other parameters values depends on your dataset. Example min_support will be different if your dataset 1000 records to the dataset with 1000000 records.
    #support of a set of items is equal to the number of transactions of the set of items diveided by the total number of transaction. we need to provide 
    #the minimum support in our rule.The items which will appear in the rules must the support greater than this minimum support.
    #to choose support we need to figure out the products which purchased frequently, atleast three four times a day. It also depends upon your business goal.
    #We create the rules based on the a miminum support. If you do not convienced with the rule then you can change the min support and create new rules.
    #product purchased three times a day 7 days in a wwek. 7*3/7501
    #minimum confidence. Example .8 means that the rule must be correct 80% of time. It is very difficult to get the rule which is correct 80%of all time.
    #Hence let start the minimum confidence from 0.2.
    #we can try dufferent value of minimum lift. But there must be some rule to define the minimum lift. Lets try with 3. 
    associationRuleMiningAprioriRules =apriori(associationRuleMiningAprioriDataset, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
    
    results = list(associationRuleMiningAprioriRules)
    
    resultDataframe = pd.DataFrame(results)
    
    resultDataframe.to_csv("associationRuleMiningAprioriRules.csv", index = False)
    

if __name__ == "__main__":
    trainAssociationRuleMiningApriori()