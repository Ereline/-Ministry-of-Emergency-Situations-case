import pandas as pd
import folium
from folium.plugins import HeatMap
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Загрузка данных из CSV
data = pd.read_csv('/content/prognoZ.csv')

# Создание словаря для соответствия мест и их названий
places = {
    -21: "Александровский МО",
    -20:	"Бардымский МО",
    -19:	"Березовский МО",
    -18:	"Большесосновский МО",
    -17:	"Верещагинский ГО",
    -16:	"Гайнский МО",
    -15:	"ГО город Березники",
    -14:	"ГО город Кизел",
    -13:	"Горнозаводский ГО",
    -12:	"Губахинский МО",
    -11:	"Добрянский ГО",
    -10:	"Еловский МО",
    -9:	"ЗАТО Звездный",
    -8:	"Ильинский ГО",
    -7:	"Карагайский МО",
    -6:	"Кишертский МО",
    -5:	"Косинский МО",
    -4:	"Кочевский МО",
    -3:	"Красновишерский ГО",
    -2:	"Краснокамский ГО",
    -1:	"Кудымкарский МО",
    0:	"Куединский МО",
    1:	"Кунгурский МО",
    2:	"Лысьвенский ГО",
    3:	"Нытвенский ГО",
    4:	"Октябрьский ГО",
    5:	"Ординский МО",
    6:	"Осинский ГО",
    7:	"Оханский ГО",
    8:	"Очерский ГО",
    9:	"Пермский ГО",
    10:	"Пермский МО",
    11:	"Сивинский МО",
    12:	"Соликамский ГО",
    13:	"Суксунский ГО",
    14:	"Уинский МО",
    15:	"Чайковский ГО",
    16:	"Частинский МО",
    17:	"Чердынский ГО",
    18:	"Чернушинский ГО",
    19:	"Чусовской ГО",
    20:	"Юрлинский МО",
    21: "Юсьвинский МО"
}

# Создание словаря для соответствия мест и координат
coords = {
    "Александровский МО": (59.159248, 57.604019),
    "Бардымский МО": (56.892502, 55.654850),
    "Березовский МО": (57.646149, 57.546398),
    "Большесосновский МО": (57.542999, 54.459251),
    "Верещагинский ГО": (58.125900, 54.444901),
    "Гайнский МО": (60.531399, 53.509449),
    "ГО город Березники": (59.401470, 56.799480),
    "ГО город Кизел": (59.043308, 57.654510),
    "Горнозаводский ГО": (58.587849, 58.662750),
    "Губахинский МО": (58.864891, 57.603008),
    "Добрянский ГО": (58.460300, 56.408859),
    "Еловский МО": (56.948799, 54.820599),
    "ЗАТО Звездный": (57.730000, 56.299999),
    "Ильинский ГО": (58.628349, 55.767948),
    "Карагайский МО": (58.451599, 55.008099),
    "Кишертский МО": (57.337002, 57.582649),
    "Косинский МО": (59.847252, 55.026051),
    "Кочевский МО": (59.738251, 54.407951),
    "Красновишерский ГО": (60.736198, 57.996799),
    "Краснокамский ГО": (58.079781, 55.731541),
    "Кудымкарский МО": (59.060848, 54.638149),
    "Куединский МО": (56.550850, 55.225948),
    "Кунгурский МО": (57.536350, 56.560699),
    "Лысьвенский ГО": (58.100380, 57.804329),
    "Нытвенский ГО": (58.116798, 55.381302),
    "Октябрьский ГО": (56.499451, 56.906052),
    "Ординский МО": (57.065250, 56.740349),
    "Осинский ГО": (57.284698, 55.451900),
    "Оханский ГО": (57.653198, 55.198002),
    "Очерский ГО": (57.894001, 54.599201),
    "Пермский ГО": (57.834850, 56.092350),
    "Пермский МО": (57.997169, 56.235279),
    "Сивинский МО": (58.468498, 54.214649),
    "Соликамский ГО": (59.636250, 56.766788),
    "Суксунский ГО": (57.056000, 57.564701),
    "Уинский МО": (56.864948, 56.528149),
    "Чайковский ГО": (56.764381, 54.106319),
    "Частинский МО": (57.307152, 54.738998),
    "Чердынский ГО": (60.683201, 56.852001),
    "Чернушинский ГО": (56.532349, 56.190300),
    "Чусовской ГО": (58.288189, 57.826660),
    "Юрлинский МО": (59.434250, 54.231152),
    "Юсьвинский МО": (59.066898, 55.483799)
}

# Создание отдельных карт и CSV-файлов для каждой категории
event_columns = ["Аварии на транспорте", "Аварии с выбросами опасных веществ", "Опасные природные явления", "ЖКХ", "Взрывы, пожары, разрушения", "Прочие опасности"]

# Определите цвета для красного, желтого и зеленого
red_color = mcolors.to_rgba("red")
yellow_color = mcolors.to_rgba("yellow")
green_color = mcolors.to_rgba("green")

# Определите диапазон значений от 0% до 100%
min_value = 0
max_value = 100

# Создание градиента цветов
gradient = mcolors.LinearSegmentedColormap.from_list('custom_gradient', [red_color, yellow_color, green_color])

for column in event_columns:
    # Создание карты
    m = folium.Map(location=[58.594189, 56.315815], zoom_start=7)

    # Создание сводной таблицы для текущей категории
    event_summary = data.groupby("Место")[column].mean().reset_index()
    event_summary["Место"] = event_summary["Место"].map(places)

    for index, row in event_summary.iterrows():
        place = row["Место"]
        risk_percent = row[column] * 100  # У каждой категории уже есть только одна колонка
        color = f"hsl({100 - risk_percent}, 100%, 50%)"  # Градиент от красного (100%) до зеленого (0%)

        if place in coords:
            folium.CircleMarker(
                location=coords[place],
                radius=15,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                popup=f"{place}: {risk_percent:.2f}%"
            ).add_to(m)

    # Отображение карты в интерактивном режиме
    m.save(f'map_{column}.html')

    # Сохранение таблицы в CSV-файл
    event_summary = event_summary.sort_values("Место")
    event_summary.to_csv(f'event_summary_{column}.csv', index=False)