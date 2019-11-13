# LearningML web y cuentas usuario

## Rutas web

`/` la home
`/admin` administración del CMS

`/account/login` login para los usuario, entrada a la cuenta de usuario

`/account/signup` proceso de registro de usuarios

`/projects` listado de proyectos del usuario (requiere autenticación)

## Rutas API

### Obtención del token

`POST /api/api-token-auth`

{"username": "ciro", "password": "1dcnnqa2"}

### Obtener un proyecto

`GET /projects/api/project/{id}`

headers

`Authoritation: Token 1c840aa735f78678491c6a77583d8539bb00fecd`

### Enviar un nuevo proyecto

`POST /projects/api/project`

headers

`Authoritation: Token 1c840aa735f78678491c6a77583d8539bb00fecd`

body

`{"name":"el proyectongazo ","description":"isisisisisissdsada","json_data":"{\"lilu\":\"lala\", \"klkl\":\"jdd\"}"}`

### Modificar un proyecto

`PUT /projects/api/project/{id}`

headers

`Authoritation: Token 1c840aa735f78678491c6a77583d8539bb00fecd`

body

`{"name":"el proyectongazo modificado","description":"isisisisisissdsada","json_data":"{\"lilu\":\"lala\", \"klkl\":\"jdd\"}"}`

## Borrar un proyecto

`DELETE /projects/api/project/{id}`

headers

`Authoritation: Token 1c840aa735f78678491c6a77583d8539bb00fecd`


/api/project/id
path('api/project', views.ApiProjectListView.as_view(), name='projects'),
    path('api/project/<int:pk>', views.ApiProjectDetailView.as_view())