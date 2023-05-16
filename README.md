# URL Shortner

## 💻 Development

### 🗄️ Database Setup: 
Create Database named `urlshortner` from MYSQL console.

### 👨‍💻 Project Setup: 

- Clone this repository
- Enter the shell by typing `$ pipenv shell`
- Install dependencies by typing `$ pipenv install`
- Complete the steps mentioned in **Environment variables** section
- Run migrations `$ python manage.py migrate`
- Run local server `$ python manage.py runserver`

### 🔐 Environment variables: 

- Create file `.env` inside `url_shortner` directory
- Copy contents from `.env.example` file and paste it in the `.env` file you just created.
- After copying the contents, edit the `SECRET_KEY`, `DATABASE_USER`, `DATABASE_NAME` and `DATABASE_PASSWORD` with your respective key, user, database_name and password.
