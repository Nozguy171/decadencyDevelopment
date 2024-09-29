
# Documentación de la API

Esta documentación describe los endpoints disponibles en la API desarrollada con Flask y Supabase.

## Autenticación

### 1. Inicio de Sesión

**Endpoint:** `/auth/login`  
**Método:** `POST`  
**Descripción:** Permite a los usuarios iniciar sesión proporcionando sus credenciales.

**Cuerpo de la Solicitud:**
```json
{
    "email": "usuario@example.com",
    "password": "tu_contraseña"
}
```

**Respuesta Exitosa:**
```json
{
    "Mensaje": "Inicio de sesión exitoso",
    "JWT": "token_de_acceso"
}
```

**Errores:**
- **400 Bad Request**: Si faltan credenciales.
    ```json
    {
        "Error": "Faltan credenciales"
    }
    ```
- **500 Internal Server Error**: Si hay un error en la autenticación.
    ```json
    {
        "Error": "Descripción del error"
    }
    ```

---

### 2. Registro de Usuario

**Endpoint:** `/auth/singUp`  
**Método:** `POST`  
**Descripción:** Permite a los usuarios registrarse proporcionando un correo electrónico y una contraseña.

**Cuerpo de la Solicitud:**
```json
{
    "email": "nuevo_usuario@example.com",
    "password": "tu_contraseña"
}
```

**Respuesta Exitosa:**
```json
{
    "Mensaje": "Registro exitoso"
}
```

**Errores:**
- **400 Bad Request**: Si faltan credenciales.
    ```json
    {
        "Error": "Faltan credenciales"
    }
    ```
- **500 Internal Server Error**: Si hay un error en el registro.
    ```json
    {
        "Error": "Descripción del error"
    }
    ```

---

### 3. Cierre de Sesión

**Endpoint:** `/auth/signOut`  
**Método:** `POST`  
**Descripción:** Permite a los usuarios cerrar sesión.

**Respuesta Exitosa:**
```json
{
    "Mensaje": "Cierre de sesión exitoso"
}
```

---

## Manejo de Texto

### 4. Calificación de Texto

**Endpoint:** `/texto`  
**Método:** `POST`  
**Descripción:** Permite enviar un texto para ser calificado y genera un audio a partir de la respuesta.

**Cuerpo de la Solicitud:**
```json
{
    "text": "Texto a calificar"
}
```

**Encabezado Requerido:**
```
Authorization: Bearer token_de_acceso
```

**Respuesta Exitosa:**
```json
{
    "Respuesta_Geminai": "Respuesta de calificación",
    "Audio_URL": "URL_del_audio_generado"
}
```

**Errores:**
- **401 Unauthorized**: Si no se proporciona un token válido.
    ```json
    {
        "Error": "No se proporcionó un token válido"
    }
    ```
- **404 Not Found**: Si no se pudo obtener el texto de la solicitud.
    ```json
    {
        "Respuesta": "No se pudo obtener el texto de la petición"
    }
    ```
- **500 Internal Server Error**: Si hay un error al manejar el texto o generar audio.
    ```json
    {
        "Error": "Descripción del error"
    }
    ```

---

## Notas Adicionales

- Asegúrate de tener las variables de entorno correctamente configuradas para que la API funcione correctamente.
- Esta API utiliza Google Generative AI y AWS Polly para la calificación de texto y la generación de audio, respectivamente.
