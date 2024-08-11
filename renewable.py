from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS listings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            description TEXT,
                            price REAL NOT NULL,
                            category TEXT NOT NULL,
                            location TEXT NOT NULL,
                            image_url TEXT
                        )''')
        conn.commit()

# Initialize the database
init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listings')
def listings():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM listings")
        all_listings = cursor.fetchall()
    return render_template('listing.html', listings=all_listings)

@app.route('/add_listing', methods=['GET', 'POST'])
def add_listing():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        category = request.form['category']
        location = request.form['location']
        image_url = request.form['image_url']
        
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO listings (title, description, price, category, location, image_url)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (title, description, price, category, location, image_url))
            conn.commit()
        return redirect(url_for('listings'))
    return render_template('add_listing.html')

if __name__ == '__main__':
    app.run(debug=True)
