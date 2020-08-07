"""Functionalities for plotting chaotic processess

SlidingFigure: An object to plot the "logistic map" curve and
    processes, with interactive control of the "r" parameters of the
    "logistic map"

"""
import matplotlib.pyplot as plt
import matplotlib.widgets
from scipy import fftpack

from . import logisticmap


class LogisticMapFigure:
    """A plotting object

    Attributes
    ----------
    xxx

    Methods
    -------
    update(val)
        given new values, the method updates and redraws
    """

    def __init__(self, logistic_map: logisticmap.LogisticMap):
        """
        Parameters
        ----------
        logistic_map: logisticmap.LogisticMap,
            a logistic map object
        """

        assert isinstance(logistic_map, logisticmap.LogisticMap)
        self._lm = logistic_map

        self._fig = plt.figure(figsize=(18, 8))
        self._axes = [
            plt.subplot2grid((9, 4), (0, 0), rowspan=8, colspan=1),  # logistic_map
            plt.subplot2grid((9, 4), (8, 0), rowspan=1, colspan=4),  # slider
            plt.subplot2grid((9, 4), (0, 1), rowspan=4, colspan=3),  # chaotic processes
            plt.subplot2grid(
                (9, 4), (4, 1), rowspan=4, colspan=3
            ),  # frequency spectrum
        ]
        self._plot_logistic_map(self._axes[0])
        self._plot_cobweb(self._axes[0])
        self._plot_chaotic_processes(self._axes[2])
        self._plot_frequency_spectrum(self._axes[3])
        self._r_slider = matplotlib.widgets.Slider(
            self._axes[1], "r", 0.0, 4.0, valinit=self._lm.r, valstep=0.2
        )
        self._r_slider.on_changed(self.update)

        self._fig.tight_layout()
        # plt.show()
        self._fig.show()

    def _plot_logistic_map(self, axis):
        self._curve_plot = axis.plot(
            self._lm.XY[:, 0], self._lm.XY[:, 1], label="logistic map"
        )[0]
        axis.plot([0, 1], [0, 1], "k", label="linear")
        axis.set_title("logistic map vs. linear")
        axis.set_xlabel("x[t-1]")
        axis.set_ylabel("x[t]")
        axis.axis("equal")
        axis.legend(loc="upper left", fancybox=True, shadow=False, framealpha=0.6)

    def _plot_cobweb(self, axis):
        self._cobweb_plot = axis.plot(
            self._lm.cobweb[:, 0], self._lm.cobweb[:, 1], "r", alpha=0.7, label="cobweb"
        )[0]

    def _plot_chaotic_processes(self, axis):
        self._processes_plot = axis.plot(self._lm.X, "k", linewidth=0.3, alpha=0.6)
        title = "{:d} chaotic processes (with random initial points) generated from the logistic map"
        axis.set_title(title.format(self._lm.X.shape[1]))
        axis.set_ylim([0, 1])
        axis.set_xlabel("t")
        axis.set_ylabel("x[t]")

    def _plot_frequency_spectrum(self, axis):
        X = fftpack.fft(self._lm.X[:, 0])
        self._spectrum_plot = axis.plot(X, "k", linewidth=0.3, alpha=0.6)[0]
        axis.set_title("frequency spectrum")
        axis.set_ylim([X.real.min() - 1, X.real.max() + 1])
        axis.set_xlabel("f")
        axis.set_ylabel("spectrum")

    def update(self, val):
        """
        Parameters
        ----------
        val: numpy.float64,
            passed to this function by the "slider.on_changed"
        """

        self._lm.r = self._r_slider.val

        self._curve_plot.set_ydata(self._lm.XY[:, 1])

        self._cobweb_plot.set_data(self._lm.cobweb[:, 0], self._lm.cobweb[:, 1])

        for i, p in enumerate(self._processes_plot):
            p.set_ydata(self._lm.X[:, i])

        X = fftpack.fft(self._lm.X[:, 0])
        self._spectrum_plot.set_ydata(X)
        self._spectrum_plot.axes.set_ylim([X.real.min() - 1, X.real.max() + 1])

        self._fig.canvas.draw_idle()

        # # for saving plots and creating animated gifs
        # plt.savefig('{:.5f}'.format(self._lm.r).replace('.', '') + '.png',
        #             facecolor='w', edgecolor='w',
        #             format='png', transparent=False,
        #             bbox_inches='tight', pad_inches=0.0)
