import random
def get_computer_choice():
    return random.choice(["قیچی" ,"کاغذ" ,"سنگ"])
def get_winner(player , computer):
    if player == computer:
        return "مساوی!"
    elif (player == "سنگ" and computer == "قیچی") or \
         (player == "کاغذ" and computer == "سنگ") or \
         (player == "قیچی" and computer == "کاغذ"):
        return "تو بردی!"
    else:
        return "کامپیوتر برد!"
choices = ["قیچی" ,"کاغذ" ,"سنگ"]
while True:
    print("\n1. سنگ  2. کاغذ  3. قیچی  4. خروج") 
    choice = input("انتخاب کن: ")
    if choice == "4":
        break
    elif choice in ["1", "2", "3"]:
        player = choices[int(choice) - 1] 
        computer = get_computer_choice()
        print(f"تو: {player} | کامپیوتر: {computer}") 
        print(get_winner(player , computer))
        