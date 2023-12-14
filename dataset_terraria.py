# Описание датасета Terraria: NAME - НАЗВАНИЕ ПРЕДМЕТОВ, CLASS - КЛАСС ПЕРСОНАЖА, GAME PROGRESSION - ПРОГРЕСС ИГРЫ, DPS (SINGLE TARGET) - УРОР ПО ОДИНОЧНОЙ ЦЕЛИ, DPS (MULTI TARGET) - УРОН ПО МНОГОЦЕЛЕВОЙ, DPS (SINGLE TARGET + PROYECTILE ONLY) - УРОН ТОЛЬКО ОДИНОЧНОЙ ЦЕЛИ + СНАРЯД, DPS (MULTI TARGET + PROYECTILE ONLY) - УРОН ТОЛЬКО ДЛЯ НЕСКОЛЬКИХ ЦЕЛЕЙ + СНАРЯД, OBSERVATIONS - НАБЛЮДЕНИЕ

import pandas as pd
import numpy as np
Terraria = pd.read_csv("Terraria.csv")
Terraria

# Этап 2: После этого требуется вывести данные с использованием команды вашдатасет.head().

Terraria.head()

# Этап 3: Затем необходимо отобразить размерность массива, используя вашдатасет.shape.

Terraria.shape

# Этап 4: Далее требуется вывести наименование всех колонок, написать что они означают в нашем датасете с помощью .columns

Terraria.columns

# Этап 5: Затем необходимо вывести все уникальные значения с помощью .unique

Terraria['CLASS'].unique()

# Этап 6: Далее нужно сделать сортировку по определенным параметрам с помощью .sort_values

Terraria.sort_values(by='DPS (SINGLE TARGET)')

# Этап 7: Затем необходимо выполнить удаление ненужных столбцов или строк с помощью .drop

Terraria.drop(columns = ["OBSERVATIONS"], inplace=True)

#Этап 8: Далее нужно заменить определенные значения в датасете (например, пустые) с помошью .replace

Terraria["GAME PROGRESSION"] = Terraria["GAME PROGRESSION"].replace(Terraria["GAME PROGRESSION"].unique(), "Unknown")
Terraria

# Этап 9: Затем необходимо выполнить удаление дубликатов с помощью .drop_duplicates()

Terraria = Terraria.drop_duplicates()
Terraria

# Этап 10: Далее нужно провести анализ с помощью функций .describe()

Terraria.describe()

# Этап 11: Затем необходимо Провести выборку данных по строкам и столбцам с помощью .loc

subset = Terraria.loc[[0, 1, 2], ['NAME', 'CLASS']]
subset

# Этап 12: Далее нужно Провести анализ с помощью функций .info()

Terraria.info()

# Финальный этап: Необходимо сохранить наш датасет с помощью .to_csv и написать в конце нужный индекс. Если он False то не будет сохранен, а если True то он сохраниться

Terraria.to_csv("Terraria_clear.csv", index=True)
Terraria