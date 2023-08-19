from matplotlib import pyplot as plt
ingr=['flour','sugar','egg','cream','milk']
quantity=[350,170,250,100,275]
rang=['y','r','b','g','c']

plt.pie(quantity,labels=ingr,colors=rang,
        startangle=0,shadow=False,explode=(0,0,0,0,0),autopct='%.2f')
plt.title('Cake Ingredients')
plt.show()