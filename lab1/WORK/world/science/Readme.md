# 📘 Проект "Книга знаний"

Этот проект собирает информацию о космосе в удобные Markdown-файлы.

## 👥 Команда
- Филенков Л. А
- Бычков Д. А
- Кострюков Е. С
- Шутов Д. О

## 🎯 Концептуализация

Наша онтология описывает основные концепции астрономии и космологии, включая:
- Основные астрономические объекты (Вселенная, Галактика, Звезда)
- Физические концепции (Гравитация, Масса)
- Космологические явления (Большой взрыв, Расширение Вселенной)
- Научные дисциплины (Астрономия, Космология)
- Специальные объекты (Черные дыры, Белые дыры, Метеориты)

Связи между понятиями включают:
- Иерархические связи (например, Вселенная → Галактика → Звезда)
- Причинные связи (например, Большой взрыв → Расширение Вселенной)
- Связи влияния (например, Гравитация влияет на Массу)
- Связи принадлежности (например, Метеорит связан со Звездой)

## 🚀 Граф связей

```mermaid
graph TD;

    %% Основные объекты
    Вселенная[Вселенная] --> Галактика[Галактика]
    Вселенная --> Большой_взрыв[Большой взрыв]
    Вселенная --> Расширение_Вселенной[Расширение Вселенной]

    %% Иерархия астрономических тел
    Галактика --> Звезда[Звезда]
    Звезда --> Черная_дыра[Черная дыра]
    Звезда --> Белая_дыра[Белая дыра]

    %% Физические концепции
    Большой_взрыв --> Расширение_Вселенной
    Альберт_Эйнштейн[Альберт Эйнштейн] --> Общая_теория_относительности[Общая теория относительности]
    Общая_теория_относительности --> Гравитация[Гравитация]
    Гравитация --> Масса[Масса]

    %% Научные дисциплины
    Астрономия[Астрономия] --> Вселенная
    Космология[Космология] --> Темная_материя[Темная материя]
    Космология --> Наблюдаемая_Вселенная[Наблюдаемая Вселенная]

    %% Связи второго порядка
    Метеорит[Метеорит] --> Звезда
    Черная_дыра --> Гравитация
    Белая_дыра --> Гравитация

    %% Добавляем ссылки
    click Вселенная "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Вселенная.md" "Открыть статью"
    click Галактика "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Галактика.md" "Открыть статью"
    click Большой_взрыв "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Большой_взрыв.md" "Открыть статью"
    click Расширение_Вселенной "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Расширение_вселенной.md" "Открыть статью"
    click Звезда "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Звезда.md" "Открыть статью"
    click Черная_дыра "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Черная_дыра.md" "Открыть статью"
    click Белая_дыра "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Белая_дыра.md" "Открыть статью"
    click Альберт_Эйнштейн "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Альберт_Эйнштейн.md" "Открыть статью"
    click Общая_теория_относительности "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Общая_теория_относительности.md" "Открыть статью"
    click Гравитация "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Гравитация.md" "Открыть статью"
    click Масса "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Масса.md" "Открыть статью"
    click Астрономия "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Астрономия.md" "Открыть статью"
    click Космология "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Космология.md" "Открыть статью"
    click Темная_материя "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Темная_материя.md" "Открыть статью"
    click Наблюдаемая_Вселенная "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Наблюдаемая_вселенная.md" "Открыть статью"
    click Метеорит "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/world/science/Метеорит.md" "Открыть статью"
