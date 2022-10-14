from django.contrib import admin


class SchoolAdminSite(admin.AdminSite):
    site_id = "My Django Project Admin Site"
    site_header = "Welcome to the my Django Project Admin Interface"
    index_title = "My Django Project Index"
