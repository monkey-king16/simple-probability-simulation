import numpy as np
import matplotlib.pyplot as plt

def plot_3d_probability():
    # Set up the figure and 3D axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Lists to store the valid coordinate points
    x_blue = []
    y_red = []
    z_prob = []
    
    for b1 in range(6):
        for r1 in range(6):
            # Enforce the constraint: neither urn can be empty
            if b1 + r1 == 0 or b1 + r1 == 10:
                continue
                
            # Calculate remaining balls for Urn 2
            b2 = 5 - b1
            r2 = 5 - r1
            
            # Calculate expected win probability
            p1 = b1 / (b1 + r1)
            p2 = b2 / (b2 + r2)
            p_win = 0.5 * p1 + 0.5 * p2
            
            # Append to our axes lists
            x_blue.append(b1)
            y_red.append(r1)
            z_prob.append(p_win)

    # Plot the 3D scatter graph
    # c=z_prob colors the points based on their height (probability)
    # s=100 controls the size of the data points
    scatter = ax.scatter(x_blue, y_red, z_prob, c=z_prob, cmap='viridis', s=100, alpha=0.9)
    
    # Labeling exactly as requested
    ax.set_xlabel('Blue Balls in Urn 1 (X)')
    ax.set_ylabel('Red Balls in Urn 1 (Y)')
    ax.set_zlabel('Probability of Winning (Z)')
    ax.set_title('3D Probability Distribution')
    
    # Force axes to show only whole numbers for ball counts
    ax.set_xticks(range(6))
    ax.set_yticks(range(6))
    
    # Add a color bar for easier reading of the Z values
    plt.colorbar(scatter, ax=ax, pad=0.1, label='Probability', shrink=0.7)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_3d_probability()