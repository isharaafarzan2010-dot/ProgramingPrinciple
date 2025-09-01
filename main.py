import random
import time
import math
def create_question(min_num, max_num):

    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    operator = random.choice(['+', '-'])
    return f"{num1} {operator} {num2}"
def ask_question(question):
   
    start_time = time.time()
    answer = input(f"What is {question}? ")
    end_time = time.time()
    time_taken = math.floor(end_time - start_time)
    try:
        user_answer = int(answer)
    except ValueError:
 
        return False, time_taken
    correct_answer = eval(question)
    return (user_answer == correct_answer), time_taken
def main():
    print("Welcome to Isharaa's the Maths Test! .")
    
    while True:
        difficulty = input("Choose your difficulty level (Easy/Medium/Hard): ").strip().lower() 
        if difficulty == 'easy':
            questions = 5
            max_num = 10
            break
        elif difficulty == 'medium':
            questions = 10
            max_num = 20
            break
        elif difficulty == 'hard':
            questions = 15
            max_num = 50
            break
        else:
            print("Invalid difficulty level. Please enter Easy, Medium, or Hard.")
    
    print(f"You have selected {difficulty.capitalize()} difficulty level.")
    
    score = 0
    correct_list = []
    time_list = []
    
    for i in range(1, questions + 1):
        print(f"\nQuestion {i} of {questions}")
        print(f"Current score: {score}")
        if i < questions:
            min_num = max_num // 2
            max_range = max_num
        else:
        
            min_num = max_num
            max_range = max_num * 2
            print("Challenge question!")
        
        question = create_question(min_num, max_range)
        correct, time_taken = ask_question(question)
      
        if correct:
         
            points = max(10 - time_taken, 1)
            score += points
        
            print(f"Fantastic! You took {time_taken} second{'s' if time_taken != 1 else ''} and earned {points} point{'s' if points != 1 else ''}.")
        else:
            print(f"Incorrect. You took {time_taken} second{'s' if time_taken != 1 else ''} and earned 0 points.")
        
        correct_list.append(correct)
        time_list.append(time_taken)
    
    total_questions = questions
    correct_count = sum(correct_list)
    percent_correct = round((correct_count / total_questions) * 100)
    avg_time = round(sum(time_list) / total_questions, 1)
    
    print("\n--- Test Results ---")
    print(f"Final score: {score}")
    print(f"Percentage correct: {percent_correct}%")
    print(f"Average response time taken: {avg_time} seconds")
    
    if correct_count == total_questions:
        print("You're a Maths Master now!")
    
    print("\nQuestion Breakdown:")
    print(f"{'Q#':<4} {'Correct':<8} {'Time (s)':<8}")
    for idx, (correct, t) in enumerate(zip(correct_list, time_list), start=1):
        correct_str = "Yes" if correct else "No"
        print(f"{idx:<4} {correct_str:<8} {t:<8}")
    
if __name__ == "__main__":
    main()
