from matplotlib import pyplot as plt

village_age=[78,81,22,87,53,12,31,42,10,36,45,95,92,80,81,75,78,89,99,66,61]
age_group=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(village_age,age_group,rwidth=1)
plt.ylabel("No. of person in that age group")
plt.xlabel('Age group')
plt.show()