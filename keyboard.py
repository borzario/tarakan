from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import list_of_admins

ib_main = InlineKeyboardButton(text="В начало", callback_data="в начало")
ikb_main = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).row(ib_main)

ib_cancel = InlineKeyboardButton(text="Отмена", callback_data="отмена")
ikb_cancel = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).row(ib_cancel)

b_human = KeyboardButton("Частное лицо")
b_company = KeyboardButton("Компания")
kb_firstwindow = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_firstwindow.add(b_human, b_company)

b_works = KeyboardButton("Услуги компании")
b_adress = KeyboardButton("Адрес компании")
b_call = KeyboardButton("Связаться со специалистом компании")
b_info = KeyboardButton("Справочник")
b_gis = KeyboardButton("Оставить отзыв в 2Гис")
kb_mainwindow = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_mainwindow.row(b_works).row(b_adress).row(b_call).row(b_gis)

b_call_to = KeyboardButton("Заказать звонок")
b_get_contacs = KeyboardButton("Связаться самому")
kb_call = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_call.add(b_call_to, b_get_contacs)

b_user = KeyboardButton("User")
b_admin = KeyboardButton("Admin")
kb_admin_first = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_admin_first.add(b_admin, b_user)

b_cancel = KeyboardButton("Отмена")
b_dezenfection = KeyboardButton("Дезинфекция")
b_dezinsection = KeyboardButton("Дезинсекция")
b_deratization = KeyboardButton("Дератизация")
b_dezodaration = KeyboardButton("Дезодорация")
b_akaric = KeyboardButton("Акарицидная обработка")
kb_servises = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_servises.add(b_dezinsection, b_dezenfection).add(b_deratization, b_dezodaration)
kb_servises_c = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_servises_c.add(b_dezinsection, b_dezenfection).add(b_deratization, b_dezodaration).add(b_akaric).add(b_cancel)
kb_servises_c1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_servises_c1.add(b_dezinsection, b_dezenfection).add(b_deratization, b_dezodaration).add(b_akaric)

b_coast = KeyboardButton("Узнать стоимость")
b_master = KeyboardButton("Вызов мастера")
kb_works = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_works.add(b_coast, b_master)

"""Here is admins buttons and keyboards"""
b_get_all_calls = KeyboardButton("Get all calls")
b_get_new_calls = KeyboardButton("Get new calls")
b_close_call = KeyboardButton("Close call")
b_get_all_oders = KeyboardButton("Get all orders")
b_get_new_oders = KeyboardButton("Get new orders")
b_close_oder = KeyboardButton("Close order")
b_give_order = KeyboardButton("Give to")
kb_admin_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin_main.add(b_get_new_calls, b_get_all_calls, b_close_call)
kb_admin_main.row(b_get_new_oders, b_get_all_oders, b_close_oder)
kb_admin_main.row(b_give_order)

b_cancel = KeyboardButton("Отмена")
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b_cancel)

b_accept = KeyboardButton("Accept")
b_dislike = KeyboardButton("Dislike")
kb_accepting = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b_accept, b_dislike)

bs_workers = [[KeyboardButton(text=f"{list(list_of_admins.workers.keys())[i]}")] for i in range(len(list_of_admins.workers))]
kbs_workers = ReplyKeyboardMarkup(keyboard=bs_workers, resize_keyboard=True)

