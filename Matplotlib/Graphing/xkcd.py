
#
# Python Version of XKCD cominc 2048
# by Douglas Weadon Higinbotham
#

import matplotlib.pyplot as plt
import numpy as np

from lmfit import Model, Parameters

# The Data

xx = np.array([ 27.5,  53.2,  56.8,  64.2,  72.1,  77.6,  83.3,  91.2, 116. ,
       121.9, 132.1, 134.1, 141.5, 143.1, 162.1, 186.8, 196.7, 211.2,
       227. , 227.1, 227.6, 231.2, 245.7, 256.2, 262. , 267. , 267.9,
       271.3, 273.5, 279.8, 284.3])

yy = np.array([ 44.8, 117.4,  62.7, 181.5,  52.1,  82.4,  73.1,  84.4, 102.2,
       143.3,  81.1,  62.3,  72.6,  58.1,  45.1,  49.7, 102.9, 142.5,
       151.5, 258.4, 120.9, 138.5, 221.2, 184.4,  20.9, 164.6, 120.3,
       190.2, 203. , 220.3, 184.2])

# The Definitions

def llog(x,e0,e1,e2):
    return e1*np.log(x)+e0

def expp(x,e1,e0):
    return e0*np.exp(x*e1)

def const(x,e0):
    return e0

def linear(x,e0,e1):
    return x*e1+e0

def quad(x,e0,e1,e2):
    return e2*x**2+e1*x+e0

def sigmoid(x, x0, k,a):
    y = a+ a / (1 + np.exp(-k*(x-x0)))
    return y


def epoly(q2,**params): # this calculates 1+param[0]*q^2+param[1]*q^4...
    value=params['e0']+params['e1']*q2+params['e2']*q2**2+params['e3']*q2**3+params['e4']*q2**4+params['e5']*q2**5+params['e6']*q2**6+params['e7']*q2**7+params['e8']*q2**8+params['e9']*q2**9+params['e10']*q2**10
    return value

# Polynomial Fit Parameters

parame=Parameters()
parame.add('e0',value=0,vary=1)
parame.add('e1',value=0,vary=1)
parame.add('e2',value=0,vary=1)
parame.add('e3',value=0,vary=1)
parame.add('e4',value=0,vary=1)
parame.add('e5',value=0,vary=1)
parame.add('e6',value=0,vary=1)
parame.add('e7',value=0,vary=1)
parame.add('e8',value=0,vary=1)
parame.add('e9',value=0,vary=1)
parame.add('e10',value=0,vary=1)

# The Fits Using LMFIT

model=Model(linear)
lresult=model.fit(yy,x=xx,e0=1,e1=-1)

model=Model(linear)
l1result=model.fit(yy[0:15],x=xx[0:15],e0=1,e1=-1)

model=Model(linear)
l2result=model.fit(yy[15:],x=xx[15:],e0=1,e1=-1)

model=Model(quad)
qresult=model.fit(yy,x=xx,e0=1,e1=-1,e2=0)

model=Model(const)
cresult=model.fit(yy,x=xx,e0=1)

model=Model(epoly)
eresult=model.fit(yy,q2=xx,params=parame)

model=Model(llog)
logresult=model.fit(yy,x=xx,e0=1,e1=1)

model=Model(expp)
exppresult=model.fit(yy,x=xx,e1=0.1,e0=1)

model=Model(sigmoid)
istresult=model.fit(yy,x=xx,x0=180,k=10,a=2)


# The Twelve Plots

myx=np.linspace(20,295,3000)
plt.figure(dpi=75,figsize=(14,10))
plt.xkcd()


plt.subplot(3,4,1)
plt.xkcd()
plt.suptitle('CURVE-FITTING METHODS AND THE MESSAGES THEY SEND')
plt.xkcd()
plt.plot(xx,yy,'o',color='black')
plt.plot(myx,linear(myx,**lresult.best_values),color='red')
plt.annotate('Linear',xy=(20,240),color='grey')
plt.xlabel('"HEY!  I DID A \n REGRESSION."')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,2)
plt.plot(xx,yy,'o',color='black')
plt.plot(myx,quad(myx,**qresult.best_values),color='red')
plt.annotate('Quadratic',xy=(20,240),color='grey')
plt.xlabel('"I WANTED A CURVED \n LINE, SO A MADE ONE \n WITH MATH."')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,3)
plt.plot(xx,yy,'o',color='black')
plt.plot(myx,llog(myx,**logresult.best_values),color='red')
plt.annotate('LOGARITHMIC',xy=(20,240),color='grey')
plt.xlabel('"LOOK, IT\'S \n TAPPERING OFF"')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,4)
plt.plot(xx,yy,'o',color='black')
plt.plot(myx,expp(myx,**exppresult.best_values),color='red')
plt.annotate('EXPONENTIAL',xy=(20,240),color='grey')
plt.xlabel('"LOOK, IT\'S GROWING \n UNCONTROLLABLY"')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])

