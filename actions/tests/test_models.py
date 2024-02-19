"""
Tests to make sure our models are working as designed!
"""
from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Actions, Prompts
# Need to disable the following pylint
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

class ActionsModelTest(TestCase):
    def test_field_content(self):
        action = Actions.objects.create(name="Test Action",
                                         description="Test Description", prompt="Test Prompt")

        self.assertEqual(action.name, "Test Action")
        self.assertEqual(action.description, "Test Description")
        self.assertEqual(action.prompt, "Test Prompt")
        self.assertTrue(isinstance(action, Actions))

class PromptsModelTest(TestCase):
    def test_field_content(self):
        action = Actions.objects.create(name="Test Action",
                                         description="Test Description", prompt="Test Prompt")
        prompt = Prompts.objects.create(name="Test Prompt",
                                         description="Prompt Description", action=action)

        self.assertEqual(prompt.name, "Test Prompt")
        self.assertEqual(prompt.description, "Prompt Description")
        self.assertEqual(prompt.action, action)
        self.assertTrue(isinstance(prompt, Prompts))

class ModelRelationshipTest(TestCase):
    def test_prompts_in_actions(self):
        action = Actions.objects.create(name="Action",
                                         description="Action Description", prompt="Action Prompt")
        Prompts.objects.create(name="Prompt 1",
                               description="Description 1", action=action)
        Prompts.objects.create(name="Prompt 2",
                               description="Description 2", action=action)

        self.assertEqual(action.prompts.count(), 2)

class ActionsModelValidationTest(TestCase):
    def test_create_invalid_if_name_empty(self):
        action = Actions(name="")
        with self.assertRaises(ValidationError):
            action.full_clean()

class ActionsModelStrTest(TestCase):
    def test_str_representation(self):
        action = Actions.objects.create(name="Action Name")
        self.assertEqual(str(action), "Action Name")

class PromptsModelStrTest(TestCase):
    def test_str_representation(self):
        action = Actions.objects.create(name="Action Name")
        prompt = Prompts.objects.create(name="Test Prompt",
                                         description="Prompt Description", action=action)
        self.assertEqual(str(prompt), "Test Prompt")
