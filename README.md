# Placement-Salary-Prediction

Django Web-App for Campus Placement Salary Prediction

## To run this project

1. **Clone the project**

   ```sh
   git clone https://github.com/vedantrokde/Placement-Salary-Prediction.git
   ```

2.  **Create a virtual environment using venv**

      ```sh
      python -m venv env
      source ./env/Scripts/activate
      ```

3.  **Make sure you are in *Placement-Salary-Prediction* folder**

    *<ins>Install all dependencies</ins>*

    ```sh
    pip install -r requirements.txt
    ```

    *<ins>Run Migrations</ins>*

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

    *<ins>Run Server</ins>*

    ```sh
    python manage.py runserver 
    ```

And you are good to go!!!

[Go to website](https://checkyourplacementstatus.herokuapp.com/) already deployed on heroku . . . 

In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/ to view website locally.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/vedantrokde/Placement-Salary-Prediction.git)

## Building models for prediction

1. **Download [Campus Recruitment Dataset](https://www.kaggle.com/benroshan/factors-affecting-campus-placement) in same directory**

2. **Run [save_model](https://github.com/vedantrokde/Placement-Salary-Prediction/save_model.py) :** `python save_model.py`

3. **Save created pickel models in** */Placement-Salary-Prediction/myapp/models/*.

**Refer to [scikit-learn](https://scikit-learn.org/stable/modules/classes.html) for any modification required!**
