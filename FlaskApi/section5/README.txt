# Create env
virtualenv venv --python=python3.8

# For mac activate .\venv\Scripts\activate (to deactivate : deactivate)
source venv/bin/activate
# For window activate .\venv\Scripts\activate (to deactivate : deactivate)
.\venv\Scripts\activate

# Install Flask
pip install Flask

# Install Flask-RESTful
pip install Flask-RESTful

# Install Flask-JWT
pip install Flask-JWT

# If user mysql, it need to install mysql-connector-python
pip install mysql-connector-python

# Run cmd project from code
cd code
python code/app.py

