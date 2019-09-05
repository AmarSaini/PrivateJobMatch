import numpy as np

# n = num candidates
# m = num employers
def createDatasets(n, m):

    # ---------- Pool of type 1 or 2 candidates and employers ----------

    candidatePool = np.random.randint(1, 3, n)
    employerPool = np.random.randint(1, 3, m)

    print(candidatePool)
    print(employerPool)

    print(np.sum(candidatePool == 1))
    print(np.sum(candidatePool == 2))
    print(np.sum(employerPool == 1))
    print(np.sum(employerPool == 2))

    # ---------- Candidate Prefs first ----------

    print("Generating Candidate Prefs")
    candidatePrefs = np.zeros((n, m//10), dtype=int)
    print(candidatePrefs.shape)
    print(candidatePrefs.shape[1])

    mySample = np.zeros(candidatePrefs.shape[1], dtype=int)

    for i in range(n):

        # Select 10 random distinct employer ids.
        samplePool = list(range(0,100))
        #print(samplePool)
        for j in range(len(mySample)):
            randIndex = np.random.randint(0, len(samplePool))
            mySample[j] = samplePool[randIndex]
            samplePool.remove(samplePool[randIndex])

        #print(mySample)

        prefNum = 0

        # rank each employer, first type 1's, then type 2's.
        for j in range(len(mySample)):
            if (candidatePool[i] == employerPool[mySample[j]]):
                candidatePrefs[i][prefNum] = mySample[j]
                prefNum += 1

        for j in range(len(mySample)):
            if (candidatePool[i] != employerPool[mySample[j]]):
                candidatePrefs[i][prefNum] = mySample[j]
                prefNum += 1

        #print(candidatePrefs[i])

        # Checked if ranked by type
        #for j in range(len(candidatePrefs[i])):
            #print(employerPool[candidatePrefs[i][j]])

    # ---------- Employer prefs based on candidates' prefs ----------
    # m by n in case all n candidates rank a specific employer.

    print("Generating Employer Prefs")
    employerPrefs = np.zeros((m, n), dtype=int)
    print(employerPrefs.shape)
    print(employerPrefs.shape[1])

    for i in range(m):

        mySample = []

        # Find all candidates who ranked this employer

        for j in range(len(candidatePrefs)):
            for k in range(len(candidatePrefs[j])):
                if (candidatePrefs[j][k] == i):
                    mySample.append(j)
                    #print("{} {}".format(j, candidatePrefs[j]))
        #print(mySample)
        np.random.shuffle(mySample)
        #print(mySample)

        prefNum = 0

        # rank each employer, first type 1's, then type 2's.
        for j in range(len(mySample)):
            if (employerPool[i] == candidatePool[mySample[j]]):
                employerPrefs[i][prefNum] = mySample[j]
                prefNum += 1

        for j in range(len(mySample)):
            if (employerPool[i] != candidatePool[mySample[j]]):
                employerPrefs[i][prefNum] = mySample[j]
                prefNum += 1

        # Correct id's (First id should be 1, not 0. 0 is used to mark no candidate/end of preferences.)
        # We need to do this for each employer individually due to non-constant number of preferences for employers.
        # (Extra 0's at the end of preference list must not be incremented by 1, since they are used to mark the end of preferences)
        for j in range(len(mySample)):
            employerPrefs[i][j] += 1

        #print(employerPrefs[i])

        # Checked if ranked by type
        #for j in range(len(mySample)):
            #print(candidatePool[employerPrefs[i][j]])

    # Correct id's (First id should be 1, not 0. 0 is used to mark no candidate/end of preferences.)
    # No need to do separately, since all candidates have the same number of preferences.
    candidatePrefs += 1


    # ---------- Output ----------
    np.savetxt('dense_candidate_prefs.csv', candidatePrefs, fmt='%d', delimiter=",")
    np.savetxt('dense_employer_prefs.csv', employerPrefs, fmt='%d', delimiter=",")


def main():
    createDatasets(50, 100)

main()
