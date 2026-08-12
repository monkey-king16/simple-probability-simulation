import functools

def solve_n_urns(N, B, R):
    """
    Finds the optimal ball distribution for N urns to maximize win probability.
    N: Total urns
    B: Total blue balls
    R: Total red balls
    """
    
    # We use lru_cache to memorize overlapping subproblems
    @functools.lru_cache(None)
    def dp(urns_left, blue_left, red_left):
        # Base Case: Only 1 urn left. Everything remaining must go here.
        if urns_left == 1:
            if blue_left + red_left < 1:
                return -float('inf'), [] # Invalid: urn cannot be empty
            
            prob = blue_left / (blue_left + red_left)
            return prob, [(blue_left, red_left)]
        
        max_p = -float('inf')
        best_path = []
        
        # Test every valid combination of blue and red for the current urn
        for b in range(blue_left + 1):
            for r in range(red_left + 1):
                # Constraint 1: Current urn must have at least 1 ball
                if b + r < 1: 
                    continue
                
                # Constraint 2: Must leave enough balls so future urns aren't empty
                if (blue_left - b) + (red_left - r) < urns_left - 1:
                    continue
                    
                current_p = b / (b + r)
                
                # Recurse for the remaining urns
                future_p, future_path = dp(urns_left - 1, blue_left - b, red_left - r)
                
                total_p = current_p + future_p
                
                # Update maximum and the path of the distribution
                if total_p > max_p:
                    max_p = total_p
                    best_path = [(b, r)] + future_path
                    
        return max_p, best_path

    # Execute the algorithm
    # The DP function returns the sum of probabilities across all urns
    total_sum_prob, distribution = dp(N, B, R)
    
    # Divide by N to get the expected value (since P(choose urn) = 1/N)
    if total_sum_prob == -float('inf'):
        return 0.0, []
        
    final_prob = total_sum_prob / N
    return final_prob, distribution

if __name__ == "__main__":
    # Test Parameters
    urns = 10
    blue_balls = 50
    red_balls = 50
    
    # Run Solver
    max_prob, optimal_dist = solve_n_urns(urns, blue_balls, red_balls)
    
    # Output Results
    print(f"--- Optimizing for {urns} Urns ---")
    print(f"Total Balls: {blue_balls} Blue, {red_balls} Red")
    print(f"\nMaximum Win Probability: {max_prob:.4f} (or {max_prob*100:.1f}%)")
    print("Optimal Distribution:")
    
    for i, (b, r) in enumerate(optimal_dist):
        print(f"  Urn {i+1}: {b} Blue, {r} Red (Win rate: {b/(b+r)*100:.1f}%)")