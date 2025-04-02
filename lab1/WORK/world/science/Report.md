# 📘 Проект "Книга знаний"

Этот проект собирает информацию о космосе в удобные Markdown-файлы.

## 🚀 Граф связей

```mermaid
graph TD;

    %% Основные объекты
    Вселенная[Вселенная] --> Галактика[Галактика]
    Вселенная --> Большой_взрыв[Большой взрыв]
    Вселенная --> Расширение_Вселенной[Расширение Вселенной]

    %% Иерархия астрономических тел
    Галактика --> Звезда[Звезда]
    Звезда --> Чёрная_дыра[Чёрная дыра]
    Звезда --> Белая_дыра[Белая дыра]

    %% Физические концепции
    Большой_взрыв --> Расширение_Вселенной
    Альберт_Эйнштейн[Альберт Эйнштейн] --> Общая_теория_относительности[Общая теория относительности]
    Общая_теория_относительности --> Гравитация[Гравитация]
    Гравитация --> Масса[Масса]

    %% Научные дисциплины
    Астрономия[Астрономия] --> Вселенная
    Космология[Космология] --> Тёмная_материя[Тёмная материя]
    Космология --> Наблюдаемая_Вселенная[Наблюдаемая Вселенная]

    %% Связи второго порядка
    Метеорит[Метеорит] --> Звезда
    Чёрная_дыра --> Гравитация
    Белая_дыра --> Гравитация

    %% Добавляем ссылки
    click Вселенная "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Вселенная.md" "Открыть статью"
    click Галактика "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Галактика.md" "Открыть статью"
    click Большой_взрыв "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Большой_взрыв.md" "Открыть статью"
    click Расширение_Вселенной "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Расширение_вселенной.md" "Открыть статью"
    click Звезда "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Звезда.md" "Открыть статью"
    click Чёрная_дыра "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Черная_дыра.md" "Открыть статью"
    click Белая_дыра "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Белая_дыра.md" "Открыть статью"
    click Альберт_Энштейн "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Альберт_Энштейн.md" "Открыть статью"
    click Общая_теория_относительности "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Общая_теория_относительности.md" "Открыть статью"
    click Гравитация "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Гравитация.md" "Открыть статью"
    click Масса "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Масса.md" "Открыть статью"
    click Астрономия "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Астрономия.md" "Открыть статью"
    click Космология "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Космология.md" "Открыть статью"
    click Тёмная_материя "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Темная_материя.md" "Открыть статью"
    click Наблюдаемая_Вселенная "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Наблюдаемая_вселенная.md" "Открыть статью"
    click Метеорит "https://github.com/EvgenyMAI/AI-labs/blob/main/lab1/KIDBOOK/Метеорит.md" "Открыть статью"