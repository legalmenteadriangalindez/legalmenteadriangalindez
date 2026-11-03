import random

opciones = {
    "1": ("Charmander", "🔥 Fuego"),
    "2": ("Squirtle", "💧 Agua"),
    "3": ("Bulbasaur", "🌿 Planta"),
}

vence = {
    "🔥 Fuego": "🌿 Planta",
    "🌿 Planta": "💧 Agua",
    "💧 Agua": "🔥 Fuego",
}

print("⚔️  ¡Bienvenido al Poké-Duelo! ⚔️")
print("1) Charmander 🔥   2) Squirtle 💧   3) Bulbasaur 🌿")

victorias_jugador = 0
victorias_rival = 0

while True:
    eleccion = input("\nElige tu Pokémon (1-3) o 'q' para salir: ").strip()
    if eleccion.lower() == "q":
        break
    if eleccion not in opciones:
        print("❌ Opción inválida. Intenta de nuevo.")
        continue

    nombre_jugador, tipo_jugador = opciones[eleccion]
    nombre_rival, tipo_rival = random.choice(list(opciones.values()))

    print(f"\n🧑 Tú elegiste: {nombre_jugador} ({tipo_jugador})")
    print(f"🤖 Rival eligió: {nombre_rival} ({tipo_rival})")

    if tipo_jugador == tipo_rival:
        print("🤝 ¡Empate! Ambos son del mismo tipo.")
    elif vence[tipo_jugador] == tipo_rival:
        print(f"🎉 ¡Ganaste! {tipo_jugador} es eficaz contra {tipo_rival}.")
        victorias_jugador += 1
    else:
        print(f"💥 ¡Perdiste! {tipo_rival} es eficaz contra {tipo_jugador}.")
        victorias_rival += 1

    print(f"📊 Marcador: Tú {victorias_jugador} — {victorias_rival} Rival")

print(f"\n🏆 Resultado final: Tú {victorias_jugador} — {victorias_rival} Rival")
print("¡Gracias por jugar! ⚡")
