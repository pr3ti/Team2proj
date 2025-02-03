from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample car inventory data
cars = [
    {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2021},
]

# Home page - Display all cars
@app.route('/')
def index():
    return render_template('index.html', cars=cars)

# Add a new car
@app.route('/add', methods=['POST'])
def add_car():
    if request.method == 'POST':
        new_id = len(cars) + 1
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']

        cars.append({"id": new_id, "make": make, "model": model, "year": int(year)})
    return redirect(url_for('index'))

# Delete a car
@app.route('/delete/<int:car_id>')
def delete_car(car_id):
    global cars
    cars = [car for car in cars if car["id"] != car_id]
    return redirect(url_for('index'))

# Update car information
@app.route('/update/<int:car_id>', methods=['POST'])
def update_car(car_id):
    for car in cars:
        if car["id"] == car_id:
            car["make"] = request.form["make"]
            car["model"] = request.form["model"]
            car["year"] = int(request.form["year"])
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

