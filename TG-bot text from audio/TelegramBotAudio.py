from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import speech_recognition as sr
import subprocess
import asyncio
import os

TOKEN = "7159151882:AAFgjwgDN_Pun9KKokgZfvZlf4k6ferOPP0"
bot = Bot(TOKEN)
dp = Dispatcher()
r = sr.Recognizer()


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Привет! Отправь мне аудиофайл и я конвертирую его в текст!")


@dp.message(F.audio)
async def converting_audio_to_text(message: types.Message):
    split_tup = os.path.splitext(message.audio.file_name)
    print(split_tup)
    file_name = f"{split_tup[0]}_{message.from_user.full_name}{split_tup[1]}"
    print(file_name)
    await bot.download(message.audio.file_id, file_name)

    file_name_wav = f"{split_tup[0]}_{message.from_user.full_name}.wav"
    print(file_name_wav)
    subprocess.call(["ffmpeg", "-i", file_name, file_name_wav], shell=True)

    with sr.AudioFile(file_name_wav) as source:
        audio = r.record(source)
        print(audio)
    text = r.recognize_google(audio, language="ru")
    print(text)
    await message.answer(text)

    os.remove(file_name)
    os.remove(file_name_wav)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
