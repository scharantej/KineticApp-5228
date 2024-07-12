## Flask Application Design for Interactive Kinetic Energy App

### HTML Files

**index.html**

- Use Bootstrap's layout for a user-friendly interface.
- Provide an introduction section explaining the concept of kinetic energy.
- Include a form with input fields for mass and velocity:
```html
<form>
  <div class="form-group">
    <label for="mass">Mass (kg):</label>
    <input type="number" class="form-control" id="mass" placeholder="Enter mass">
  </div>
  <div class="form-group">
    <label for="velocity">Velocity (m/s):</label>
    <input type="number" class="form-control" id="velocity" placeholder="Enter velocity">
  </div>
  <button type="submit" class="btn btn-primary">Calculate</button>
</form>
```

**results.html**

- Display the calculated kinetic energy based on user input:
```html
<div>
  <h2>Result:</h2>
  <p id="result"></p>
</div>
```

### Routes

**app.py**

**Route 1: GET index**

- Render the index page:
```python
@app.route('/')
def index():
    return render_template('index.html')
```

**Route 2: POST calculate**

- Receive the form data, calculate the kinetic energy using the formula KE = 1/2 * mass * velocity^2, and render the results page:
```python
@app.route('/calculate', methods=['POST'])
def calculate():
    mass = float(request.form['mass'])
    velocity = float(request.form['velocity'])
    kinetic_energy = 0.5 * mass * velocity ** 2

    return render_template('results.html', kinetic_energy=kinetic_energy)
```