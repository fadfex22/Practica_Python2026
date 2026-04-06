def ejercicio10():

    rounds = [
        {
            'theme': 'Entrada',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
                'Lucia': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
            }
        },
        {
            'theme': 'Plato principal',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Lucia': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            }
        },
        {
            'theme': 'Postre',
            'scores': {
                'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
                'Lucia': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            }
        }
    ]

    general = {
        "Valentina": {'Puntaje': 0, 'Victorias': 0, 'Mejor': 0},
        "Mateo": {'Puntaje': 0, 'Victorias': 0, 'Mejor': 0},
        "Camila": {'Puntaje': 0, 'Victorias': 0, 'Mejor': 0},
        "Santiago": {'Puntaje': 0, 'Victorias': 0, 'Mejor': 0},
        "Lucia": {'Puntaje': 0, 'Victorias': 0, 'Mejor': 0}
    }

    for ronda in rounds:
        puntos_max = 0
        ganador_ronda = ""

        for chef in ronda['scores']:
            puntos_actuales = sum(ronda['scores'][chef].values())
            general[chef]['Puntaje'] += puntos_actuales

            if puntos_actuales > general[chef]['Mejor']:
                general[chef]['Mejor'] = puntos_actuales

            if puntos_actuales > puntos_max:
                puntos_max = puntos_actuales
                ganador_ronda = chef

        general[ganador_ronda]['Victorias'] += 1

        print(f"\n--- TABLA LUEGO DE: {ronda['theme']} ---")
        for nombre in general:
            print(f"{nombre}: {general[nombre]['Puntaje']} pts acumulados")

    print("\n" + "=" * 50)
    print("TABLA FINAL DE POSICIONES")
    print("=" * 50)

    final_ordenado = sorted(general.items(), key=lambda x: x[1]['Puntaje'], reverse=True)

    for nombre, datos in final_ordenado:
        total = datos['Puntaje']
        vics = datos['Victorias']
        mejor = datos['Mejor']
        promedio = total / len(rounds)

        print(f"{nombre} -> Total: {total} | Vics: {vics} | Mejor: {mejor} | Promedio: {promedio:.1f}")