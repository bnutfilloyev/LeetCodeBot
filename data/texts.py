class Text:
    def __init__(self):
        self.source = '<b>Oldindan minnatdorchiligimni bildiraman, meni yaxshilash fikriga kelganingiz uchun. </b>\n\n' \
                      'Ushbu havola orqali mening kodlarimni topishingiz mumkin:'

        self.start_message = "<b>Assalomu Alaykum, hurmatli {}.</b>\n\n" \
                     "Men LeetCode discuss guruhi uchun yaratilgan maxsus botman. " \
                     "Men sizning natijalaringizni ko'rsatib turishim, " \
                     "reytingizni hisoblash va " \
                     "kunlik savollarni sizga eslatish uchun xizmat qilaman. \n\n" \
                     "Meni yaxshilashimga o'z hissangizni qo'shish uchun " \
                     "/source buyrug'idan foydalanishingiz mumkin." \


class Keyboard:
    def __init__(self):
        self.source = "Havola"
        self.source_url = "https://github.com/YoshlikMedia/LeetCodeBot"


text = Text()
keyboard = Keyboard()
