#app/auth/routes
from app.auth import auth
from flask import render_template

@auth.route('/login')
def login():
    """Login Page"""
    return "<h3>Login Page</h3>"

@auth.route('/logout')
def logout():
    """Logout"""
    return "<h3>Logout</h3>"
