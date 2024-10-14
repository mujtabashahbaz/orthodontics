import unittest
from unittest.mock import patch
from src.openai_integration import generate_treatment_plan
from src.data_models import TreatmentPlanInputs

class TestOpenAIIntegration(unittest.TestCase):
    @patch('openai.Completion.create')
    def test_generate_treatment_plan(self, mock_openai):
        # Mock response from OpenAI
        mock_openai.return_value = type('obj', (object,), {
            'choices': [type('obj', (object,), {'text': 'Sample treatment plan'})]
        })
        
        inputs = TreatmentPlanInputs(
            patient_name="John Doe",
            age=25,
            gender="Male",
            contact_info="john.doe@example.com",
            malocclusion_type="Class I",
            crowding="Minor",
            spacing="None",
            bite_issues="Overbite",
            tmj_issues="None",
            additional_findings="Healthy gums",
            treatment_goals=["Improve dental alignment", "Enhance aesthetics"]
        )
        
        plan = generate_treatment_plan(inputs)
        self.assertEqual(plan, "Sample treatment plan")

if __name__ == '__main__':
    unittest.main()
