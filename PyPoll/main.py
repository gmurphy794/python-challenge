import csv
import operator

csvpath = ('/Users/gmurphy794/Documents/GitHub/python-challenge/PyPoll/election_data.csv')
file = open("pollfile.txt", 'w')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    candidates = []
    candidates2 = []
    candidateVotes=[]
    candidateVotesP = []
    
    
    for row in csvreader:
        candidates2.append(row[2])
        if row[2] not in candidates:
            candidates.append(str(row[2]))
            candidateVotes.append(0)
   
    for i in range(len(candidates2)):
        if candidates2[i] == candidates[0]:
            candidateVotes[0] += 1
        elif candidates2[i] == candidates[1]:
            candidateVotes[1] += 1
        elif candidates2[i] == candidates[2]:
            candidateVotes[2] += 1
        else:
            candidateVotes[3] += 1
    
    candidateDic = {}
    for i in range(len(candidates)):
        candidateDic[candidates[i]] = candidateVotes[i]
    sorted_d = sorted(candidateDic.items(), key=operator.itemgetter(1), reverse=True) 
        
        
    for x in candidateVotes:
        candidateVotesP.append(round((x/len(candidates2))*100))
    candidateVotesP.sort(reverse = True)


    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(len(candidates2)))
    print("----------------------------")
    for i in range(len(candidates)):
        print(str(sorted_d[i][0]) + ": " 
              + str(candidateVotesP[i]) + ".000% " + "(" + str(sorted_d[i][1]) + ")" )
    print("----------------------------")
    print("Winner: " + str(sorted_d[0][0]))
    
    file.write("Election Results" + "\n")
    file.write("----------------------------" + "\n")
    file.write("Total Votes: " + str(len(candidates2)) + "\n")
    file.write("----------------------------" + '\n')
    for i in range(len(candidates)):
        file.write(str(sorted_d[i][0]) + ": " 
              + str(candidateVotesP[i]) + ".000% " + "(" + str(sorted_d[i][1]) + ")" + '\n')
    file.write("----------------------------" + '\n')
    file.write("Winner: " + str(sorted_d[0][0]))    
    
    
    
    
    
    
    
    

    