import pandas as pd
# from dominance_analysis import Dominance
# import openpyxl as openpyxl

# load CSV from 
data = pd.read_csv(r'C:\Users\blais\Downloads\NDA.csv')

# print(data)

# Data for concepts and their criteria values
data = {
    'Concept': ['A', 'B', 'C', 'D'],
    'Cost': [8, 6, 9, 7],
    'Feasibility': [7, 9, 6, 8],
    'User Satisfaction': [9, 8, 7, 6],
    'Scalability': [6, 7, 8, 9],
    'Performance': [7, 9, 6, 8],
    'Security': [8, 7, 9, 6]
}

# Define data for each concept and its criteria scores
concepts = {
    'A': [8, 7, 9, 6, 7, 8],
    'B': [6, 9, 8, 7, 9, 7],
    'C': [9, 6, 7, 8, 6, 9],
    'D': [7, 8, 6, 9, 8, 6]
}

# Define empty lists to store dominated and non-dominated concepts
dominated = []
non_dominated = []

for name1, score1 in concepts.items():
    dominated = False

    for name2, score2 in concepts.items():
        if name1!= name2:
            
            # Check if concept1 dominates concept2
            if all(s2 >= s1 for s1, s2 in zip(score1, score2)) and any (s2 > s1 for s1,s2 in zip(score1, score2)):
                dominated = True
                break

    if  dominated:
        dominated.append(name1)
    else:
        non_dominated.append(name1)



print( dominated)
print( non_dominated)
