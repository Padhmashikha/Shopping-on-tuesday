from app.main import main
from flask import render_template

@main.route('/')
def home():
    """Homepage"""
    return "<h3>Homepage</h3>"

@main.route('/products')
def products():
    """Products listing page"""
    return "<h5>Products</h5>"