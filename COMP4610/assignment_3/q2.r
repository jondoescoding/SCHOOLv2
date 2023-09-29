# Define the probabilities
P_D <- 1/1000  # Probability that an item is defective
P_T_given_notD <- 2/100  # Probability that the test is positive given the item is not defective
P_notT_given_D <- 1/100  # Probability that the test is negative given the item is defective

# Calculate the complementary probabilities
P_notD <- 1 - P_D  # Probability that an item is not defective
P_T_given_D <- 1 - P_notT_given_D  # Probability that the test is positive given the item is defective

# Calculate the total probability of a positive test result
P_T <- P_T_given_D * P_D + P_T_given_notD * P_notD

# Apply Bayes' theorem to find the probability that an item is defective given a positive test result
P_D_given_T <- (P_T_given_D * P_D) / P_T

# Print the result
print(P_D_given_T)