from django.test import TestCase
from .models import Complaint
from django.utils import timezone

class ComplaintModelTest(TestCase):

    def setUp(self):
        self.complaint = Complaint.objects.create(
            name='Test User',
            email='test@example.com',
            category='fraud',
            description='Test complaint about online fraud.',
            date_reported=timezone.now()
        )

    def test_complaint_creation(self):
        """Check that the complaint was created properly."""
        self.assertEqual(self.complaint.name, 'Test User')
        self.assertEqual(self.complaint.email, 'test@example.com')
        self.assertEqual(self.complaint.category, 'fraud')
        self.assertEqual(self.complaint.description, 'Test complaint about online fraud.')

    def test_string_representation(self):
        """Check the __str__ method of Complaint."""
        self.assertEqual(str(self.complaint), 'Test User - fraud')
