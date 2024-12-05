# Видеоплеер с режимами анализа эмоций и статистики

Этот проект представляет видеоплеер с двумя основными режимами работы:

1. **Просмотр видео с анализом эмоций и сбором данных**:
   - Сбор данных об эмоциях с лица зрителя (с использованием OpenCV).
   - Учет лайков/дизлайков во время просмотра.
2. **Просмотр видео с отображением статистики**:
   - Отображение статистики по ранее проведенным испытаниям.

## 🛠 Стек технологий
- **PySide6**: для создания графического интерфейса.
- **OpenCV (cv2)**: для анализа видео и определения эмоций.
- **python-vlc**: для воспроизведения видео.

## 🔧 Установка и запуск

1. Создай виртуальное окружение:
   ```bash
   python3 -m venv venv
   ```
2. Активируй виртуальное окружение:
   - Для Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - Для Windows:
     ```bash
     venv\Scripts\activate
     ```
3. Установи зависимости:
   ```bash
   pip install -e .
   ```

4. Запусти приложение:
   ```bash
   python main.py
   ```

## 📋 Как использовать
1. При запуске приложения выбери режим работы:
   - **Режим анализа эмоций**: воспроизведение видео с фиксацией эмоций и лайков/дизлайков.
   - **Режим статистики**: отображение собранной статистики по предыдущим сеансам.

## 📂 Структура проекта
- `main.py` — основной файл для запуска приложения.
- `ui/` — интерфейс приложения на PySide6.
- `utils/` — вспомогательные утилиты для обработки видео и анализа эмоций.

## 📖 Требования
- Python 3.8+
- PySide6
- OpenCV
- python-vlc

## 🤝 Вклад
Если у тебя есть идеи для улучшения или ты нашел баг, создавай pull request или issue на GitHub.

---

### ✨ Пример интерфейса
_Добавь скриншоты интерфейса, если они доступны._
