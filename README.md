# simple-probability-simulation
## The Problem
You have two urns, five red balls, and five blue balls. You can distribute the balls into the urns any way you like, but each urn must have at least one ball in it. I will choose one urn at random (p = 0.5) and then draw one ball from it. If the ball is blue, you win. How should you distribute the balls to maximize your probability of winning?


## The Solution
To maximize the expected value, you must push the probability of drawing a blue ball from one urn to 100% without severely penalizing the other urn.
*   **Urn 1:** 1 Blue, 0 Red (100% win rate if chosen)
*   **Urn 2:** 4 Blue, 5 Red (~44.4% win rate if chosen)
*   **Maximum Total Probability:** ~72.2% (13/18)

## Mathematical Visualization
The probability distribution forms a saddle graph (hyperbolic paraboloid). The highest peaks represent the optimal asymmetrical strategies, while the flat center represents an even 50/50 distribution.

![3D Probability Distribution](Figure_1.png)
