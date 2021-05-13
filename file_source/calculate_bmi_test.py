import unittest

from numpy import round_

from calculate_bmi import generate_bmi_categories


class Test(unittest.TestCase):
    file = "./person_data.json"

    def test_bmi_category(self):
        calculated_bmi = generate_bmi_categories(self.file)
        assert(calculated_bmi.iloc[2]['BMIcategory'] == 'Normal weight')

    def test_health_risk(self):
        calculated_bmi = generate_bmi_categories(self.file)
        assert(calculated_bmi.iloc[2]['HealthRisk'] == 'Low risk')

    def test_bmi(self):
        round_value = 2
        calculated_bmi = generate_bmi_categories(self.file)
        assert(round(calculated_bmi.iloc[2]['BMI'], round_value) == 23.77)


if __name__ == '__main__':
    unittest.main()
