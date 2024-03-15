import numpy as np
import matplotlib.pyplot as plt

def simulate_dk_effect(text):
    #split the text into words
    words = text.split()
    num_subjects = len(words)
    
    #generate random task performance data
    np.random.seed(0)
    performance = np.random.normal(50,15, num_subjects)
    
    #simulate self-assessment data
    self_assessment = np.where(performance < 30, np.random.normal(performance + 40, 5), np.where((performance >= 30) & (performance < 70), np.random.normal(performance - 40, 5)))
    return performance, self_assessment

# Get the text input from the user
text = input("Enter a text: ")

# call the simulate_dk_effect function
performance, self_assessment = simulate_dk_effect(text)

# plot the relationship between performance and self-assessment
plt.scatter(performance, self_assessment)
plt.xlabel("Performance")
plt.ylabel("Self-assessment")
plt.title("Dunning-Kruger Effect")
plt.show() 