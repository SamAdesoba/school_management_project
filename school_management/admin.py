from django.contrib import admin


class SchoolAdminSite(admin.AdminSite):
    site_id = "My Django Project Admin Site"
    site_header = "WELCOME TO SCHOOL MANAGEMENT ADMIN INTERFACE"
    index_title = "My Django Project Index"
