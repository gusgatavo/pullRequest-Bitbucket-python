# README -- Generador de Pull Request automatizado

Este ejecutador tiene dos formas de ejecución, las cuales son las siguientes:

1- La primera opción de ejecución corresponde a la generación de PR individual la cual se tiene que ejecutar con el siguiente comando.

    py PrBitbucket_individual.py {workspace} {repo_slug} {branch_origin} {branch_destination}

2- La segunda opción corresponde a la ejecución masiva de los PR, la cual se ejecutan con el siguiente comando:

    py PrBitbucket_Massive.py

### Configuración generica del proyecto

Para realizar la configuración general del proyecto se tiene que tener en cuenta las siguientes consideración:

1- Se tiene que configurar el usuario y la clave para lograr la comunicación con la api de Bitbucket.

Para esto se tiene que obtener el username del usuario con el que va a ejecutar el PR. Este se puede obtener con los siguientes pasos.

    1- ingresando a __settings__ -> __Account settings__
    2- En la sección "**Bitbucket profile setting**", se puede apreciar el campo "**Username**"