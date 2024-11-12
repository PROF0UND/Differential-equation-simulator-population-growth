#import libs
import numpy
import matplotlib.pyplot as plotter

#create parameters
y_initial = 10
growth_rate = 0.1
time_end = 50
time_step = 0.5
k = 100

#create lists to store the time and y values
time_list = numpy.arange(0, time_end + 1, time_step)
population = [y_initial]

#fill list with values
for t in time_list[1:]:
    new_pop = population[-1] + (growth_rate * population[-1] * (1 - population[-1] / k)) * time_step
    population.append(new_pop)

#make the graph
plotter.plot(time_list, population, marker = '*', label="Simulated y(t)")
plotter.title("Population Growth ODE")
plotter.show()
