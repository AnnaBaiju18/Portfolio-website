import matplotlib.pyplot as plt
Tasks = ['Coding','Debugging','Research','Documentation','Testing']
hours = [ 9,6,3,2,3 ]
colors = [ 'red' , 'orange' , 'blue' , 'green' , 'yellow']
plt.figure(figsize = (6,6))
plt.pie(hours,labels=Tasks,colors=colors,autopct='%1.1f%%')
plt.title('Time Spent on Programming Tasks')
plt.axis('equal')
plt.show()