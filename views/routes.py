from flask import Blueprint,render_template 

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder="dashboard")


@dashboard_bp.route('/')
def dashboard():
    return render_template('dashboard/dashboard.html')
