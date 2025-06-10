# README -- Generador de Pull Request automatizado


## Descripción
Este proyecto esta desarrollado para genera Pull Request de manera automatica y masiva. Esto enfocado principalmente a migración con gran cantidad de componentes.

## Configuración generical del proyecto

Para realizar la configuración del proyecto Se debe tener tanto el usuario y la clave para lograr la comunicación con la api de Bitbucket.

1- Para obtener el username, se tiene que acceder a, ingresando a [settings -> Account settings](https://bitbucket.org/account/settings/).
2- En la sección "Bitbucket profile setting", se puede apreciar el campo "Username"  (Como se muestra en la imagen a continuación).
    
![obtención username](assent/UserName.svg "obtención username")
3- Para obtener la clave para realizar la conexión por medio de la api se tiene que acceder a [settings -> App passwords](https://bitbucket.org/account/settings/app-passwords/). En esta sección se tiene que presionar el botón "Create app password"
![botón de creación de clave de app](assent/AppPassword_1.svg "botón de creación de clave de app")
4- Luego de presionar el botón se abrir un formulario en donde se tiene que ingresar el nombre de la clave, y se debera escojer los permisos asociados.
![Formulario de creación de clave](assent/AppPassword_2.svg "Formulario de creación de clave")
Como se aprecia en la imagen solo damos permisos para escribir pull requests. Después presionamos el botón "Create".

5- Se levantara un modal en donde se puede apreciar la clave a utilizar.
![Modal con clave de app](assent/AppPassword_3.svg "Modal con clave de app")
6- Una vez obtenida esta información se tiene que dejar esta información en el archivo [.env](.env), en donde se tiene que pegar el username y la password app, obtenida anteriormente
    
    USER={username}
    PASSWORD={appPassword}
    

## Formas de ejecución

Este ejecutador tiene dos formas de ejecución, las cuales son las siguientes:

1- La primera opción de ejecución corresponde a la generación de PR individual la cual se tiene que ejecutar con el siguiente comando.

    py PrBitbucket_individual.py {workspace} {repo_slug} {branch_origin} {branch_destination}

2- La segunda opción corresponde a la ejecución masiva de los PR, la cual se ejecutan con el siguiente comando:

    py PrBitbucket_Massive.py

Esta ejecución obtiene la información a ejecutar desde el archivo [pullRequest.txt](pullRequest.txt). En el cual se tiene que registra la workspace, repo_slug, branch_origin, branch_destination; esto separado con una coma. Como se muesta a continuación

    {workspace},{repo_slug},{branch_origin},{branch_destination}

3- La respuesta varia dependiendo de la forma de ejecutar el proyecto. En el caso de ejecutar el flujo individual el resultado de la ejecución aparecera por pantalla.
![resultado ejecución individual](assent/ExectIndividual.svg "resultado ejecución individual")

Por otro lado en el caso de ejecutar de manera masiva se generar un archivo (result.txt), el cual contendra el resultado de cada uno de PR solicitados.
![resultado ejecución Masiva](assent/ExectMasiva.svg "resultado ejecución Masiva")
