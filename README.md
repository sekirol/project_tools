### clean.py
Скрипт очищает файлы, сгенерированные инструментом STM32CubeMX, от служебных маркеров. 

Спускается по дереву проекта и очищает все .c и .h файлы от строк вида

```c
/* USER CODE BEGIN ... */

/* USER CODE END ... */
```

Запуск скрипта производится из корня проекта STM32CubeMX.