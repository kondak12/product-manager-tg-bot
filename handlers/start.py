from aiogram.filters import command
from aiogram import types, Router


router = Router()

@router.message(command.CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Данный бот предназначен для ведения списка задач.\n\n"
                         "Основные команды:\n"
                         " - /start – Начало работы/перезагрузка бота\n"
                         " - /register – Регистрация нового пользователя\n"
                         " - /login – Авторизация пользователя для доступа к его задачам\n"
                         " - /add_task <название> <дедлайн> <приоритет> <описание> – Создание новой задачи\n"
                         " - /tasks – Вывод списка всех задач\n"
                         " - /reminders <установка/изменение> – Настройка напоминаний\n"
                         " - /statistics <период в днях> – Просмотр статистики\n"
                         " - /help – Список доступных команд и инструкция по их использованию\n")