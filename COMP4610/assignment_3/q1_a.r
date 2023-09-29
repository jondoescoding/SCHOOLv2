# Question #1a
simulate_experiments <- function(n, p, num_experiments) {
  # Simulate one experiment
  x <- rbinom(1, size = n, prob = p)
  print(paste("Number of successes in one experiment:", x))

  # Simulate multiple experiments
  x <- rbinom(num_experiments, size = n, prob = p)

  # Define title and label for histogram
  main_title <- "Histogram of simulated experiments"
  x_axis_label <- "Number of successes"

  # Create histogram
  hist(x, main = main_title, xlab = x_axis_label)
}
