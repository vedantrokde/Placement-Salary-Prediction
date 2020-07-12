# Placement-Salary-Prediction
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/vedantrokde/Placement-Salary-Prediction.git)

`Django` Web-App for Campus Placement Salary Prediction

## How to run this project

1. **Clone the project**

```sh
git clone https://github.com/vedantrokde/Placement-Salary-Prediction.git
```

2.  **Create a virtual-env using venv**

```sh
python -m venv env
source ./env/Scripts/activate
```

3.  **Make sure you are in *Placement-Salary-Prediction* folder**

    1. Install all dependencies

    ```sh
    pip install -r requirements.txt
    ```

    2. Run Migrations

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

    3. Run Server

    ```sh
    python manage.py runserver 
    ```

And you are good to go!!!
In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/
