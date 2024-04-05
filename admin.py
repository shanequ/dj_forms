"""
Customised Admin Site.
"""
from django.contrib import admin


class AccountAdminSite(admin.AdminSite):
    title_header = 'My Admin'
    site_header = 'My Administration Site'
    index_title = 'My Admin'
