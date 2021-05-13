import unittest
from calculate_bmi import calculate_bmi_per_person


class Test(unittest.TestCase):
    person = {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77}

    def test_bmi_category(self):
        calculated_bmi = calculate_bmi_per_person(self.person)
        assert(calculated_bmi['BMIcategory'] == 'Very severely obese')

    def test_health_risk(self):
        calculated_bmi = calculate_bmi_per_person(self.person)
        assert(calculated_bmi['HealthRisk'] == 'Very high risk')

    def test_bmi(self):
        calculated_bmi = calculate_bmi_per_person(self.person)
        assert(calculated_bmi['BMI'] == 42.78)


if __name__ == '__main__':
    unittest.main()
