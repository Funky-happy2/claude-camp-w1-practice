import random

lang_choice = input("Select language / 选择语言:\n1. English\n2. 中文 (Chinese)\nChoose / 选择 (1 or 2): ").strip()
lang = "zh" if lang_choice == "2" else "en"

translations = {
    "en": {
        "welcome": "🎉 Welcome to the Greeting Generator! 🎉",
        "enter_name": "Enter your name: ",
        "enter_age": "Enter your age: ",
        "generating": "✨ Generating your greeting... ✨",
        "greeting_type": "Greeting style: {style}",
        "greetings": [
            ("🎩 Formal",        "🎩 Good day, {name}. You are {age} years of age, which places your birth in {birth_year}. A pleasure to make your acquaintance."),
            ("👋 Casual",        "👋 Hey {name}! Nice to meet you! You're {age} years old — that's pretty cool! 😄"),
            ("🥳 Enthusiastic",  "🥳 HELLO {name}!!! I CAN'T BELIEVE YOU'RE {age} YEARS OLD! THAT'S AMAZING!!! 🎊🎉"),
            ("🌟 Poetic",        "🌟 Ah, {name}! Like a star born in {birth_year}, you shine brighter at every age. Here's to {age} wonderful years! 🌸"),
            ("🔮 Mysterious",    "🔮 The oracle speaks... {name}... born in {birth_year}... now {age} years walk this earth... fascinating. 🌙"),
            ("☠️ Pirate",        "☠️ Ahoy, {name}! Ye be {age} years old, sailed since {birth_year}! A fine sea dog ye are! ⚓🦜"),
        ],
        "again": "Do you want to generate another greeting? (yes/no): ",
        "goodbye": "👋 Goodbye! Have a great day! 😊",
        "ok_again": "🔄 Ok, let's generate another greeting!",
        "invalid_again": "🤔 Invalid input. Let's generate another greeting!",
    },
    "zh": {
        "welcome": "🎉 欢迎使用问候语生成器！🎉",
        "enter_name": "请输入您的姓名：",
        "enter_age": "请输入您的年龄：",
        "generating": "✨ 正在生成您的问候语... ✨",
        "greeting_type": "问候语风格：{style}",
        "greetings": [
            ("🎩 正式",   "🎩 您好，{name}，您今年 {age} 岁，也就是说您出生于 {birth_year} 年。幸会。"),
            ("👋 随意",   "👋 嗨，{name}！很高兴认识你！你今年 {age} 岁，真酷！😄"),
            ("🥳 热情",   "🥳 你好呀，{name}！！！你居然已经 {age} 岁了！太厉害了！！！🎊🎉"),
            ("🌟 诗意",   "🌟 啊，{name}！如同 {birth_year} 年诞生的星辰，你在 {age} 岁依然闪耀！🌸"),
            ("🔮 神秘",   "🔮 神谕降临……{name}……诞生于 {birth_year} 年……如今已走过 {age} 个春秋……奇妙。🌙"),
            ("☠️ 海盗",   "☠️ 哟吼，{name}！你已经 {age} 岁啦，自 {birth_year} 年扬帆至今！真是条好汉！⚓🦜"),
        ],
        "again": "您想再生成一个问候语吗？(是/否)：",
        "goodbye": "👋 再见！祝您有美好的一天！😊",
        "ok_again": "🔄 好的，让我们再生成一个！",
        "invalid_again": "🤔 无效输入，让我们再生成一个！",
    }
}

t = translations[lang]

while True:
    print(t["welcome"])

    name = input(t["enter_name"]).strip()
    age_raw = input(t["enter_age"])
    age_raw = "".join([char for char in age_raw if char.isdigit() or char == "."])
    age = float(age_raw.strip())
    birth_year = int(2026 - age)

    style, text = random.choice(t["greetings"])

    print(t["generating"])
    print(t["greeting_type"].format(style=style))
    print(text.format(name=name, age=int(age), birth_year=birth_year))

    again = input(t["again"])
    if again.lower() in ("no", "否"):
        print(t["goodbye"])
        break
    elif again.lower() in ("yes", "是"):
        print(t["ok_again"])
    else:
        print(t["invalid_again"])
