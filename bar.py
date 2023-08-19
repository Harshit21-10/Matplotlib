from matplotlib import pyplot as plt
from matplotlib import style

Batsman1 = [41,52,58,37,97,97,55]
Batsman2 = [40,54,66,87,27,95,85]
Matches = [1,3,5,7,9,11,13]
matches = [2,4,6,8,10,12,14]

plt.bar(Matches,Batsman1,label="MS Dhoni")
plt.bar(matches,Batsman2,label="Virat Kohli")

plt.legend()
plt.xlabel("Matches")
plt.ylabel("Run Scored")
plt.title("Comparision of Batsman")

plt.show()