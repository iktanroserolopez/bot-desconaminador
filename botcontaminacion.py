import  discord


from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def hola(ctx):
    await ctx.send("Soy tu asistente virtual, aquí para ayudarte a entender y combatir la contaminación ambiental. Juntos podemos aprender sobre las causas, efectos y soluciones para proteger nuestro planeta. Si tienes alguna pregunta o necesitas información específica, no dudes en preguntar. ¡Vamos a hacer del mundo un lugar más limpio y saludable!")
@bot.command()
async def informacion(ctx):
    await ctx.send("""

presentacion de comandos texto : 
                   /hola
                   /informacion
                   /ayuda
                   /animalo
                   /informacionener
                   /impact
                   /word
                   /goodword
                   /renov
                   /reutilizar
                   /ambiente
                   /util
                   /contaminacion
                   /limpieza
                   /remplazoplastico
                   /desperdicioalimentario
                   /dividirBasura
                   /image1
                   /image2
                   /image3
                   /image4
                   /image5
                   """)
@bot.command()
async def ayuda(ctx):
    await ctx.send("""
Cómo Ayudar a Reducir la Contaminación Desde Casa

Reducir la contaminación desde casa es más fácil de lo que parece. Aquí hay algunas acciones simples que puedes tomar:

Reduce el uso de plásticos: Opta por productos reutilizables como botellas y bolsas de tela.
Ahorra energía: Apaga las luces y desconecta los aparatos electrónicos cuando no los uses.
Recicla: Separa los residuos y recicla papel, vidrio, plástico y metales.
Usa productos ecológicos: Elige productos de limpieza y de cuidado personal que sean amigables con el medio ambiente.
Ahorra agua: Repara las fugas y utiliza dispositivos de bajo consumo de agua.
Planta árboles: Los árboles ayudan a purificar el aire y a reducir el CO2.
Cada pequeña acción cuenta y, juntas, pueden hacer una gran diferencia en la lucha contra la contaminación.
                   
                   """)


@bot.command()
async def animalo(ctx):
    await ctx.send("""
La contaminación tiene efectos devastadores en los animales. Aquí hay algunos ejemplos de cómo diferentes tipos de contaminación los afectan:

Contaminación del aire: Puede causar problemas respiratorios, cáncer y alterar los patrones de migración. Los animales pueden sufrir daños en sus órganos y tener una menor tasa de éxito reproductivo12.
Contaminación del agua: Los productos químicos y metales pesados en el agua pueden ser absorbidos por anfibios y peces, afectando su salud y la de los depredadores que se alimentan de ellos. Esto puede llevar a deformidades, enfermedades y muerte3.
Contaminación del suelo: Los pesticidas y otros contaminantes pueden ser absorbidos por las plantas y entrar en la cadena alimentaria, afectando a los animales que dependen de estas plantas para alimentarse3.
Contaminación acústica: El ruido excesivo en los océanos afecta la capacidad de los mamíferos marinos para navegar, comunicarse y detectar peligros4.
Reducir la contaminación es crucial para proteger la biodiversidad y la salud de los ecosistemas.
                   """)
    
@bot.command()
async def informacionener(ctx):
    await ctx.send("""
Recomendación de Energías Limpias

Las energías limpias son esenciales para un futuro sostenible. Fuentes como la solar, eólica, hidroeléctrica y geotérmica no solo reducen la emisión de gases de efecto invernadero, sino que también disminuyen nuestra dependencia de los combustibles fósiles. Al optar por energías renovables, contribuimos a la protección del medio ambiente y a la mejora de la calidad del aire. Además, estas energías son inagotables y cada vez más accesibles. Adoptar energías limpias es un paso crucial hacia un planeta más saludable y un legado positivo para las futuras generaciones.
                   
                   """)
    
@bot.command()
async def impact(ctx):
    await ctx.send("""

Riesgos e Impactos de la Contaminación

La contaminación afecta gravemente tanto a la salud humana como al medio ambiente. En las personas, puede causar enfermedades respiratorias, cardiovasculares y cáncer, además de problemas neurológicos. En el medio ambiente, contribuye al cambio climático, la acidificación del suelo y del agua, y la pérdida de biodiversidad. La contaminación del agua y del suelo también puede dañar los ecosistemas y afectar la vida acuática. Reducir la contaminación es esencial para proteger nuestra salud y el planeta.
                   
                   """)
    
@bot.command()
async def word(ctx):
    await ctx.send("""
Un Mundo Sin Contaminación

Imagínate un mundo sin contaminación: el aire sería puro y fresco, permitiendo respirar sin preocupaciones. Los ríos y océanos estarían limpios, llenos de vida marina saludable. Los bosques y campos florecerían, proporcionando hábitats seguros para la fauna. Las ciudades serían más verdes y tranquilas, con menos ruido y más espacios naturales. La salud humana mejoraría, con menos enfermedades respiratorias y cardiovasculares. Un mundo sin contaminación sería un lugar más saludable y hermoso para todos los seres vivos.
                   
                   """)
    
