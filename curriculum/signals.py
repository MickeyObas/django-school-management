"""
Assign courses to each and every student based on their level and department of study. For example, 100 level CSC students will take CSC 101, MTS 101, PHY 101 etc.
"""

from django.dispatch import receiver
from django.db.models.signals import post_save
