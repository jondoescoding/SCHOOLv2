# Question 1b & c
# Define the parameters
n <- 31  # number of trials
p <- 0.447  # probability of success

# Generate a sequence of possible values for X
x <- 0:n

# Calculate the PMF for each value of X
pmf <- dbinom(x, size = n, prob = p)

# Plot the PMF
plot(x, pmf, type = "h", main = "PMF of X", xlab = "Number of successes", ylab= "Probability")

# Calculate the CDF for each value of X
cdf <- pbinom(x, size = n, prob = p)

# Plot the CDF
plot(x, cdf, type = "s", main = "CDF of X", xlab = "Number of successes", ylab = "Cumulative probability")
