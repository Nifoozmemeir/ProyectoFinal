# Portfolio - Instalación
Python 3.12.4 y Django 5.1

- Clonar el repo
```sh
git clone https://github.com/Nifoozmemeir/Portfolio.git
```
- Crear el entorno virtual ![windows-11-icon-logo-6C39629E45-seeklogo comasdasd](https://github.com/user-attachments/assets/3439ac37-728a-48fa-8d6f-8057f07e79fa)
```sh 
py -m venv myvenv
```
- Crear el entorno virtual ![linux-tux-logo-png-transparent-svg-vector-bie-supply-14aa](https://github.com/user-attachments/assets/bbc3c437-0056-4892-9986-ef2832156535)
```sh 
python -m venv myvenv
```
- Iniciar el entorno virtual ![windows-11-icon-logo-6C39629E45-seeklogo comasdasd](https://github.com/user-attachments/assets/3439ac37-728a-48fa-8d6f-8057f07e79fa)
```sh
.\myvenv/Scripts/activate
```
- Iniciar el entorno virtual ![linux-tux-logo-png-transparent-svg-vector-bie-supply-14aa](https://github.com/user-attachments/assets/bbc3c437-0056-4892-9986-ef2832156535)
```sh
source myvenv/Scripts/activate
```
- Actualizar pip
```sh
python -m pip install --upgrade pip
```
- Descargar dependencias
```sh
pip install -r requirements.txt
```
- Crear la base de datos ![windows-11-icon-logo-6C39629E45-seeklogo comasdasd](https://github.com/user-attachments/assets/3439ac37-728a-48fa-8d6f-8057f07e79fa)
```sh
py manage.py migrate
```
- Crear la base de datos ![linux-tux-logo-png-transparent-svg-vector-bie-supply-14aa](https://github.com/user-attachments/assets/bbc3c437-0056-4892-9986-ef2832156535)
```sh
python manage.py migrate
```
- Crear un super usuario ![windows-11-icon-logo-6C39629E45-seeklogo comasdasd](https://github.com/user-attachments/assets/3439ac37-728a-48fa-8d6f-8057f07e79fa)
```sh
py manage.py createsuperuser
```
- Crear un super usuario ![linux-tux-logo-png-transparent-svg-vector-bie-supply-14aa](https://github.com/user-attachments/assets/bbc3c437-0056-4892-9986-ef2832156535)
```sh
python manage.py createsuperuser
```
- Levantar el server ![windows-11-icon-logo-6C39629E45-seeklogo comasdasd](https://github.com/user-attachments/assets/3439ac37-728a-48fa-8d6f-8057f07e79fa)
```sh
py manage.py runserver
```
- Levantar el server ![linux-tux-logo-png-transparent-svg-vector-bie-supply-14aa](https://github.com/user-attachments/assets/bbc3c437-0056-4892-9986-ef2832156535)
```sh
python manage.py runserver
```

- ENJOY!
