from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Actions, Context
# pylint: disable=no-member

class ActionsModelTestNoContext(TestCase):
    def test_field_content(self):
        action = Actions.objects.create(name="Test Action", description="Test Description",
                                        prompt="Test Prompt", success_criteria="Test Success Criteria")
        self.assertEqual(action.name, "Test Action")
        self.assertEqual(action.description, "Test Description")
        self.assertEqual(action.success_criteria, "Test Success Criteria")
        self.assertEqual(action.prompt, "Test Prompt")
        self.assertIsNotNone(action.created)
        self.assertTrue(isinstance(action, Actions))

class ActionsModelTestWithContext(TestCase):
    def test_field_content(self):
        context = Context.objects.create(name="Test Context",
                                         description="Context Description")
        action = Actions.objects.create(name="Test Action", description="Test Description",
                                        prompt="Test Prompt", success_criteria="Test Success Criteria",
                                        context = context)
        self.assertEqual(action.name, "Test Action")
        self.assertEqual(action.description, "Test Description")
        self.assertEqual(action.success_criteria, "Test Success Criteria")
        self.assertEqual(action.prompt, "Test Prompt")
        self.assertEqual(action.context, context)
        self.assertIsNotNone(action.created)
        self.assertTrue(isinstance(action, Actions))

class ActionsModelTestAddContextLater(TestCase):
    def test_field_content(self):
        context = Context.objects.create(name="Test Context",
                                         description="Context Description")
        action = Actions.objects.create(name="Test Action", description="Test Description",
                                        prompt="Test Prompt", success_criteria="Test Success Criteria")
        self.assertEqual(action.name, "Test Action")
        self.assertEqual(action.description, "Test Description")
        self.assertEqual(action.success_criteria, "Test Success Criteria")
        self.assertEqual(action.prompt, "Test Prompt")
        self.assertIsNotNone(action.created)
        self.assertTrue(isinstance(action, Actions))

        action.context = context
        action.save()

        updated_action = Actions.objects.get(id=action.id)
        self.assertEqual(updated_action.context, context)

class ActionsModelValidationTest(TestCase):
    def test_create_invalid_if_name_empty(self):
        action = Actions(name="")
        with self.assertRaises(ValidationError):
            action.full_clean()

class ActionsModelStrTest(TestCase):
    def test_str_representation(self):
        action = Actions.objects.create(name="Action Name")
        self.assertEqual(str(action), "Action Name")

class ContextsModelTest(TestCase):
    def test_field_content(self):
        context = Context.objects.create(name="Test Context",
                                         description="Context Description")

        self.assertEqual(context.name, "Test Context")
        self.assertEqual(context.description, "Context Description")
        self.assertTrue(isinstance(context, Context))
