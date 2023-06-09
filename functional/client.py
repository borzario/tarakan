from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import *
import data_base
import keyboard
import price


class CallOrder(StatesGroup):
    sost1 = State()
    sost2 = State()
    sost3 = State()
    sost4 = State()

async def start_order_call(message: types.Message):
    await message.reply("Как к Вам обращаться?\nДля отмены заказа звонка нажмите на кнопку Отмена",
                        reply_markup=keyboard.kb_cancel)
    await CallOrder.sost1.set()

async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    try:
        await message.reply("ОК", reply_markup=keyboard.kb_mainwindow)
    except:
        await bot.send_message(message.from_user.id, "OK", reply_markup=keyboard.kb_mainwindow)

async def get_name(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.reply("Введите контакт, по которому с вами можно связаться\nНомер телефона / телеграм",
                        reply_markup=keyboard.kb_cancel)
    await CallOrder.sost2.set()

async def get_contact(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["contact"] = message.text
    await message.reply("Укажите удобную дату и время, когда с Вами можно связаться", reply_markup=keyboard.kb_cancel)
    await CallOrder.sost3.set()

async def get_time(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["time"] = message.text
    await message.reply("Менеджер свяжется с Вами в указанное время. Спасибо за обращение в СЭС Биозащита!",
                        reply_markup=keyboard.kb_mainwindow)
    await data_base.add_call_to_user(state)
    await state.finish()


class MasterCall(StatesGroup):
    sost1 = State()
    sost2 = State()
    sost3 = State()
    sost4 = State()
    sost5 = State()
    sost6 = State()

async def start_master_call(message: types.Message):
    await message.reply("Kак к Вам обращаться?")
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_cancel)
    await MasterCall.sost1.set()


async def get_name_for_master(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.reply("Введите контакт, по которому с вами можно связаться\nНомер телефона / телеграм")
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_cancel)
    await MasterCall.sost2.set()


async def get_contact_for_master(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["contact"] = message.text
    await message.reply("Укажите удобную дату и время, когда с Вами можно связаться")
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_cancel)
    await MasterCall.sost3.set()


async def get_time_master(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["time"] = message.text
    await message.reply("Какая услуга вас интересует", reply_markup=keyboard.kb_servises)
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_cancel)
    await MasterCall.sost4.set()

async def get_service_info(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["service"] = message.text
        data["type"] = await data_base.get_info_about_user(message)
    await message.reply("Укажите адрес (в одном сообщении)")
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_cancel)
    await MasterCall.sost5.set()


async def get_service_adress(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["adress"] = message.text
    await message.reply("Кратко опишите проблему (в одном сообщении)")
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_cancel)
    await MasterCall.sost6.set()

async def get_discription(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["discription"] = message.text
    await message.reply("Оформление заявки успешно завершено. Спасибо за обращение в СЭС Биозащита!",
                        reply_markup=keyboard.kb_mainwindow)
    await data_base.add_master_call(state)
    await state.finish()


class PriseGetting(StatesGroup):
    sost1 = State()


async def get_cost(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите услугу",
                           reply_markup=keyboard.kb_servises_c1)
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_cancel)
    await PriseGetting.sost1.set()


async def get_serv_for_price(message: types.Message, state=FSMContext):
    if await data_base.get_user_type(message) == "Компания":
        await bot.send_message(message.from_user.id, f"{price.ur_user[message.text]}", reply_markup=keyboard.kb_mainwindow)

    elif await data_base.get_user_type(message) == "Частное лицо":
        await bot.send_message(message.from_user.id, price.ur_user[message.text], reply_markup=keyboard.kb_mainwindow)
    await state.finish()



def registr_client(dp: Dispatcher):
    dp.register_message_handler(start_order_call, lambda message: "Заказать звонок" in message.text, state=None)
    dp.register_message_handler(start_master_call, lambda message: "Вызов мастера" in message.text, state=None)
    dp.register_message_handler(get_cost, lambda message: message.text.lower() == "узнать стоимость", state=None)
    dp.register_message_handler(cancel, state="*", commands=['отмена', 'cancel'])
    dp.register_callback_query_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(get_name, state=CallOrder.sost1)
    dp.register_message_handler(get_serv_for_price, state=PriseGetting.sost1)
    dp.register_message_handler(get_contact, state=CallOrder.sost2)
    dp.register_message_handler(get_time, state=CallOrder.sost3)
    dp.register_message_handler(get_name_for_master, state=MasterCall.sost1)
    dp.register_message_handler(get_contact_for_master, state=MasterCall.sost2)
    dp.register_message_handler(get_time_master, state=MasterCall.sost3)
    dp.register_message_handler(get_service_info, state=MasterCall.sost4)
    dp.register_message_handler(get_service_adress, state=MasterCall.sost5)
    dp.register_message_handler(get_discription, state=MasterCall.sost6)




