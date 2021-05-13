import unittest
from calculate_bmi import calculate_bmi_per_person


class Test(unittest.TestCase):
    person = {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77}

    def test_bmi_category(self):
        calculated_bmi = calculate_bmi_per_person(self.person)
        assert(calculated_bmi['BMIcategory'] == 'Normal weight')

    def test_health_risk(self):
        calculated_bmi = calculate_bmi_per_person(self.person)
        assert(calculated_bmi['HealthRisk'] == 'Low risk')

    def test_bmi(self):
        calculated_bmi = calculate_bmi_per_person(self.person)
        assert(calculated_bmi['BMI'] == 23.77)


if __name__ == '__main__':
    unittest.main()
