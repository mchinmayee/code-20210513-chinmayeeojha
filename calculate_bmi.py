import json

import pandas as pd
import numpy as np


file = "./person_data.json"


def generate_bmi_categories(data_file):
    data = pd.read_json(data_file)

    data['BMI'] = data['WeightKg']/(data['HeightCm']/100.0) ** 2

    conditions = [(data['BMI'] <= 18.4), (data['BMI'] <= 24.9),
                  (data['BMI'] <= 29.9), (data['BMI'] <= 34.9), (data['BMI'] <= 39.9), (data['BMI'] >= 40)]

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

    data['BMIcategory'] = np.select(conditions, bmi_category)

    data['HealthRisk'] = np.select(conditions, health_risk)

   #  print(data.head())
    return data


def main():
    generate_bmi_categories(file)


if __name__ == '__main__':
    main()
