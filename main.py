
# Import necessary modules
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    """
    Render the main page.
    """
    return render_template('index.html')

# Define the route for the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calculate the kinetic energy.
    """
    # Get the form data
    mass = float(request.form['mass'])
    velocity = float(request.form['velocity'])

    # Calculate the kinetic energy
    kinetic_energy = 0.5 * mass * velocity ** 2

    # Render the results page
    return render_template('results.html', kinetic_energy=kinetic_energy)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
