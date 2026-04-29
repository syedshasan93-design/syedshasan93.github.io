import random

print("=== My Game ===")

score = 0
balls = 6

for ball in range(1, balls + 1):
    print(f"\nBall {ball}")

    user = int(input("Enter runs (0-6): "))
    comp = random.randint(0, 6)

    print(f"Computer chose: {comp}")

    if user == comp:
        print("OUT! 🛑")
        break
    else:
        score += user
        print(f"You scored {user} runs")

print(f"\nFinal Score: {score}")
