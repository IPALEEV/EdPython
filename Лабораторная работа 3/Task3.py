def count_letters(text):
    text = text.lower()
    letters_counter = {}

    for ch in text:
        if ch.isalpha():
            letters_counter.setdefault(ch, 0)
            letters_counter[ch] += 1

    return letters_counter


def calculate_frequency(letters_dict, letters_count):
    frequency = {}

    for letter, amount in letters_dict.items():
        frequency[letter] = amount / letters_count

    return frequency


def letters_amount(text):
    count = 0
    for letter in text:
        if letter.isalpha():
            count += 1
    return count


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

a = count_letters(main_str)
b = calculate_frequency(a, letters_amount(main_str))
for letter, frequency in b.items():
    print(f"{letter}: {frequency:.2f}")
