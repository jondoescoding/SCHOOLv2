# Define the total number of cards and the number of clubs
total_cards <- 52
clubs <- 13

# After one card is removed, the total number of cards and clubs are reduced by 1
total_cards <- total_cards - 1
clubs <- clubs - 1

# Calculate the probability of drawing two clubs from the remaining cards
# This is a combination problem, so we use the choose() function in R
prob <- choose(clubs, 2) / choose(total_cards, 2)

# Print the result
print(prob)