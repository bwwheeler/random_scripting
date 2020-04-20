'''generate a random critic score for a film (out of 10)'''

import random

def main():
    with open('critic_scores.txt','w') as critic_scores:
        for x in range(50):
            score = (str(random.randint(3, 9)) + "." + str(random.randint(0, 9)))
            critic_scores.write(score + '\n')
            
if __name__ == "__main__":
	main()