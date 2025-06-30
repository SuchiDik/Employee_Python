from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from logger import logger
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

# 🔗 Backend API URL (Update this when deploying)
API_URL = "http://127.0.0.1:8000"

# 🔑 Authentication token (for demo)
HEADERS = {"Authorization": "Bearer mysecrettoken"}


# ✅ Home - List Employees
@app.route('/')
def index():
    try:
        response = requests.get(f"{API_URL}/employees/", headers=HEADERS)
        if response.status_code == 200:
            employees = response.json()
        else:
            employees = []
            flash("Failed to fetch employees.", "danger")
        return render_template('index.html', employees=employees)
    except Exception as e:
        logger.error(f"Error fetching employees: {e}")
        flash("Error connecting to backend.", "danger")
        return render_template('index.html', employees=[])


# ✅ Create Employee

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            data = {
                "name": request.form['name'],
                "department": request.form['department'],
                "email": request.form['email']
            }
            response = requests.post(f"{API_URL}/employees/", json=data, headers=HEADERS)
        except:
            flash("Error connecting to backend.", "danger")
            return redirect(url_for('index'))
        if response.status_code == 200:
                flash("Employee added successfully!", "success")
        else:
                flash("Failed to add employee.", "danger")
                return redirect(url_for('index'))
    return render_template('add.html')

 # ✅ Delete Employee
@app.route('/delete/<int:emp_id>')
def delete(emp_id):
    try:
        response = requests.delete(f"{API_URL}/employees/{emp_id}", headers=HEADERS)
        if response.status_code == 200:
            flash("Employee deleted successfully!", "success")
        else:
            flash("Failed to delete employee.", "danger")
    except Exception as e:
        logger.error(f"Error deleting employee: {e}")
        flash("Error connecting to backend.", "danger")
    return redirect(url_for('index'))


# ✅ Search Employees
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    try:
        response = requests.get(
            f"{API_URL}/employees/search/",
            params={'query': query, 'skip': 0, 'limit': 10},
            headers=HEADERS
        )
        if response.status_code == 200:
            employees = response.json()
        else:
            employees = []
            flash("Search failed.", "danger")
        return render_template('index.html', employees=employees, search_query=query)
    except Exception as e:
        logger.error(f"Error searching employees: {e}")
        flash("Error connecting to backend.", "danger")
        return render_template('index.html', employees=[], search_query=query)


if __name__ == '__main__':
    print("In main")
    #port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, port=8000)
