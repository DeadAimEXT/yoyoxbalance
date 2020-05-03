<h1> Que es esto? </h1>

Hola, dotero HN. He aqui el responsable del balance del torneo

Es un algoritmo asqueroso y escrito en unas horas que basicamente pasa por diferentes pasos de complejidad apuntando 
a disminuir la desviacion estandard entre los promedios de los equipos.

<h2> Paso 1: Nivel JOH </h2>
Empareja al mas alto mmr con el mas bajo, el segundo mas alto con el segundo mas bajo etc
Esto se hace para tener un punto de partida decente

<h2> Paso 2: Nivel OEA </h2>
Organiza cada equipo en orden de su MMR promedio y organiza internamente el MMR de cada uno
de los jugadores. Despues compara el equipo con MMR mas alto con el mas bajo, compara cada uno
de sus jugadores segun su rank interno (el mas alto de equipo 1 vs el mas alto del equipo 2)
e intenta cambiarlos si determina que esto es favorable para lograr 2 promedios mas parecidos. Este
proceso se repite n cantidad de veces hasta que se observa mejora en la desviacion estandard 
(esto en el codigo creo que esta en 10 reps ajaber?)

<h2> Paso 3: Nivel CICIH/Yoyox </h2>
Cuando la OEA ya no puede hacer nada, viene la CICIH liderada por Yoyox y decide comparar
TODOS los jugadores del equipo #1 contra TODOS los jugadores del equipo con menos MMR,
y usando el poder de las matematicas y estadistica, hace el cambio mas apropiado para el
balance y erradicacion de la corrupcion total.


<h1> FAQ </h1>

<h3>P: Donde esta la lista de los jugadores? </h3>
R: Es privada porque algunas personas no quieren compartir su MMR, este script incluye una pequeña funcion
que crear jugadores con mmr random si la quieren probar. No todos los jugadores compartieron su MMR exacto solo
su medalla, a ellos se les asigno el valor numerico correspondiente al mmr de esa medalla promedio.

<h3>P: Podes hacer el script facil de usar para todos? </h3>
R: No quiero, pero el codigo es libre de adaptar como quieran

<h3>P: Tu codigo esta feo/puedo hacer algo mejor/se puede optimizar mas</h3>
R: Hacelo, para eso esta en github

<h3>P: Funciona con cualquier juego?</h3>
R: Teoricamente funciona con cualquier entrada en el formato [('nombre unico1', ELO Numerico1), ('nombre unico2', ELO Numerico2)...('nombre unicoN', ELO NumericoN)],
actualmente esta hecho estrictamente para equipos de 5, pero se puede parametrizar facilmente.

<h3>P: No me gusta mi team!! Fraude!!!</h3>
R: No




