"""
Tests to make sure our views are working as designed!
"""
from unittest.mock import patch
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Actions
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=invalid-name

class ActionsViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Setup initial data
        cls.action = Actions.objects.create(name="Test Action",
                                            description="Test Description", prompt="Test Prompt")

    def test_get_all_actions(self):
        url = '/api/actions'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_action(self):
        url = '/api/actions'
        data = {"name": "New Action", "description": "New Description", "prompt": "New Prompt"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actions.objects.count(), 2)

    def test_retrieve_action(self):
        url = f'/api/actions/{self.action.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Action')

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
