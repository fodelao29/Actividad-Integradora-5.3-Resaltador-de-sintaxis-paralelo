# Parallel-Syntaxis-Highlighter

# Reporte: Actividad Integradora 5.3 Resaltador de sintaxis paralelo 

### Rodolfo de la O - A01366363

### Santiago Sorzano - A01769673

## Resumen
En este repositorio se encuentra la solución a la actividad integradora 5.3 que se nos pide una continuación de la actividad integradora 3.4 pasada, pero en este caso estaremos utilizando un sistema en paralelo que permite a los hilos trabajar simultáneamente y así generar más procesos a la vez.

## Reflexión:
Tuvimos varias complicaciones a cerca de las ideas que planteamos ya que en un principio queríamos utilizar un código que pudiera dar nombre y crear nuevos archivos html para así poder resaltar cada uno de estos archivos, pero no resultó ser la mejor forma, por lo que cambiamos de idea y nos funcionó de mejor manera, ya que esta nueva versión del código nos asegura el buen funcionamiento del mismo mientras que busca hacer los procesos de manera eficiente y rápida.

## Complejidad:
“0.42” “0.47” “0.42” “0.47” “0.42” Con una media de 0.44 segundos en las 5 pruebas realizadas pudimos observar que este método es mucho más eficiente que el visto en la actividad 3.4, ya utiliza todos los hilos a la vez. 

En nuestro código nosotros buscamos la manera más rápida de poder obtener resultados correctos, lo cual hacía que hubiera un gran nivel de complejidad ya que se buscaba darle a sintaxis a varios archivos, a pesar de se sigue el mismo proceso que si solo se quisiera leer un archivo, el hecho de leer más y en una cantidad de tiempo limitada hacia que esto tuviera demasiada complejidad, llegando al punto de crear distintas versiones durante un periodo de tiempo muy corto y generando distintos errores.

## Implicaciones éticas:
Esta forma de programación permite una mejora considerable al acortar los tiempos de espera, pero también exige mucho más de los equipos de cómputo, ya que utiliza todos los hilos posibles al mismo tiempo, esto tiene ventajas computacionalmente hablando pero en la parte ética de este vemos que estamos impulsando a generar procesadores que consumen mas y mas energia llevando esto a unos límites antes inalcanzables tan solo para lograr más velocidad, esto está dando pie a crisis ambientales hasta incluso al calentamiento global debido a que dia a dia estamos utilizando cantidades inmensurables de energía que con el paso del tiempo se hará cada vez más grande si continuamos en este camino.

De igual manera los códigos actuales son muy fáciles de compartir y utilizar, ya sea el ejemplo más popular github, donde cualquier usuario puede hacer uso de cualquier código que sea público, ya se para fines lucrativos o negativos, gracias a que el acceso a compartir información es tan fácil nos ha permitido acelerar la tecnología al punto en el que está ahora pero al mismo tiempo cada vez es más difícil darle el mérito a la persona que lo merece porque es muy fácil que alguien haya logrado robar su código.

## Conclusión:
Este es un proyecto que nos da bastante conocimiento ya que aprendimos usar los hilos o los multiprocesos, y que tienen bastantes aplicaciones en otras áreas de la programación actual, siendo a la fecha parte importante de las inteligencias artificiales y de aparatos que usamos todos los días ya sea Alexa, Google Nest, entre otros.