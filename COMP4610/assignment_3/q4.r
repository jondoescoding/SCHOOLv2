# Define the function
f <- function(x, k) {
  ifelse(x >= 0 & x <= 1, k*(1-x)^4, 0)
}

# Define the integral of the function minus 1 (since total probability should be 1)
g <- function(k) {
  integrate(f, lower = 0, upper = 1, k = k)$value - 1
}

# Use uniroot to find the value of k that makes g(k) = 0
solution <- uniroot(g, interval = c(0, 100))

# Print the solution
print(solution$root)

# Load necessary libraries
library(ggplot2)

# Define the function
f <- function(x, k) {
  ifelse(x >= 0 & x <= 1, k*(1-x)^4, 0)
}

# Use the value of k found in part a
k <- solution$root

# b. Sketch the probability density function
x_values <- seq(0, 1, by = 0.01)
y_values <- f(x_values, k)
df <- data.frame(x = x_values, y = y_values)
ggplot(df, aes(x = x, y = y)) +
  geom_line() +
  labs(x = "X", y = "f(X)", title = "Probability Density Function")

# c. Determine the mean of X
# The mean of a continuous random variable X with pdf f(x) is given by E[X] = integral(x*f(x) dx)
mean_x <- integrate(function(x) x*f(x, k), lower = 0, upper = 1)$value

# d. Determine the variance of X to 3 decimal places
# The variance of a continuous random variable X with pdf f(x) is given by Var[X] = E[X^2] - (E[X])^2
ex2 <- integrate(function(x) (x^2)*f(x, k), lower = 0, upper = 1)$value
var_x <- ex2 - mean_x^2

# e. Find the quantity of flour that the factory should have in stock at the beginning of a week
# such that there is a probability of 0.98 that the demand in that week will be met.
# This is equivalent to finding the 98th percentile of the distribution.
quantile_x <- uniroot(function(x) integrate(f, lower = 0, upper = x, k = k)$value - 0.98,
                     interval = c(0, 1))$root

# Print the results
print(paste("Mean of X: ", mean_x))
print(paste("Variance of X: ", round(var_x, 3)))
print(paste("Quantity of flour to stock: ", round(quantile_x)))