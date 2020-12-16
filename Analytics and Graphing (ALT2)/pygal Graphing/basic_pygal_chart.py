# install pygal and lxml packages before running this code
import pygal

#assign it an easier variable name
disChart = pygal.XY(stroke=False)


#chart title
disChart.title = 'Correlation'

#disChart.add('Series Name', [lists of data points])
disChart.add('A', [(0, 0), (.1, .2), (.3, .1), (.5, 1), (.8, .6), (1, 1.08), (1.3, 1.1), (2, 3.23), (2.43, 2)])
disChart.add('B', [(.1, .15), (.12, .23), (.4, .3), (.6, .4), (.21, .21), (.5, .3), (.6, .8), (.7, .8)])
disChart.add('C', [(.05, .01), (.13, .02), (1.5, 1.7), (1.52, 1.6), (1.8, 1.63), (1.5, 1.82), (1.7, 1.23), (2.1, 2.23), (2.3, 1.98)])

#save top a vector graphics file
disChart.render_to_file('chart.svg')

#show in your browser
disChart.render_in_browser()
