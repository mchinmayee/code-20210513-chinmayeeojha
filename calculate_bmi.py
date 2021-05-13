
body_stats_data = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]

bmi_category = [
    'Underweight',  # 18.4 and below
    'Normal weight',  # 18.5 - 24.9
    'Overweight',  # 25 - 29.9
    'Moderately obese',  # 30 - 34.9
    'Severely obese',  # 35 - 39.9
    'Very severely obese'  # > 40
]

health_risk = [
    'Malnutrition risk',
    'Low risk',
    'Enhanced risk',
    'Medium risk',
    'High risk',
    'Very high risk'
]


def calculate_bmi(body_stats):
    bmi_calculated = []

    for person in body_stats:
        calculated_bmi = calculate_bmi_per_person(person)
        bmi_calculated.append(calculated_bmi)

    return bmi_calculated


def calculate_bmi_per_person(person):
    decimal_places = 2

    pWeight = person["WeightKg"]
    pHeight = person["HeightCm"]/100.0
    # pGender = person["Gender"]
    bmi_value = round(pWeight / pHeight, decimal_places)
    health_category = determine_health_category(bmi_value)
    person['BMI'] = bmi_value
    person['BMIcategory'] = bmi_category[health_category]
    person['HealthRisk'] = health_risk[health_category]

    return person


def determine_health_category(bmi):
    category_value = len(bmi_category)
    if bmi <= 18.4:
        category_value = 0
    elif bmi >= 18.5 and bmi <= 24.9:
        category_value = 1
    elif bmi >= 25 and bmi <= 29.9:
        category_value = 2
    elif bmi >= 30 and bmi <= 34.9:
        category_value = 3
    elif bmi >= 35 and bmi <= 39.9:
        category_value = 4
    else:
        category_value = 5

    return category_value


def main():
    calculated_bmi = calculate_bmi(body_stats_data)
    for person in calculated_bmi:
        print(person)


if __name__ == '__main__':
    main()
