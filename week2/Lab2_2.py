age_input = input("Please enter your age: ")
age = int(age_input)

if age < 5:
    print("You're too young for movies! Enjoy cartoons.")
    
elif 5 <= age <= 12:
    print("Recommend: G-rated or PG-rated movies.")
    
elif 13 <= age <= 17:
    print("Recommend: PG-13 or R-rated (with parental guidance).")
    
else:
    print("Recommend: Any movie rating.")
    
    like_action = input("Do you like action movies? (yes/no): ").strip().lower()
    
    if like_action == "yes":
        print("You might enjoy the latest action blockbuster!")
