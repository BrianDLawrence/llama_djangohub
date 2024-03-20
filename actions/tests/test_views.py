from unittest.mock import patch
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Actions, Context
# pylint: disable=no-member
# pylint: disable=invalid-name

class ActionsViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.action = Actions.objects.create(name="Test Action", description="Test Description",
                                            prompt="Test Prompt", success_criteria="New Success Criteria")
        cls.context = Context.objects.create(name="Test Context",description="Test Description")

    def test_get_all_actions(self):
        url = '/api/actions'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"],"Test Action")

    def test_create_action(self):
        url = '/api/actions'
        data = {"name": "New Action", "description": "New Description",
                "prompt": "New Prompt", "success_criteria":"New Success Criteria"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actions.objects.count(), 2)

    def test_retrieve_action(self):
        url = f'/api/actions/{self.action.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Action')
        self.assertEqual(response.data['success_criteria'], 'New Success Criteria')

    def test_update_action(self):
        url = f'/api/actions/{self.action.id}'
        data = {"name": "Updated Action",
                 "description": self.action.description, "prompt": self.action.prompt}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.action.refresh_from_db()
        self.assertEqual(self.action.name, "Updated Action")

    def test_destroy_action(self):
        url = f'/api/actions/{self.action.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Actions.objects.count(), 0)

    @patch('actions.views.publish')
    def test_send_action(self, mock_publish):
        url = f'/api/send/{self.action.id}'
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that 'publish' was called once with the correct arguments
        mock_publish.assert_called_once_with(self.action)

    @patch('actions.views.get_amount_unanswered_messages')
    def test_check_sends_not_answered(self, mock_get_amount_unanswered_messages):
        mock_get_amount_unanswered_messages.return_value = 0
        url = '/api/get_amount_unanswered_messages'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], 0)
        mock_get_amount_unanswered_messages.assert_called_once()

    def test_associate_context_with_action(self):
        url = f'/api/addcontextaction/{self.action.id}'
        data = {"contextid": self.context.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data["context"],self.context.id)
        self.action.refresh_from_db()
        self.assertEqual(self.action.context, self.context)

class ContextViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.context = Context.objects.create(name="Test Context",description="Test Description")

    def test_get_all_contexts(self):
        url = '/api/context'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"],"Test Context")

    def test_create_context(self):
        url = '/api/context'
        data = {"name": "New Context", "description": "New Description"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Context.objects.count(), 2)

    def test_destroy_context(self):
        url = f'/api/context/{self.context.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Context.objects.count(), 0)

    def test_update_context(self):
        url = f'/api/context/{self.context.id}'
        data = {"name": "Updated Context",
                 "description": self.context.description}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.context.refresh_from_db()
        self.assertEqual(self.context.name, "Updated Context")
