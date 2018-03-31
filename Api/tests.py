# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Job
from django.contrib.auth import get_user_model
# Create your tests here.

User=get_user_model()

class JobAPITestCase(APITestCase):
	def setUp(self):
		user = User(username='test',email='test@test.com')
		user.set_password('sshhshhshs1234')
		user.save()
		job=Job.objects.create(
			title='testjob',
			description='welding of windows',
			status='open',
			category="testcategoy")

	def test_single_user(self):
		user_count= User.objects.count()
		self.assertEqual(user_count,1)


	def test_single_job(self):
		Job_count= Job.objects.count()
		self.assertEqual(Job_count,1)
