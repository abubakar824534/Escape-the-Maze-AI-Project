# \# 🧩 Escape the Maze — AI Search Algorithms

# 

# \## 📌 Project Overview

# 

# \*\*Escape the Maze\*\* is an Artificial Intelligence mini-project inspired by \*The Maze Runner\*.

# 

# The objective is to implement classical AI search algorithms to navigate a maze, avoid walls, handle different terrain costs, and find a path from the starting position to the exit.

# 

# The project also includes a key-collection challenge where the agent must collect all escape-code pieces before reaching the final exit.

# 

# \## 🧠 Search Algorithms Implemented

# 

# | Algorithm | Description |

# |---|---|

# | Depth-First Search (DFS) | Explores deeply before backtracking |

# | Breadth-First Search (BFS) | Finds a path with the fewest steps |

# | Depth-Limited Search (DLS) | Performs DFS with a maximum depth limit |

# | Iterative Deepening Search (IDS) | Repeatedly increases the DLS depth limit |

# | Uniform-Cost Search (UCS) | Finds the path with the lowest total cost |

# | Greedy Best-First Search | Uses a heuristic to guide exploration |

# | A\* Search | Combines actual path cost and heuristic estimation |

# 

# \## 📁 Project Structure

# 

# ```text

# maze\_runner/

# ├── search.py

# ├── heuristics.py

# ├── griever\_hole.py

# ├── problems.py

# ├── util.py

# ├── maze.py

# ├── runner.py

# ├── display.py

# └── mazes/

# ```

# 

# \### Important Files

# 

# \- \*\*search.py\*\* — Implements DFS, BFS, DLS, IDS, UCS, Greedy, and A\*.

# \- \*\*heuristics.py\*\* — Contains Manhattan and Euclidean distance heuristics.

# \- \*\*griever\_hole.py\*\* — Defines the key-collection search problem and its heuristic.

# \- \*\*problems.py\*\* — Defines the search problem interfaces.

# \- \*\*util.py\*\* — Contains Stack, Queue, and PriorityQueue data structures.

# \- \*\*runner.py\*\* — Runs the algorithms and displays their results.

# \- \*\*mazes/\*\* — Contains the maze layouts used for testing.

# 

# \## ⚙️ Requirements

# 

# \- Python 3

# \- Tkinter (optional, for graphical visualization)

# 

# The core project uses Python's standard library.

# 

# \## 🚀 How to Run

# 

# \### 1. Clone the Repository

# 

# ```bash

# git clone <repository-url>

# cd <repository-folder>

# ```

# 

# Replace `<repository-url>` with your GitHub repository URL.

# 

# \### 2. Run Search Algorithms

# 

# \*\*Depth-First Search\*\*

# 

# ```bash

# python runner.py -l maze\_small -a dfs

# ```

# 

# \*\*Breadth-First Search\*\*

# 

# ```bash

# python runner.py -l maze\_medium -a bfs

# ```

# 

# \*\*Depth-Limited Search\*\*

# 

# ```bash

# python runner.py -l maze\_small -a dls -d 60

# ```

# 

# \*\*Iterative Deepening Search\*\*

# 

# ```bash

# python runner.py -l maze\_small -a ids

# ```

# 

# \*\*Uniform-Cost Search\*\*

# 

# ```bash

# python runner.py -l griever\_alley -a ucs

# ```

# 

# \*\*Greedy Best-First Search\*\*

# 

# ```bash

# python runner.py -l greedy\_trap -a gbfs -H manhattan

# ```

# 

# \*\*A\* Search\*\*

# 

# ```bash

# python runner.py -l maze\_big -a astar -H manhattan

# ```

# 

# \*\*Key Collection Problem\*\*

# 

# ```bash

# python runner.py -l keys\_small -p keys -a bfs

# ```

# 

# \*\*A\* with Key Hunt Heuristic\*\*

# 

# ```bash

# python runner.py -l keys\_medium -p keys -a astar -H keyhunt

# ```

# 

# \### Additional Commands

# 

# ```bash

# python runner.py --list

# python runner.py -l maze\_medium --compare

# python runner.py -l maze\_medium -a bfs -t

# python runner.py -l maze\_medium -a bfs -q

# ```

# 

# \- `--list` displays available mazes.

# \- `--compare` compares search algorithms.

# \- `-t` uses text-mode visualization.

# \- `-q` displays numerical results without graphical visualization.

# 

# \## 🗺️ Maze Symbols

# 

# | Symbol | Description | Movement Cost |

# |---|---|---|

# | `%` | Wall | Impassable |

# | Space | Normal corridor | 1 |

# | `S` | Starting position | 1 |

# | `E` | Exit | 1 |

# | `\~` | Thick ivy | 3 |

# | `G` | Griever territory | 10 |

# | `K` | Escape-code piece | 1 |

# 

# \## 📊 Sample Results

# 

# The following are reference results from the project specification.

# 

# | Algorithm | Maze | Path Cost | Steps |

# |---|---|---:|---:|

# | DFS | maze\_small | 50 | 50 |

# | BFS | maze\_medium | 66 | 66 |

# | DLS (limit 60) | maze\_small | 50 | 50 |

# | IDS | maze\_small | 50 | 50 |

# | UCS | griever\_alley | 42 | 28 |

# | Greedy | greedy\_trap | 52 | 25 |

# | A\* | greedy\_trap | 25 | 25 |

# | A\* | maze\_big | 124 | 124 |

# | BFS (Key Hunt) | keys\_small | 54 | 54 |

# 

# Actual results may vary for non-optimal algorithms depending on successor ordering.

# 

# \## 🔍 Key AI Concepts

# 

# \*\*Graph Search:\*\* Uses an explored-state set to avoid repeated expansions.

# 

# \*\*Heuristics:\*\* Estimate the remaining distance to a goal to guide search.

# 

# \*\*Optimality:\*\* BFS minimizes the number of steps, while UCS and A\* with suitable heuristics minimize total movement cost.

# 

# \*\*State Representation:\*\* The key-collection problem tracks both the agent's current position and the collected escape-code pieces.

# 

# \*\*Priority Queue:\*\* UCS, Greedy, and A\* use priority queues to select the next state to explore.

# 

# \## 🎯 Learning Outcomes

# 

# This project provides practical experience with:

# 

# \- Classical AI search techniques

# \- Stack, Queue, and PriorityQueue data structures

# \- Graph traversal and state-space exploration

# \- Heuristic design

# \- Pathfinding with weighted terrain

# \- Problem formulation and key-collection search

# \- Comparing algorithm efficiency and solution quality

# 

# \## 📚 Academic Context

# 

# Developed as part of \*\*Artificial Intelligence — Mini Project 01: Escape the Maze\*\*.

# 

# The project is intended for educational purposes and demonstrates fundamental concepts in classical AI search.

