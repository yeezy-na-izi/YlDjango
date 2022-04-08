# YlDjango

[Проект братюни](https://github.com/extroot/yandexLyceumPlus)

## Проект для Яндекс Лицея ++

В этом проекте проходит все обучение в Яндексе на направлении Django

### Для запуска

Установка зависимостей
```
pip install -r requirements.txt
```

Создание виртуального окружения (можно посмотреть в файле .env.example)
```
echo > .env 'SECRET_KEY="your-secret-key"\nDEBUG=True' 
```

Создание и обновление базы данных
```
python manage.py migrate
```

Запуск сервера
```
python manage.py runserver
```

