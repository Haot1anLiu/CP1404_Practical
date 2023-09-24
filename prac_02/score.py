import random

def determine_result(score):
    """Determine the result based on the score."""
    if 0 <= score <= 100:
        if score >= 90:
            return "excellent"
        elif score >= 50:
            return "pass"
        else:
            return "bad"
    else:
        return "Invalid"

def main():
    score = float(input("Please enter the score:"))
    result = determine_result(score)
    print(result)

    random_score = random.uniform(0, 100)
    print(f"Random Score: {random_score:.2f}")
    print(determine_result(random_score))

if __name__ == "__main__":
        main()


