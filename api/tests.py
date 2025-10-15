"""
Tests for the profile API endpoint.
"""
from django.test import TestCase, Client
from unittest.mock import patch
import json


class ProfileEndpointTests(TestCase):
    """Test cases for the /me endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_timestamp_updates_dynamically(self):
        """Test that timestamp changes between requests."""
        import time
        
        response1 = self.client.get('/me')
        data1 = json.loads(response1.content)
        
        time.sleep(0.1)  # Small delay
        
        response2 = self.client.get('/me')
        data2 = json.loads(response2.content)
        
        # Timestamps should be different
        self.assertNotEqual(data1['timestamp'], data2['timestamp'])

    def test_fact_field_exists(self):
        """Test that fact field is present and non-empty."""
        response = self.client.get('/me')
        data = json.loads(response.content)
        
        self.assertIn('fact', data)
        self.assertIsInstance(data['fact'], str)
        self.assertGreater(len(data['fact']), 0)

    @patch('api.views.requests.get')
    def test_cat_fact_api_integration(self, mock_get):
        """Test successful cat fact API integration."""
        # Mock successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'fact': 'Test cat fact'
        }
        
        response = self.client.get('/me')
        data = json.loads(response.content)
        
        self.assertEqual(data['fact'], 'Test cat fact')

    @patch('api.views.requests.get')
    def test_cat_fact_api_fallback(self, mock_get):
        """Test fallback when cat fact API fails."""
        # Mock API failure
        mock_get.side_effect = Exception('API Error')
        
        response = self.client.get('/me')
        data = json.loads(response.content)
        
        # Should still return 200 with fallback fact
        self.assertEqual(response.status_code, 200)
        self.assertIn('fact', data)
        self.assertIsInstance(data['fact'], str)

    def test_only_get_method_allowed(self):
        """Test that only GET requests are accepted."""
        post_response = self.client.post('/me')
        self.assertEqual(post_response.status_code, 405)
        
        put_response = self.client.put('/me')
        self.assertEqual(put_response.status_code, 405)
        
        delete_response = self.client.delete('/me')
        self.assertEqual(delete_response.status_code, 405)

    def test_endpoint_returns_200(self):
        """Test that the endpoint returns a 200 status code."""
        response = self.client.get('/me')
        self.assertEqual(response.status_code, 200)

    def test_response_content_type(self):
        """Test that the response has correct content type."""
        response = self.client.get('/me')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_response_structure(self):
        """Test that the response has the correct structure."""
        response = self.client.get('/me')
        data = json.loads(response.content)
        
        # Check top-level fields
        self.assertIn('status', data)
        self.assertIn('user', data)
        self.assertIn('timestamp', data)
        self.assertIn('fact', data)
        
        # Check user object fields
        self.assertIn('email', data['user'])
        self.assertIn('name', data['user'])
        self.assertIn('stack', data['user'])

    def test_status_field_value(self):
        """Test that status field is 'success'."""
        response = self.client.get('/me')
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')

    def test_user_fields_are_strings(self):
        """Test that user fields contain string values."""
        response = self.client.get('/me')
        data = json.loads(response.content)
        
        self.assertIsInstance(data['user']['email'], str)
        self.assertIsInstance(data['user']['name'], str)
        self.assertIsInstance(data['user']['stack'], str)

    def test_timestamp_format(self):
        """Test that timestamp is in ISO 8601 format."""
        response = self.client.get('/me')
        data = json.loads(response.content)
        
        # Check timestamp contains expected characters for ISO format
        timestamp = data['timestamp']
        self.assertIn('T', timestamp)
        self.assertIn('Z', timestamp)
        self.assertTrue(timestamp.endswith('Z'))

