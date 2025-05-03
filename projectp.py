def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def health_suggestions(category):
    suggestions = {
        "Underweight": """
            Health Suggestions:
            - Increase calorie intake with nutrient-dense foods like nuts, seeds, and whole grains.
            - Include more protein in your diet (e.g., lean meats, eggs, dairy, legumes).
            - Regular strength training can help build muscle mass.
            - Consult a healthcare provider if you're struggling to gain weight.
        """,
        "Normal weight": """
            Health Suggestions:
            - Keep up your balanced diet with plenty of fruits, vegetables, and whole grains.
            - Include regular physical activity (e.g., walking, swimming, cycling) to maintain your weight.
            - Stay hydrated and get enough sleep (7-9 hours a night).
            - Consider incorporating mindfulness or stress-reduction techniques.
        """,
        "Overweight": """
            Health Suggestions:
            - Focus on a balanced, calorie-controlled diet rich in whole foods like fruits, vegetables, lean proteins, and whole grains.
            - Engage in regular physical activities, such as walking, jogging, or swimming.
            - Gradually reduce portion sizes and limit sugary or high-fat foods.
            - Consult a healthcare provider for a personalized weight-loss plan.
        """,
        "Obesity": """
            Health Suggestions:
            - Work with a healthcare provider to create a personalized weight management plan.
            - Focus on a sustainable, nutrient-dense diet with fewer processed foods and sugars.
            - Incorporate daily physical activities like brisk walking, swimming, or cycling.
            - Seek support from a professional for weight management and possible lifestyle changes.
        """
    }
    return suggestions.get(category, "Stay healthy and active!")

def convert_to_metric(weight, height, unit_type):
    if unit_type == 'imperial':
        # Convert weight from pounds to kilograms and height from inches to meters
        weight = weight * 0.453592
        height = height * 0.0254
    return weight, height

def get_user_input():
    # Asking for units
    unit_type = input("Enter unit type (metric or imperial): ").strip().lower()
    if unit_type not in ['metric', 'imperial']:
        print("Invalid unit type. Please enter either 'metric' or 'imperial'.")
        return None, None, None

    # Taking weight and height inputs
    weight = float(input("Enter weight: "))
    height = float(input("Enter height: "))

    # Convert to metric if imperial units were used
    if unit_type == 'imperial':
        weight, height = convert_to_metric(weight, height, unit_type)

    return weight, height, unit_type

# Main program
print("Welcome to the Advanced BMI Calculator!")

# Get user input
weight, height, unit_type = get_user_input()

if weight and height:
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    # Categorize BMI
    category = categorize_bmi(bmi)
    # Get health suggestions based on BMI category
    suggestions = health_suggestions(category)

    # Display result
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")
    print(suggestions)
