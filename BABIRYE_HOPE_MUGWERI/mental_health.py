emotions = {
        1: "Terrible",
        2: "Very Bad",
        3: "Bad",
        4: "Not Good",
        5: "Neutral",
        6: "Good",
        7: "Very Good",
        8: "Great",
        9: "Excellent",
        10: "Superb"
    }

rating = int(input("Please enter your mental health rating (1-10): "))
if  rating <= 10:
                print( rating, emotions[rating])
else:
                print("Invalid rating. Please enter a number between 1 and 10.")
        
print("Thank you for sharing your mental health rating.")
print("Your rating:", rating)
print("Emotion associated with your rating:", emotions)




