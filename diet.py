# The Health Words

# BMI: A quick score that tells you if you are underweight, normal, or overweight for your height.

# BMR: The number of calories your body burns just to stay alive if you lay in bed all day doing absolutely nothing.

# TDEE: The total calories you burn in a day once you add your daily walking, working, and workouts to your BMR.

# Calorie Target: The number of calories you need to eat each day to hit your weight goal.

# Activity Factor: A number used to multiply your BMR based on how much you move (sitting all day vs. exercising hard).

# Aim: Your main goal—whether you want to lose weight, gain muscle, or stay the same.



# # Define a function to calculate Body Mass Index (BMI) using weight (kg) and height (cm)
# def bmi_calculator(weight, height):
#     # Convert height from cm to meters, square it, and divide weight by that value
#     bmi = weight / ((height / 100) ** 2)
#     # Send back the calculated BMI value, rounded to 2 decimal places
#     return round(bmi, 2)


# # Define a function to calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation
# def bmr_calculator(gender, age, weight, height):
#     # Check if the text inside the 'gender' variable matches exactly "male"
#     if gender == "male":
#         # Calculate standard male BMR using weight, height, and age formulas
#         bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
#         # Send the calculated male BMR value back to where the function was called
#         return bmr
#     # If gender wasn't male, check if it matches exactly "female"
#     elif gender == "female":
#         # Calculate standard female BMR (subtracts 161 instead of adding 5)
#         bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
#         # Send the calculated female BMR value back to where the function was called
#         return bmr


# # Define a function to calculate Total Daily Energy Expenditure (TDEE) based on activity level
# def tdee_calculator(bmr, activity):
#     # Create a dictionary (lookup table) pairing activity descriptions with their numeric multipliers
#     activity_factor = {
#         "Sedentary": 1.20,
#         "Lightly Active": 1.375,
#         "Moderately Active": 1.55,
#         "Very Active": 1.75,
#         "Extra Active": 1.90,
#     }
#     # Look up the multiplier using the 'activity' key and multiply it by the baseline BMR value
#     tdee = bmr * activity_factor[activity]
#     # Send back the calculated TDEE value, rounded to 2 decimal places
#     return round(tdee, 2)


# # Define a function to adjust daily calories based on the user's fitness goal
# def calorie_target(tdee, aim):
#     # Check if the fitness goal matches exactly "weight maintain"
#     if aim == "weight maintain":
#         # Maintenance calories are equal to the standard TDEE value
#         calorie = tdee
#     # Check if the fitness goal matches exactly "weight loss"
#     elif aim == "weight loss":
#         # Subtract 400 calories from TDEE to create a caloric deficit for fat loss
#         calorie = tdee - 400
#     # Check if the fitness goal matches exactly "weight gain"
#     elif aim == "weight gain":
#         # Add 300 calories to TDEE to create a caloric surplus for muscle building
#         calorie = tdee + 300
#     # Send back the final targeted calorie value, rounded to 2 decimal places
#     return round(calorie, 2)


# # Call bmi_calculator with 60kg and 150cm, then print the result directly to the screen
# print("your BMI is=", bmi_calculator(60, 150))


# # Call bmr_calculator for a 25yo male (50kg, 150cm) and print the result directly to the screen
# print("Your BMR is=", bmr_calculator("male", 25, 50, 150))
# # Run bmr_calculator again with the same values and save the result into a variable named 'bmr'
# bmr = bmr_calculator("male", 25, 50, 150)

# # Call tdee_calculator using our saved 'bmr' variable and "Very Active", then print the result
# print("Your tdee=", tdee_calculator(bmr, "Very Active"))

# # Run tdee_calculator again with the same values and save the output into a variable named 'tdee'
# tdee = tdee_calculator(bmr, "Very Active")
# # This line is a comment (ignored by Python) showing a alternative way to structure print statements
# # tdee=("Your tdee=",tdee_calculator(bmr,"Very Active"))


# # Call calorie_target using our 'tdee' variable and "weight loss", then print the final target
# print("Your calorie target is=", calorie_target(tdee, "weight loss"))




def bmi_calculator(weight, height): # Body Mass Index
    bmi = weight / ((height/100)**2) # weight must be in kg and height in m (Conversion)
    return round(bmi,2)

def bmr_calculator(weight, height, age, gender): # Basal Metabolic Rate (Diff. for Male & Female)
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        return bmr
    elif gender == "female":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        return bmr

def tdee_calculator(bmr, activity): # Total Daily Energy Expenditure (Activity Factor --> Some other factors)
    #Define all the factors
    activity_factor = {
        "Sedentary": 1.20, 
        "Lightly_Active": 1.375, 
        "Moderately_Active": 1.55, 
        "Very_Active": 1.725, 
        "Extra_Active": 1.90
    }
    tdee = bmr * activity_factor[activity]
    return round(tdee,2)

def calorie_target(tdee, aim):
    if aim == "weight maintain":
        calorie = tdee
    elif aim == "weight loss":
        calorie = tdee - 400
    elif aim == "weight gain": 
        calorie = tdee + 300
    return calorie

# print(bmi_calculator(90, 180))
# print(bmr_calculator(90, 170, 24, "male"))
# bmr = bmr_calculator(90, 170, 24, "male")
# print(tdee_calculator(bmr, "Moderately_Active"))
# tdee = tdee_calculator(bmr, "Moderately_Active")
# print("Your Final T")
# print(calorie_target(tdee, "weight loss"))