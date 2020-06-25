import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets

from . import logisticmap

class SlidingFigure:
    ''''''
    def __init__(self, logistic_map: logisticmap.LogisticMap):
        ''''''
        assert isinstance(logistic_map, logisticmap.LogisticMap) 
        self._lm = logistic_map
        
        self._fig = plt.figure(figsize=(18, 6))
        self._axes = [
            plt.subplot2grid((9, 4), (0, 0), rowspan=8, colspan=1), # logistic_map
            plt.subplot2grid((9, 4), (8, 0), rowspan=1, colspan=4), # slider
            plt.subplot2grid((9, 4), (0, 1), rowspan=8, colspan=3), # chaotic processes
        ]
        self.plot_logistic_map(self._axes[0])
        self.plot_chaotic_processes(self._axes[2])
        self._r_slider = matplotlib.widgets.Slider(
            self._axes[1], 'r',
            0.0, 4.0, valinit=self._lm.r, valstep=0.2)
        self._r_slider.on_changed(self.update)
        
        self._fig.tight_layout()
        plt.show()

    def plot_logistic_map(self, axis):
        ''''''
        self._lm_curve_plot = axis.plot( self._lm.XY[:,0], self._lm.XY[:,1],
                                         label='logistic map')[0]
        axis.plot([0, 1], [0, 1], 'k', label='linear')
        axis.set_title('logistic map vs. linear')
        axis.set_xlabel('x[t-1]')
        axis.set_ylabel('x[t]')
        axis.axis('equal')
        axis.legend(loc='upper left', fancybox=True, shadow=False, framealpha=0.6)
        
    def plot_chaotic_processes(self, axis):
        ''''''
        self._lm_processes_plot = axis.plot(self._lm.X, 'k', linewidth=0.3, alpha=0.6)
        title = '{:d} chaotic processes (with random initial points) generated from the logistic map'
        axis.set_title(title.format(self._lm.X.shape[1]))
        axis.set_xlabel('t')
        axis.set_ylabel('x[t]')
    
    def update(self, val):
        ''''''
        self._lm.r = self._r_slider.val
        self._lm_curve_plot.set_ydata(self._lm.XY[:,1])
        for i,p in enumerate(self._lm_processes_plot):
            p.set_ydata(self._lm.X[:,i])
        self._fig.canvas.draw_idle()
        # plt.savefig('{:.5f}'.format(self._lm.r).replace('.','') + '.png',
        #             facecolor='w', edgecolor='w',
        #             format='png', transparent=False,
        #             bbox_inches='tight', pad_inches=0.0)