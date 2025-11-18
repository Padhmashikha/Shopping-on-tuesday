#app/admin/routes
from app.admin import admin
from flask import render_template

@admin.route('/super-admin')
def super_admin():
    """Admin login"""
    return "<h3>Super Admin Page</h3>"