## Installation Instructions for the app:
1. Install Flask using `pip install flask`
2. Clone the app using `git clone https://github.com/JSnakegitHub/Challenge-3.git`

## Getting Started With Tests:
### For Python 2:
1. `pip install pytest`
2. `pip install coverage report`
3. `pip install pytest-cov`
4. `pip install pytest-xdist`
### For Python 3:
1. `pip3 install pytest`
2. `pip3 install coverage report`
3. `pip3 install pytest-cov`
4. `pip3 install pytest-xdist`
## Running the tests on a virtual environment
### For python 2:
1. `pip install -U virtualenv`
2. `python -m virtualenv venv`
3. `source venv/bin/activate` # in Windows -> venv\Scripts\activate.bat
4. `pip install pytest`
### For Python 3:
1. `pip3 install -U virtualenv`
2. `python3 -m virtualenv venv`
3. `source venv/bin/activate` # in Windows -> venv\Scripts\activate.bat
4. `pip install pytest`
### For Python 3.6+:
2. `python3 -m venv venv`
3. `source venv/bin/activate` # in Windows -> venv\Scripts\activate.bat
4. `pip install pytest`
### What The Tests Are Testing:
1. If the required endpoints are rendered.
2. If the requests are being sent in the right format (JSON-JavaScript Object Notation).
3. If Validations are being respected

## Testing the App Locally.
1. [Postman](https://www.getpostman.com/) should be used to test the application locally
2. Move to the project directory locally
3. Once you are in the project's root directory, run the command `python run.py`.
4. At this point the server should be running.
5. The application is set to run on port 8080 
