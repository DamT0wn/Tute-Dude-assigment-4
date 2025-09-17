# Tute-Dude-assigment-3

📌 Flask + MongoDB Atlas + API Project

This project demonstrates a Flask application with the following features:

A /api route that returns JSON data stored in a local file (data.json).

A frontend form that inserts user data into MongoDB Atlas.

On successful submission, the user is redirected to a success page.
If there’s an error, it is displayed on the same form page without redirection.

🚀 Features

Flask Backend with routes:

/api → Returns JSON from data.json.

/ → Displays a form for submitting data.

/success → Displays confirmation message.

MongoDB Atlas Integration for storing form data.

Error Handling → Shows errors on form page without reloading.

Templating with Jinja2 (Flask render_template).

📂 Project Structure
flask_app/
│── app.py              # Main Flask app
│── data.json           # Sample data file for API
│── templates/
│     └── form.html     # HTML form for frontend
│── README.md           # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <your-repo-url>
cd flask_app

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3️⃣ Install Dependencies
pip install flask pymongo

🛠 MongoDB Atlas Setup

Go to MongoDB Atlas
.

Create a free cluster.

Create a database named mydatabase and collection mycollection.

Whitelist your IP or allow access from anywhere.

Get the connection string and update in app.py:

client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/test")

▶️ Running the Application

Run Flask server:

python app.py


You’ll see:

 * Running on http://127.0.0.1:5000/

🌐 Usage

Visit http://127.0.0.1:5000/api → Returns JSON data from data.json.

Visit http://127.0.0.1:5000/ → Displays the form.

Submit the form:

✅ Success → Redirects to /success page → "Data submitted successfully!"

❌ Error → Displays error message on form page.

🧪 Example JSON Response

GET /api

[
  {"id": 1, "name": "Alice", "email": "alice@example.com"},
  {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

📜 License

This project is open-source and free to use for learning purposes.
