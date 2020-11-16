# Make code folder
mkdir code

# Create Vỉtualenv
virtualenv venv --python=python3.8

# Activate venv
./venv/Scripts/activate

# Install vendor: Flask, Flask-JWT, Flask-RESTful, Flask-SQLAlchemy
pip install Flask
pip install Flask-JWT
pip install Flask-RESTful
pip install Flask-SQLAlchemy

