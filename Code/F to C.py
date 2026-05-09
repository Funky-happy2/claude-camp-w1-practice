lang_choice = input("Select language / 选择语言:\n1. English\n2. 中文 (Chinese)\nChoose / 选择 (1 or 2): ").strip()
lang = "zh" if lang_choice == "2" else "en"

translations = {
    "en": {
        "welcome": "🌡️ Welcome to the Fahrenheit to Celsius converter! 🔄",
        "choose_calc": "Choose your calculation: \n1. 🇺🇸 Fahrenheit to Celsius \n2. 🌍 Celsius to Fahrenheit\n                   \nChoose 1 or 2: ",
        "enter_f": "🌡️ Enter the temperature in Fahrenheit: ",
        "enter_c": "🌡️ Enter the temperature in Celsius: ",
        "f_to_c_result": "🌡️ {f} Fahrenheit is {c:.2f} degrees Celsius to 2 decimal points.",
        "c_to_f_result": "🌡️ {c} degrees Celsius is {f:.2f} Fahrenheit to 2 decimal points.",
        "freezing": "🥶 It's freezing outside! Make sure to bundle up!",
        "cold": "🧥 It's quite cold outside. Don't forget your coat!",
        "chilly": "🍂 It's a bit chilly outside. You might want a light jacket.",
        "warm": "☀️ The weather is nice and warm. Enjoy your day!",
        "hot": "🔥 It's very hot outside! Stay hydrated and cool!",
        "invalid": "❌ Invalid input. Please enter 1 or 2.",
        "again": "Do you want to convert another temperature? (yes/no): ",
        "goodbye": "👋 Goodbye! Stay comfortable! 😊",
        "ok_again": "🔄 Ok, let's convert another temperature!",
        "invalid_again": "🤔 Invalid input. Let's convert another temperature!",
    },
    "zh": {
        "welcome": "🌡️ 欢迎使用温度转换器！🔄",
        "choose_calc": "选择您的计算方式：\n1. 🇺🇸 华氏度转摄氏度\n2. 🌍 摄氏度转华氏度\n\n请选择 1 或 2：",
        "enter_f": "🌡️ 请输入华氏度温度：",
        "enter_c": "🌡️ 请输入摄氏度温度：",
        "f_to_c_result": "🌡️ {f} 华氏度等于 {c:.2f} 摄氏度（保留两位小数）。",
        "c_to_f_result": "🌡️ {c} 摄氏度等于 {f:.2f} 华氏度（保留两位小数）。",
        "freezing": "🥶 外面非常寒冷！记得多穿衣服！",
        "cold": "🧥 外面很冷，别忘了穿外套！",
        "chilly": "🍂 外面有点凉，你可能需要一件薄外套。",
        "warm": "☀️ 天气温暖宜人，祝您愉快！",
        "hot": "🔥 外面非常热！请注意补水保凉！",
        "invalid": "❌ 无效输入，请输入 1 或 2。",
        "again": "您想再转换一次温度吗？(是/否)：",
        "goodbye": "👋 再见！注意保暖！😊",
        "ok_again": "🔄 好的，让我们再转换一次！",
        "invalid_again": "🤔 无效输入，让我们再转换一次！",
    }
}

t = translations[lang]

while True:
    print(t["welcome"])

    f_or_c = input(t["choose_calc"])
    f_or_c = "".join([char for char in f_or_c if char.isdigit()])
    f_or_c = f_or_c.strip()
    f_or_c = eval(f_or_c)

    if f_or_c == 1:
        f = input(t["enter_f"])
        f = "".join([char for char in f if char.isdigit() or char == "."])
        f = f.strip()
        f = float(f)
        c = (f - 32) * 5 / 9
        print(t["f_to_c_result"].format(f=f, c=c))

        if c < 0:
            print(t["freezing"])
        elif 0 <= c < 10:
            print(t["cold"])
        elif 10 <= c < 20:
            print(t["chilly"])
        elif 20 <= c < 30:
            print(t["warm"])
        else:
            print(t["hot"])
    elif f_or_c == 2:
        c = input(t["enter_c"])
        c = "".join([char for char in c if char.isdigit() or char == "."])
        c = c.strip()
        c = float(c)
        f = (c * 9 / 5) + 32
        print(t["c_to_f_result"].format(c=c, f=f))

        if f < 32:
            print(t["freezing"])
        elif 32 <= f < 50:
            print(t["cold"])
        elif 50 <= f < 68:
            print(t["chilly"])
        elif 68 <= f < 86:
            print(t["warm"])
        else:
            print(t["hot"])
    else:
        print(t["invalid"])
        continue

    again = input(t["again"])
    if again.lower() in ("no", "否"):
        print(t["goodbye"])
        break
    elif again.lower() in ("yes", "是"):
        print(t["ok_again"])
    else:
        print(t["invalid_again"])
