import datetime
from aiogram.filters import command
from aiogram import types, Router
from aiogram.exceptions import AiogramError

from config import TASK_REPOSITORY, TASK_SERVICE
from keyboards import default_keyboard_builder, date_inline_keyboard_builder


router = Router()

@router.message(command.Command("add_task"))
async def add_task_handler(message: types.Message, command: command.CommandObject):
    if not command.args:
        await message.answer("Использование: /add_task <название>")
        return
    try:
        arg = command.args.split()
        if not arg:
            raise ValueError

        task_name = " ".join(arg[0])

    except ValueError:
        await message.answer("Используйте: /add_task <название задачи>")
    except AiogramError:
        await message.answer("Ошибка при добавлении задачи.")

    else:
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        minute = datetime.datetime.now().minute
        hour = datetime.datetime.now().hour
        keyboard = await date_inline_keyboard_builder()

        await message.answer(
            f"Дата дедлайна: {day}-{month}-{year} - {hour}:{minute}\n"
            "Выберите нужную дату кнопками ниже",
            reply_markup=keyboard
        )