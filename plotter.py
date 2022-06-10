import matplotlib.pyplot as plt
def plotter(y,x): ###
    fig = plt.figure(1)
    yline = plt.plot(y,x)
    #syncline = plt.plot(sync)
    plt.grid()
    plt.show()
    #ax = fig.add_subplot(111)
    #ax.patch.set_facecolor('#ababab')
    #ax.patch.set_alpha(0.5)
    #fig.patch.set_facecolor('#E0E0E0')