import numpy as np

def realWorldSimulator(preference_file1, preference_file2, match_file1, match_file2):

    candPrefs = np.loadtxt(preference_file1, dtype=int, delimiter=',')
    employerPrefs = np.loadtxt(preference_file2, dtype=int, delimiter=',')

    candMatches = np.zeros((len(candPrefs), 3), dtype=int)
    candMatches -= 1
    employerMatches =  np.zeros((len(employerPrefs), 3), dtype=int)

    candsAvailable = np.zeros(len(candPrefs), dtype=int)
    candsAvailable += 1

    numPrefsForEmployer = np.zeros(len(employerPrefs), dtype=int)

    for i in range(len(employerPrefs)):
        numPrefsForEmployer[i] = np.sum(employerPrefs[i]>0)


    employerHasCandidate = np.zeros(len(employerPrefs), dtype=int)

    # candsAvailable: 1 means available, 0 means taken.

    # Employers 0-32 are High Class, chooses top prefs (top 3)
    # Employers 33-65 are Medium Class, chooses middle prefs (top 3 after 33% prefs)
    # Employers 66-99 are Low Class, chooses low prefs (top 3 after 66% prefs)


    # 3 Rounds

    for i in range(3):

        for k in range(len(candPrefs)):
            if (candsAvailable[k] == 0):
                candMatches[k][i] = -2

        for j in range(len(employerMatches)//3):

            if (employerHasCandidate[j] == 1):
                employerMatches[j][i] = -2
                continue

            offerCand = employerPrefs[j][i]

            if (candsAvailable[offerCand-1] == 1):
                candMatches[offerCand-1][i] = j+1
                employerMatches[j][i] = offerCand
                candsAvailable[offerCand-1] = 0
                employerHasCandidate[j] = 1

            else:
                employerMatches[j][i] = -1

        for j in range(len(employerMatches)//3, 2*(len(employerMatches)//3)):

            if (employerHasCandidate[j] == 1):
                employerMatches[j][i] = -2
                continue

            offerCand = employerPrefs[j][ int(numPrefsForEmployer[j]*0.33) + i]

            if (candsAvailable[offerCand-1] == 1):
                candMatches[offerCand-1][i] = j+1
                employerMatches[j][i] = offerCand
                candsAvailable[offerCand-1] = 0
                employerHasCandidate[j] = 1

            else:
                employerMatches[j][i] = -1

        for j in range(2*(len(employerMatches)//3), len(employerMatches)):

            if (employerHasCandidate[j] == 1):
                employerMatches[j][i] = -2
                continue

            offerCand = employerPrefs[j][ int(numPrefsForEmployer[j]*0.66) + i]

            if (candsAvailable[offerCand-1] == 1):
                candMatches[offerCand-1][i] = j+1
                employerMatches[j][i] = offerCand
                candsAvailable[offerCand-1] = 0
                employerHasCandidate[j] = 1

            else:
                employerMatches[j][i] = -1

    candMatches2 = np.zeros( (len(candMatches), 3), dtype='|S5')

    for i in range(len(candMatches)):
        for j in range(len(candMatches[i])):
            if (candMatches[i][j] == -1):
                candMatches2[i][j] = '-1'
            elif (candMatches[i][j] == -2):
                candMatches2[i][j] = '-2'
            else:
                candMatches2[i][j] = 'e' + str(candMatches[i][j])



    employerMatches2 = np.zeros( (len(employerMatches), 3), dtype='|S5')

    for i in range(len(employerMatches)):
        for j in range(len(employerMatches[i])):
            employerMatches2[i][j] = str(employerMatches[i][j])


    np.savetxt(match_file1, candMatches2, fmt='%s', delimiter=",")
    np.savetxt(match_file2, employerMatches2, fmt='%s', delimiter=",")

def matchSimulator(preference_file1, preference_file2, match_file1, match_file2):

    candPrefs = np.loadtxt(preference_file1, dtype=int, delimiter=',')
    employerPrefs = np.loadtxt(preference_file2, dtype=int, delimiter=',')

    candMatches = np.zeros((len(candPrefs), 3), dtype=int)
    candMatches -= 1
    employerMatches =  np.zeros((len(employerPrefs), 3), dtype=int)

    candsAvailable = np.zeros(len(candPrefs), dtype=int)
    candsAvailable += 1

    numPrefsForEmployer = np.zeros(len(employerPrefs), dtype=int)

    for i in range(len(employerPrefs)):
        numPrefsForEmployer[i] = np.sum(employerPrefs[i]>0)


    employerHasCandidate = np.zeros(len(employerPrefs), dtype=int)

    # candsAvailable: 1 means available, 0 means taken.

    # Employers 0-32 are High Class, chooses top prefs (top 3)
    # Employers 33-65 are Medium Class, chooses middle prefs (top 3 after 33% prefs)
    # Employers 66-99 are Low Class, chooses low prefs (top 3 after 66% prefs)


    # 3 Rounds

    for i in range(3):

        for k in range(len(candMatches)):
            if (candsAvailable[k] == 0):
                candMatches[k][i] = -2

        for j in range(len(employerMatches)):

            if (employerHasCandidate[j] == 1):
                employerMatches[j][i] = -2
                continue

            offerCand = employerPrefs[j][i]

            if (candsAvailable[offerCand-1] == 1):
                candMatches[offerCand-1][i] = j+1
                employerMatches[j][i] = offerCand
                candsAvailable[offerCand-1] = 0
                employerHasCandidate[j] = 1

            else:
                employerMatches[j][i] = -1

    candMatches2 = np.zeros( (len(candMatches), 3), dtype='|S5')

    for i in range(len(candMatches)):
        for j in range(len(candMatches[i])):
            if (candMatches[i][j] == -1):
                candMatches2[i][j] = '-1'
            elif (candMatches[i][j] == -2):
                candMatches2[i][j] = '-2'
            else:
                candMatches2[i][j] = 'e' + str(candMatches[i][j])



    employerMatches2 = np.zeros( (len(employerMatches), 3), dtype='|S5')

    for i in range(len(employerMatches)):
        for j in range(len(employerMatches[i])):
            employerMatches2[i][j] = str(employerMatches[i][j])


    np.savetxt(match_file1, candMatches2, fmt='%s', delimiter=",")
    np.savetxt(match_file2, employerMatches2, fmt='%s', delimiter=",")

def dataPrep(match_file1, match_file2, preference_file1, preference_file2):

    candMatches = np.loadtxt(match_file1, dtype=str, delimiter=',')
    employerMatches = np.loadtxt(match_file2, dtype=str, delimiter=',')


    denseCandMatches = np.zeros(candMatches.shape, dtype=int)
    denseEmployerMatches = np.zeros(employerMatches.shape, dtype=int)


    print(candMatches[0])
    print(employerMatches[0])

    for i in range(len(candMatches)):
        tempIndex = 0
        for j in range(len(candMatches[i])):
            if (candMatches[i][j] == '-1' or candMatches[i][j] == ''):
                continue
            else:
                denseCandMatches[i][tempIndex] = int(candMatches[i][j][1:])
                tempIndex += 1

    for i in range(len(employerMatches)):
        tempIndex = 0
        for j in range(len(employerMatches[i])):
            if (employerMatches[i][j] == '-1' or employerMatches[i][j] == ''):
                continue
            else:
                denseEmployerMatches[i][tempIndex] = int(employerMatches[i][j])
                tempIndex += 1


    np.savetxt(preference_file1, denseCandMatches, fmt='%d', delimiter=",")
    np.savetxt(preference_file2, denseEmployerMatches, fmt='%d', delimiter=",")

# Used for Simulator
def calcSimulatorMetrics(preference_file1, preference_file2, match_file1, match_file2, numberOfTopJobsToConsider, penalty):

    candPrefs = np.loadtxt(preference_file1, dtype='|S5', delimiter=',')
    employerPrefs = np.loadtxt(preference_file2, dtype='|S5', delimiter=',')
    candMatches = np.loadtxt(match_file1, dtype='|S5', delimiter=',')
    employerMatches = np.loadtxt(match_file2, dtype='|S5', delimiter=',')


    for i in range(len(candPrefs)):
        for j in range(len(candPrefs[i])):
            if (candPrefs[i][j] != '0'):
                candPrefs[i][j] = 'e' + candPrefs[i][j]
            else:
                candPrefs[i][j] = ''

    for i in range(len(employerPrefs)):
        for j in range(len(employerPrefs[i])):
            if (employerPrefs[i][j] == '0'):
                employerPrefs[i][j] = ''

    print candPrefs[0]
    print employerPrefs[0]
    print candMatches[0]
    print employerMatches[0]


    # Calculate Metric for Employer.

    # 100x100
    employerMetrics = np.zeros( (len(employerMatches)+4, numberOfTopJobsToConsider) , dtype=float)



    # Calc displacement for the first n matches

    for j in range(numberOfTopJobsToConsider):

        for i in range(len(employerMatches)):

            if (employerMatches[i][j] == '-2'):
                employerMetrics[i][j] = -2
                continue

            if (employerMatches[i][j] == '-1'):
                employerMetrics[i][j] = -1

            elif (employerMatches[i][j] == ''):
                employerMetrics[i][j] = -2

            else:

                # Calc penalty for no match

                totalPenalty = 0

                for k in range(j):
                    if (employerMatches[i][k] == '-1'):
                        totalPenalty += penalty


                for k in range(len(employerPrefs[i])):
                    if (employerMatches[i][j] == employerPrefs[i][k]):
                        distance = k
                        employerMetrics[i][j] = distance + totalPenalty

        sum = 0
        count = 0

        for i in range(len(employerMatches)):
            if (employerMetrics[i][j] != -1 and employerMetrics[i][j] != -2):
                sum += employerMetrics[i][j]
                count += 1

        employerMetrics[len(employerMetrics)-4][j] = sum
        if (count != 0):
            employerMetrics[len(employerMetrics)-3][j] = sum/count

    # Count jobs that have no matches
    for j in range(numberOfTopJobsToConsider):
        total = 0.0
        noMatchCount = 0.0

        for i in range(len(employerMatches)):
            if (employerMatches[i][j] != ''):
                total += 1
            if (employerMatches[i][j] == '-1'):
                noMatchCount += 1

        if (total == 0):
            break

        else:
            employerMetrics[len(employerMetrics)-2][j] = noMatchCount
            employerMetrics[len(employerMetrics)-1][j] = (noMatchCount/total)*100

    np.savetxt('employerMetrics.csv', employerMetrics, fmt='%f', delimiter=',')




    # Calculate Metric for Candidate.

    # 100x100
    candMetrics = np.zeros( (len(candMatches)+4, numberOfTopJobsToConsider) , dtype=float)

    # Calc displacement for the first n matches

    for j in range(numberOfTopJobsToConsider):

        for i in range(len(candMatches)):

            if (candMatches[i][j] == '-2'):
                candMetrics[i][j] = -2
                continue

            if (candMatches[i][j] == '-1'):
                candMetrics[i][j] = -1

            elif (candMatches[i][j] == ''):
                candMetrics[i][j] = -2

            else:

                # Calc penalty for no match

                totalPenalty = 0

                for k in range(j):
                    if (candMatches[i][k] == '-1'):
                        totalPenalty += penalty


                for k in range(len(candPrefs[i])):
                    if (candMatches[i][j] == candPrefs[i][k]):
                        distance = k
                        candMetrics[i][j] = distance + totalPenalty

        sum = 0
        count = 0

        for i in range(len(candMatches)):
            if (candMetrics[i][j] != -1 and candMetrics[i][j] != -2):
                sum += candMetrics[i][j]
                count += 1

        candMetrics[len(candMetrics)-4][j] = sum
        if (count != 0):
            candMetrics[len(candMetrics)-3][j] = sum/count

    # Count jobs that have no matches
    for j in range(numberOfTopJobsToConsider):
        total = 0.0
        noMatchCount = 0.0

        for i in range(len(candMatches)):
            if (candMatches[i][j] != ''):
                total += 1
            if (candMatches[i][j] == '-1'):
                noMatchCount += 1

        if (total == 0):
            break

        else:
            candMetrics[len(candMetrics)-2][j] = noMatchCount
            candMetrics[len(candMetrics)-1][j] = (noMatchCount/total)*100

    np.savetxt('candMetrics.csv', candMetrics, fmt='%f', delimiter=',')


def calcMixedSimulatorMetrics(preference_file1, preference_file2, preference_file3, preference_file4, match_file1, match_file2, numberOfTopJobsToConsider, penalty):

    candPrefs = np.loadtxt(preference_file1, dtype='|S5', delimiter=',')
    employerPrefs = np.loadtxt(preference_file2, dtype='|S5', delimiter=',')
    lmfCandPrefs = np.loadtxt(preference_file3, dtype='|S5', delimiter=',')
    lmfEmployerPrefs = np.loadtxt(preference_file4, dtype='|S5', delimiter=',')
    candMatches = np.loadtxt(match_file1, dtype='|S5', delimiter=',')
    employerMatches = np.loadtxt(match_file2, dtype='|S5', delimiter=',')


    for i in range(len(candPrefs)):
        for j in range(len(candPrefs[i])):
            if (candPrefs[i][j] != '0'):
                candPrefs[i][j] = 'e' + candPrefs[i][j]
            else:
                candPrefs[i][j] = ''

    for i in range(len(employerPrefs)):
        for j in range(len(employerPrefs[i])):
            if (employerPrefs[i][j] == '0'):
                employerPrefs[i][j] = ''

    for i in range(len(lmfCandPrefs)):
        for j in range(len(lmfCandPrefs[i])):
            if (lmfCandPrefs[i][j] != '0'):
                lmfCandPrefs[i][j] = 'e' + lmfCandPrefs[i][j]
            else:
                lmfCandPrefs[i][j] = ''

    for i in range(len(lmfEmployerPrefs)):
        for j in range(len(lmfEmployerPrefs[i])):
            if (lmfEmployerPrefs[i][j] == '0'):
                lmfEmployerPrefs[i][j] = ''

    print candPrefs[0]
    print employerPrefs[0]
    print candMatches[0]
    print employerMatches[0]


    # Calculate Metric for Employer.

    # 100x100
    employerMetrics = np.zeros( (len(employerMatches)+4, numberOfTopJobsToConsider) , dtype=float)



    # Calc displacement for the first n matches

    for j in range(numberOfTopJobsToConsider):

        for i in range(len(employerMatches)):

            if (employerMatches[i][j] == '-2'):
                employerMetrics[i][j] = -2
                continue

            if (employerMatches[i][j] == '-1'):
                employerMetrics[i][j] = -1

            elif (employerMatches[i][j] == ''):
                employerMetrics[i][j] = -2

            else:

                # Calc penalty for no match

                totalPenalty = 0

                for k in range(j):
                    if (employerMatches[i][k] == '-1'):
                        totalPenalty += penalty

                found = False
                for k in range(len(employerPrefs[i])):
                    if (employerMatches[i][j] == employerPrefs[i][k]):
                        distance = k
                        employerMetrics[i][j] = distance + totalPenalty
                        found = True

                # Mixed
                if (found == False):
                    for k in range(len(lmfEmployerPrefs[i])):
                        if (employerMatches[i][j] == lmfEmployerPrefs[i][k]):
                            distance = k
                            employerMetrics[i][j] = distance/10 + totalPenalty
                            found = True

        sum = 0
        count = 0

        for i in range(len(employerMatches)):
            if (employerMetrics[i][j] != -1 and employerMetrics[i][j] != -2):
                sum += employerMetrics[i][j]
                count += 1

        employerMetrics[len(employerMetrics)-4][j] = sum
        if (count != 0):
            employerMetrics[len(employerMetrics)-3][j] = sum/count

    # Count jobs that have no matches
    for j in range(numberOfTopJobsToConsider):
        total = 0.0
        noMatchCount = 0.0

        for i in range(len(employerMatches)):
            if (employerMatches[i][j] != ''):
                total += 1
            if (employerMatches[i][j] == '-1'):
                noMatchCount += 1

        if (total == 0):
            break

        else:
            employerMetrics[len(employerMetrics)-2][j] = noMatchCount
            employerMetrics[len(employerMetrics)-1][j] = (noMatchCount/total)*100

    np.savetxt('employerMetrics.csv', employerMetrics, fmt='%f', delimiter=',')




    # Calculate Metric for Candidate.

    # 100x100
    candMetrics = np.zeros( (len(candMatches)+4, numberOfTopJobsToConsider) , dtype=float)

    # Calc displacement for the first n matches

    for j in range(numberOfTopJobsToConsider):

        for i in range(len(candMatches)):

            if (candMatches[i][j] == '-2'):
                candMetrics[i][j] = -2
                continue

            if (candMatches[i][j] == '-1'):
                candMetrics[i][j] = -1

            elif (candMatches[i][j] == ''):
                candMetrics[i][j] = -2

            else:

                # Calc penalty for no match

                totalPenalty = 0

                for k in range(j):
                    if (candMatches[i][k] == '-1'):
                        totalPenalty += penalty

                found = False
                for k in range(len(candPrefs[i])):
                    if (candMatches[i][j] == candPrefs[i][k]):
                        distance = k
                        candMetrics[i][j] = distance + totalPenalty
                        found = True

                # Mixed
                if (found == False):
                    for k in range(len(lmfCandPrefs[i])):
                        if (candMatches[i][j] == lmfCandPrefs[i][k]):
                            distance = k
                            candMetrics[i][j] = distance/10 + totalPenalty
                            found = True

        sum = 0
        count = 0

        for i in range(len(candMatches)):
            if (candMetrics[i][j] != -1 and candMetrics[i][j] != -2):
                sum += candMetrics[i][j]
                count += 1

        candMetrics[len(candMetrics)-4][j] = sum
        if (count != 0):
            candMetrics[len(candMetrics)-3][j] = sum/count

    # Count jobs that have no matches
    for j in range(numberOfTopJobsToConsider):
        total = 0.0
        noMatchCount = 0.0

        for i in range(len(candMatches)):
            if (candMatches[i][j] != ''):
                total += 1
            if (candMatches[i][j] == '-1'):
                noMatchCount += 1

        if (total == 0):
            break

        else:
            candMetrics[len(candMetrics)-2][j] = noMatchCount
            candMetrics[len(candMetrics)-1][j] = (noMatchCount/total)*100

    np.savetxt('candMetrics.csv', candMetrics, fmt='%f', delimiter=',')


def calcVacancyMetrics(match_file1, match_file2, numberOfTopJobsToConsider):
    candMatches = np.loadtxt(match_file1, dtype='|S5', delimiter=',')
    employerMatches = np.loadtxt(match_file2, dtype='|S5', delimiter=',')

    print candMatches[0]
    print employerMatches[0]


    # Calculate Metric for Employer.
    employerMetrics = np.zeros( (2, numberOfTopJobsToConsider) , dtype=float)

    # Count jobs that have no matches
    for j in range(numberOfTopJobsToConsider):
        total = 0.0
        noMatchCount = 0.0

        for i in range(len(employerMatches)):
            if (employerMatches[i][j] != ''):
                total += 1
            if (employerMatches[i][j] == '-1'):
                noMatchCount += 1

        if (total == 0):
            break

        else:
            employerMetrics[0][j] = noMatchCount
            employerMetrics[1][j] = (noMatchCount/total)*100


    # Calculate Metric for Candidate.
    candMetrics = np.zeros( (2, numberOfTopJobsToConsider) , dtype=float)

    # Count jobs that have no matches
    for j in range(numberOfTopJobsToConsider):
        total = 0.0
        noMatchCount = 0.0

        for i in range(len(candMatches)):
            if (candMatches[i][j] != ''):
                total += 1
            if (candMatches[i][j] == '-1'):
                noMatchCount += 1

        if (total == 0):
            break

        else:
            candMetrics[0][j] = noMatchCount
            candMetrics[1][j] = (noMatchCount/total)*100

    np.savetxt('employerVacancy.csv', employerMetrics, fmt='%f', delimiter=',')
    np.savetxt('candVacancy.csv', candMetrics, fmt='%f', delimiter=',')



def main():

    #----- Normal DAA/LMF Simulation -----
    #dataPrep('candidate_matches.csv', 'employer_matches.csv', "dense_candidate_matches.csv", "dense_employer_matches.csv")
    #matchSimulator('dense_candidate_matches.csv','dense_employer_matches.csv', 'candidate_simulated_matches.csv', 'employer_simulated_matches.csv')

    #----- Mixed DAA Simulation -----
    #dataPrep('new_candidate_matches.csv', 'new_employer_matches.csv', "dense_candidate_matches.csv", "dense_employer_matches.csv")
    #matchSimulator('dense_candidate_matches.csv','dense_employer_matches.csv', 'candidate_simulated_matches.csv', 'employer_simulated_matches.csv')

    #----- Real World Simulation -----
    #realWorldSimulator('dense_candidate_prefs.csv','dense_employer_prefs.csv', 'candidate_simulated_matches.csv', 'employer_simulated_matches.csv')
    #return

    #----- Vacancy Metrics -----
    #calcVacancyMetrics('candidate_simulated_matches.csv', 'employer_simulated_matches.csv', 3)
    #return

main()
