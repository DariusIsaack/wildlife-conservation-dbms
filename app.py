from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (username, password)
        )

        user = cur.fetchone()

        cur.close()
        conn.close()

        if user:
            return redirect('/dashboard')
        else:
            return "Invalid login credentials"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():

    conn = get_connection()
    cur = conn.cursor()

    # Total animals
    cur.execute("SELECT COUNT(*) FROM animals")
    animal_count = cur.fetchone()[0]

    # Total habitats
    cur.execute("SELECT COUNT(*) FROM habitats")
    habitat_count = cur.fetchone()[0]

    # Total observations
    cur.execute("SELECT COUNT(*) FROM observations")
    observation_count = cur.fetchone()[0]

    # Total incidents
    cur.execute("SELECT COUNT(*) FROM incidents")
    incident_count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return render_template(
        'dashboard.html',
        animal_count=animal_count,
        habitat_count=habitat_count,
        observation_count=observation_count,
        incident_count=incident_count
    )

@app.route('/animals')
def animals():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT animal_id, species, tag_id, age, health_status, habitat_id
        FROM animals
        ORDER BY animal_id
    """)

    animals = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('animals.html', animals=animals)

@app.route('/add_animal', methods=['POST'])
def add_animal():
    species = request.form['species']
    tag_id = request.form['tag_id']
    age = request.form['age']
    health_status = request.form['health_status']
    habitat_id = request.form['habitat_id']

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO animals (species, tag_id, age, health_status, habitat_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (species, tag_id, age, health_status, habitat_id))

    conn.commit()

    cur.close()
    conn.close()

    return redirect('/animals')
@app.route('/delete_animal/<int:id>')
def delete_animal(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM animals WHERE animal_id = %s", (id,))

    conn.commit()

    cur.close()
    conn.close()

    return redirect('/animals')

@app.route('/edit_animal/<int:id>', methods=['GET', 'POST'])
def edit_animal(id):
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        species = request.form['species']
        tag_id = request.form['tag_id']
        age = request.form['age']
        health_status = request.form['health_status']
        habitat_id = request.form['habitat_id']

        cur.execute("""
            UPDATE animals
            SET species=%s,
                tag_id=%s,
                age=%s,
                health_status=%s,
                habitat_id=%s
            WHERE animal_id=%s
        """, (species, tag_id, age, health_status, habitat_id, id))

        conn.commit()

        cur.close()
        conn.close()

        return redirect('/animals')

    cur.execute("""
        SELECT animal_id, species, tag_id, age, health_status, habitat_id
        FROM animals
        WHERE animal_id=%s
    """, (id,))

    animal = cur.fetchone()

    cur.close()
    conn.close()

    return render_template('edit_animal.html', animal=animal)

@app.route('/habitats')
def habitats():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT habitat_id, name, location, type
        FROM habitats
        ORDER BY habitat_id
    """)

    habitats = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('habitats.html', habitats=habitats)

@app.route('/add_habitat', methods=['POST'])
def add_habitat():
    name = request.form['name']
    location = request.form['location']
    habitat_type = request.form['type']

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO habitats (name, location, type)
        VALUES (%s, %s, %s)
    """, (name, location, habitat_type))

    conn.commit()

    cur.close()
    conn.close()

    return redirect('/habitats')

@app.route('/delete_habitat/<int:id>')
def delete_habitat(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM habitats WHERE habitat_id = %s",
        (id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect('/habitats')

@app.route('/edit_habitat/<int:id>', methods=['GET', 'POST'])
def edit_habitat(id):
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        habitat_type = request.form['type']

        cur.execute("""
            UPDATE habitats
            SET name=%s,
                location=%s,
                type=%s
            WHERE habitat_id=%s
        """, (name, location, habitat_type, id))

        conn.commit()

        cur.close()
        conn.close()

        return redirect('/habitats')

    cur.execute("""
        SELECT habitat_id, name, location, type
        FROM habitats
        WHERE habitat_id=%s
    """, (id,))

    habitat = cur.fetchone()

    cur.close()
    conn.close()

    return render_template('edit_habitat.html', habitat=habitat)

@app.route('/observations')
def observations():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            o.observation_id,
            a.species,
            s.name,
            o.location,
            o.notes,
            o.observation_date
        FROM observations o
        JOIN animals a ON o.animal_id = a.animal_id
        JOIN staff s ON o.staff_id = s.staff_id
        ORDER BY o.observation_id
    """)

    observations = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('observations.html', observations=observations)

@app.route('/add_observation', methods=['POST'])
def add_observation():
    animal_id = request.form['animal_id']
    staff_id = request.form['staff_id']
    location = request.form['location']
    notes = request.form['notes']

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO observations (
            animal_id,
            staff_id,
            location,
            notes
        )
        VALUES (%s, %s, %s, %s)
    """, (animal_id, staff_id, location, notes))

    conn.commit()

    cur.close()
    conn.close()

    return redirect('/observations')

@app.route('/delete_observation/<int:id>')
def delete_observation(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM observations WHERE observation_id = %s",
        (id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect('/observations')

@app.route('/reports')
def reports():
    conn = get_connection()
    cur = conn.cursor()

    # Animals per habitat
    cur.execute("""
        SELECT h.name, COUNT(a.animal_id)
        FROM habitats h
        LEFT JOIN animals a
        ON h.habitat_id = a.habitat_id
        GROUP BY h.name
    """)
    animals_per_habitat = cur.fetchall()

    # Average age
    cur.execute("""
        SELECT species, AVG(age)
        FROM animals
        GROUP BY species
    """)
    avg_age = cur.fetchall()

    # Observations per staff
    cur.execute("""
        SELECT s.name, COUNT(o.observation_id)
        FROM staff s
        LEFT JOIN observations o
        ON s.staff_id = o.staff_id
        GROUP BY s.name
    """)
    observation_count = cur.fetchall()

    # Incidents
    cur.execute("""
        SELECT a.species, i.incident_type
        FROM animals a
        JOIN incidents i
        ON a.animal_id = i.animal_id
    """)
    incidents = cur.fetchall()

    cur.close()
    conn.close()

    # Chart Data
    habitat_labels = [row[0] for row in animals_per_habitat]
    habitat_counts = [row[1] for row in animals_per_habitat]

    staff_labels = [row[0] for row in observation_count]
    staff_counts = [row[1] for row in observation_count]

    return render_template(
        'reports.html',

        animals_per_habitat=animals_per_habitat,
        avg_age=avg_age,
        observation_count=observation_count,
        incidents=incidents,

        habitat_labels=habitat_labels,
        habitat_counts=habitat_counts,

        staff_labels=staff_labels,
        staff_counts=staff_counts
    )

if __name__ == '__main__':
    app.run(debug=True)