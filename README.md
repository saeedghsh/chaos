# Chaotic Systems

Python implementation and exprementation with few simplistic chaotic systems.
<!-- Also intended as an scaffold for starting python projects. -->

* Logistic Map: <img src="https://render.githubusercontent.com/render/math?math=x_{t %2B 1}=rx_{t}(x_{t} %2B 1)">  
  <p align="center">
      <img src="https://github.com/saeedghsh/ChaoticSystems/blob/master/animation.gif" width="900">
  </p>

## Usage
```bash
pip install -r requirements.txt
python main.py logisticmap --length 100 --count 500
```
for help:
```bash
python main.py -h
python main.py logisticmap -h
```

## Pyreverse : UML Diagrams for Python
```bash
$ pip install pylint # pyreverse is now part of pylint
$ cd ~/code/ChaoticSystems
$ pyreverse -o svg -p chaos chaos/*.py
$ pyreverse -o svg -p chaoticSystems main.py
$ pyreverse -o svg -p testt ests/*.py
# -a N, -A    depth of research for ancestors
# -s N, -S    depth of research for associated classes
# -A, -S      all ancestors, resp. all associated
# -m[yn]      add or remove the module name
# -f MOD      filter the attributes : PUB_ONLY/SPECIAL/OTHER/ALL
# -k          show only the classes (no attributes and methods)
# -b          show 'builtin' objects
```

## laundry list

* [x] separate parsers for different type of systems (with subparser)

* [x] gererate chaotic processes via logistic maps
  - [ ] reproduce all the plots from [here](https://en.wikipedia.org/wiki/Logistic_map)
    + [x] frequency spectrum
    + [x] [cobweb plot](https://en.wikipedia.org/wiki/Cobweb_plot)
    + [ ] [Bifurcation diagram](https://en.wikipedia.org/wiki/Bifurcation_diagram)
    + [ ] "lyapunov exponent" v.s. `r`: In mathematics the Lyapunov
      exponent or Lyapunov characteristic exponent of a dynamical
      system is a quantity that characterizes the rate of separation
      of infinitesimally close trajectories.
   + [ ] Two- and three-dimensional [Poincaré plots](https://en.wikipedia.org/wiki/Poincar%C3%A9_plot)
  - [ ] use [Tent map](https://en.wikipedia.org/wiki/Tent_map) instead of "Logistic map"
  - [ ] use the "[hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_functions) map" instead of "Logistic map".

* [ ] the 2D plot from the derivative of the process: <img src="https://render.githubusercontent.com/render/math?math=(x,y)=(dX_{t}, dX_{t %2B 1})">

* [ ] List other chaotic systems
  - [ ] [Arnold tongue](https://en.wikipedia.org/wiki/Arnold_tongue)
  - [ ] double-rod pendulum
  - [ ] Lorenz attractor 
  - [ ] Mobility VS time of blue/red cars from [here](https://en.wikipedia.org/wiki/Chaos_theory)
  - [ ] [Three-body problem](https://en.wikipedia.org/wiki/Three-body_problem)

* [ ] [dynamic mode decomposition](https://en.wikipedia.org/wiki/Dynamic_mode_decomposition)

* [ ] ? predicting chaos ("Although, 3-body is rather a simpler chaotic system" -Adam) "[Newton vs the machine: solving the chaotic three-body problem using deep neural networks](https://arxiv.org/abs/1910.07291)"
* [ ] ? stochastic chaos

## References
https://en.wikipedia.org/wiki/Arnold_tongue#Standard_circle_map


## License
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/ChaoticSystems/blob/master/LICENSE).
```
Copyright (C) Saeed Gholami Shahbandi
```