# Using Statsmodel For Local Regression

import statsmodels.api as sm
lowess = sm.nonparametric.lowess
nnn=lowess(yy,xx,frac=0.4)

plt.xkcd()
plt.subplot(3,4,5)
plt.plot(nnn[:,0],nnn[:,1],'-',color='red')
plt.plot(xx,yy,'o',color='black')
plt.annotate('LOESS',xy=(20,240),color='grey')
plt.xlabel('"I\'M SOPHISTICATED, NOT \n LIKE THOSE BUMBLING \n POLYNOMIAL PEOPLE."')
plt.annotate('by Douglas Higinbotham in Python inspired by https://xkcd.com/2048',xy=(20,-520),rotation=0,annotation_clip=False,fontsize=10)

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,6)
plt.plot(xx,yy,'o',color='black')
plt.plot([np.min(myx),np.max(myx)],[cresult.best_values['e0'],cresult.best_values['e0']],color='red',label='Linear Regression')
plt.annotate('Linear',xy=(20,240),color='grey')
plt.annotate('No Slope',xy=(20,210),color='grey')
plt.xlabel('"I\'M MAKING A \n SCATTER PLOT BUT \n I DON\'T WANT TO"')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,7)
plt.plot(xx,yy,'o',color='black')
plt.plot(xx,sigmoid(xx,**istresult.best_values),color='red')
plt.annotate('SIGMOID',xy=(20,235),color='grey')
plt.xlabel('"I NEEDED TO CONNECT \n THESE TWO LINES."')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,8)
a=lresult.eval_uncertainty(x=xx,sigma=3)
plt.fill_between(xx,qresult.best_fit-a,qresult.best_fit+a,color='pink')
plt.plot(xx,qresult.best_fit-a,'-',color='red')
plt.plot(xx,qresult.best_fit+a,color='red')
plt.plot(xx,yy,'o',color='black')
plt.annotate('95% Confidence',xy=(20,240),color='grey')
plt.annotate('Interval',xy=(20,210),color='grey')
plt.xlabel('"LISTEN, SCIENCE IS HARD \n BUT I\'M A SERIOUS PERSON \n DOING MY BEST."')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,9)
plt.plot(xx,yy,'o',color='black')
plt.plot(xx[0:15],linear(xx[0:15],**l1result.best_values),color='red')
plt.plot(xx[15:],linear(xx[15:],**l2result.best_values),color='red')
plt.annotate('PIECEWISE',xy=(20,235),color='grey')
plt.xlabel('"NOW I JUST NEED TO \n RENORMALIZE THE DATA."')
aa=l1result.eval_uncertainty(x=xx[0:15],sigma=1)
bb=l2result.eval_uncertainty(x=xx[15:],sigma=1)
plt.plot(xx[0:15],linear(xx[0:15],**l1result.best_values)+aa,color='red',lw=1)
plt.plot(xx[0:15],linear(xx[0:15],**l1result.best_values)-aa,color='red',lw=1)
plt.plot(xx[15:],linear(xx[15:],**l2result.best_values)+bb,color='red',lw=1)
plt.plot(xx[15:],linear(xx[15:],**l2result.best_values)-bb,color='red',lw=1)

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])




plt.xkcd()
plt.subplot(3,4,10)
plt.plot(xx,yy,color='red')
plt.plot(xx,yy,'o',color='black')
plt.annotate('CONNECT',xy=(20,240),color='grey')
plt.annotate('THE DOTS',xy=(20,210),color='grey')
plt.xlabel('"REGRESSION?!  JUST USE \n THE DEFAULT PLOTTING."')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,11)
import matplotlib.image as mpimg
img=mpimg.imread('Figures/elephant.png')
plt.imshow(img,extent=(10,330,20,270))
plt.annotate('Elephant',xy=(20,240),color='grey')
plt.xlabel('"AND WITH FIVE \n PARAMETERS I CAN MAKE \n ITS TRUNK WIGGLE."')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])


plt.xkcd()
plt.subplot(3,4,12)
#plt.xkcd()
plt.plot(xx,yy,'o',color='black')
plt.plot(myx,epoly(myx,**eresult.best_values),color='red')
plt.annotate('House of Cards',xy=(20,235),color='grey')
plt.xlabel('"AS YOU CAN SEE, THIS \n MODEL SMOOTHLY FITS \n THE --- NO NO WAIT DON\'T \n EXTEND IT AAAAA!"')

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticks([])
frame1.axes.xaxis.set_ticks([])

plt.tight_layout(rect=[0, 0.01, 1, 0.975])
plt.savefig('Figures/Python-XKCD-2048.png')
plt.savefig('Figures/Python-XKCD-2048.pdf')

plt.show()