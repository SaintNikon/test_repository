# Git course: 


## Что внутри

- `train.py` — обучение простой модели на датасете Iris
- `requirements.txt` — зависимости проекта

## Установка

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск

```bash
python train.py
```

## Практика с Git

1. **Клонировать репозиторий**
   ```bash
   git clone <url-репозитория> ml-git-demo
   cd ml-git-demo
   ```

2. **Создать ветку под свою задачу**
   ```bash
   git checkout -b feature/add-metrics
   ```

3. **Внести изменения** (например, добавить вывод метрик в `train.py`), затем:
   ```bash
   git add train.py
   git commit -m "Добавлен вывод accuracy и F1"
   ```

4. **Отправить ветку на сервер**
   ```bash
   git push -u origin feature/add-metrics
   ```

5. **Создать Pull Request** в веб-интерфейсе GitHub/GitLab и попросить код-ревью.

Удачи!
