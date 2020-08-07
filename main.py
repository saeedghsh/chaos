#!/usr/bin/env python
""" Generation of chaotic processes via logistic map"""

from __future__ import print_function

import argparse

from chaos.logisticmap import LogisticMap
from chaos.plotting import LogisticMapFigure


def main_logisticmap(args: argparse.Namespace):
    """instantiating the LogisticMap and the plotting object

    Parameters
    ----------
    args.length : int
        The length of each processes
    args.count : int
        The numebr of processes
    """

    LM = LogisticMap(r=0.0, length=args.length, count=args.count)
    _ = LogisticMapFigure(LM)


import matplotlib.pyplot as plt
import numpy as np
import time

def main_draw_bifurcation():
    """"""
    bifurcation_fig = plt.figure(10)

    count, length, r_resolution = 200, 60, 2000
    LMs = [LogisticMap(r=_r, length=length, count=count)
           for _r in np.linspace(0, 4, r_resolution)]
    R = np.array([lm.r for lm in LMs])
    B = np.array([lm.X[-1,:] for lm in LMs])        
    
    plt.plot(
        np.repeat(R, count),
        B.reshape(-1),
        'k,')
    bifurcation_fig.show()
    
    

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description="number and temopral length of processes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    SUBPARSERS = PARSER.add_subparsers()

    LOGISTICMAP_PARSER = SUBPARSERS.add_parser("logisticmap")
    LOGISTICMAP_PARSER.set_defaults(func=main_logisticmap)
    LOGISTICMAP_PARSER.add_argument(
        "--count",
        dest="count",
        type=int,  # nargs=1,
        action="store",
        default=100,
        help="number of the chaotic processes",
    )
    LOGISTICMAP_PARSER.add_argument(
        "--length",
        dest="length",
        type=int,  # nargs=1,
        action="store",
        default=60,
        help="[temporal] length of the chaotic processes",
    )
    LOGISTICMAP_PARSER.add_argument(
        "--draw-bifurcation",
        dest="draw_bifurcation",
        action="store_true",
        default=False,
        help="If specificed, will draw bifurcation diagram",
    )


    ARGS = PARSER.parse_args()
    ARGS.func(ARGS)
    
    if ARGS.draw_bifurcation:
        main_draw_bifurcation()

    # I am calling this to keep the plots open
    plt.show()
