# SONQO

Primero, cambiar a tu rama local:
```bash
git checkout tu_rama
```
Hacer pull de la rama 'main':
```bash
git pull origin main
```
> [!WARNING]
> Si les sale algún error de reconciliar las ramas divergentes, hagan esto:
>```bash
>git config --global pull.rebase false
>```

Ejecutar la aplicación Flask
Prerrequisitos
Debes tener python3 instalado, puedes verificarlo con:
```bash
python3 --version
```

Iniciar el entorno virtual de Python

En Windows:
```bash
myvenv\Scripts\activate
```

En Linux:
```bash
source myvenv/bin/activate
```

En la terminal les debe salir algo así:
```bash
(myvenv) ➜  sonqo-web git:(main)
```

Eso significa que están dentro del entorno virtual.

Instalar las dependencias
```bash
pip install -r requirements.txt
```

Ejecutar el servidor
```bash
python run.py
```

Les saldrá algo así:
```bash
(myvenv) ➜  sonqo-web git:(main) python run.py
 * Serving Flask app 'sonqo'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 141-320-397
```

Ahora, abran el navegador y vayan a la dirección que les haya salido. 
En este caso fue `http://127.0.0.1:5000`

Ver las páginas
Por ejemplo, para ver la página de login:
`http://127.0.0.1:5000/login`