@bot.command()
async def goodword(ctx):
    await ctx.send("""
Lugares que Cambiaron por Reutilizar

En muchas partes del mundo, la reutilización ha transformado comunidades enteras. Por ejemplo, en San Francisco, la implementación de programas de reutilización y reciclaje ha reducido significativamente los residuos enviados a los vertederos, convirtiendo a la ciudad en un líder en sostenibilidad1. En Ámsterdam, la reutilización de materiales de construcción ha dado lugar a innovadores proyectos de vivienda sostenible2. Además, en Japón, la práctica de “mottainai” (no desperdiciar) ha llevado a la creación de mercados de segunda mano y tiendas de reparación, promoviendo una cultura de reutilización y reducción de residuos3. Estos ejemplos demuestran cómo la reutilización puede tener un impacto positivo y duradero en nuestras comunidades y el medio ambiente.
                   
                   """)
  
@bot.command()
async def renov(ctx):
    await ctx.send ("puedes comprar paneles solares,esa es la opcion economica")
@bot.command()
async def reutilizar(ctx):
    await ctx.send ("puedes reulilizar papel imprimido,carton o otras cosas, puedes aprender como en youtube.com")
@bot.command()
async def ambiente(ctx):
    await ctx.send ("el medio ambiente es muy delicado y al usar productos plasticos u otros que dañen el ambiente hay menos y menos comida")
@bot.command()
async def util(ctx):
    await ctx.send ("no usar productos de un solo uso como toallas humedas o papel de baño almenos que sea nesesario")

@bot.command()
async def contaminacion(ctx):
    await ctx.send("""aqui hay algunas formas en las que la contaminacion afecta al mundo:
Salud Humana: Contamina el aire, agua y suelo, causando enfermedades respiratorias, cardiovasculares y problemas gastrointestinales, además de aumentar la carga en los sistemas de salud.
Ecosistemas: Degrada hábitats naturales y pone en peligro la biodiversidad, afectando la vida de plantas y animales y alterando el equilibrio ecológico.
Cambio Climático: Aumenta los gases de efecto invernadero, acelerando el calentamiento global, causando fenómenos climáticos extremos y elevando el nivel del mar, lo que pone en riesgo a las comunidades costeras y la estabilidad global.
                   """)
@bot.command()
async def limpieza(ctx):
    await ctx.send("""una de las formas para ayudar a hacer de tu ciudad un lugar mas limpio es salir a limpiar la calle donde vives o ir a limpiar tu parque mas cercano asi ayudas a hacer del planeta un lugar mas limpio""")

@bot.command()
async def remplazoplastico(ctx):
    await ctx.send("""
Existen varios materiales que se pueden utilizar como sustitutos del plástico,
como el papel, las fibras naturales (como el algodón, el cáñamo o el yute) y las bolsas reutilizables hechas de materiales reciclados (como el nylon o el poliéster)
por ejemplo usar bolsas de tela o envases o frascos de vidrio
""")
    
@bot.command()
async def desperdicioalimentario(ctx):
    await ctx.send("""
Reducir el desperdicio alimentario es importante, por varias razones.
Mejora la nutrición y la seguridad alimentaria mundial, ya que proporciona una dieta saludable a una población en crecimiento.
Además, reduce las emisiones de gases de efecto invernadero y ahorra financieramente para empresas y consumidores.
""")
    
@bot.command()
async def dividirBasura(ctx):
    await ctx.send("""
 Aquí te dejo algunos consejos sobre cómo dividir la basura:

Orgánica: Desechos de comida, restos de frutas y verduras.
Inorgánica: Plásticos, vidrios, metales y papel.
Reciclable: Botellas de plástico, latas, cartón y papeles limpios.
No reciclable: Papel higiénico, pañales, y otros residuos sanitarios.
¡Recuerda! Separar correctamente los residuos ayuda a cuidar el medio ambiente.
""")
@bot.command()
async def image1(ctx):
    await ctx.send(file=discord.File("botcomandos/contaminacion.jpeg"))

@bot.command()
async def image2(ctx):
    await ctx.send(file=discord.File("botcomandos/contaminacion1.jpg"))

@bot.command()
async def image3(ctx):
    await ctx.send(file=discord.File("botcomandos/dead.jpg"))

@bot.command()
async def image4(ctx):
    await ctx.send(file=discord.File("botcomandos/megacon.jpeg"))

@bot.command()
async def image5(ctx):
    await ctx.send(file=discord.File("botcomandos/mundo.jpeg"))

bot.run("introduce tu token de discord")
