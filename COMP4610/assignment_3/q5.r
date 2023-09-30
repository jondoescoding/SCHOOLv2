# Load necessary libraries
library(ggplot2)

# Define the function
f <- function(x) {
  ifelse(x <= 1, 0,
         ifelse(x <= 3, (x-1)^2/12,
                ifelse(x < 7, 14*x/24 - x^2/24 - 25/24,
                       1)))
}

# Plot the function
x_values <- seq(0, 8, by = 0.01)
y_values <- f(x_values)
df <- data.frame(x = x_values, y = y_values)
ggplot(df, aes(x = x, y = y)) +
  geom_line() +
  labs(x = "X", y = "f(X)", title = "Probability Density Function")

# Calculate P(2.8 <= X <= 5.2)
p_value <- integrate(f, lower = 2.8, upper = 5.2)$value

# Print the result
print(paste("P(2.8 <= X <= 5.2) = ", p_value))
