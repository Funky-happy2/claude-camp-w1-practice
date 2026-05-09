import random

lang_choice = input("Select language / 选择语言:\n1. English\n2. 中文 (Chinese)\nChoose / 选择 (1 or 2): ").strip()
lang = "zh" if lang_choice == "2" else "en"

translations = {
    "en": {
        "welcome": "🔐 Welcome to the Password Generator! 🛡️",
        "enter_length": "📏 Enter the length of the password: ",
        "generated": "🔑 Generated password: {password}",
        "very_weak": "🚨 This password is very weak. Consider using a longer password with a mix of letters, numbers, and special characters.",
        "weak": "⚠️ This password is weak. Consider using a longer password with a mix of letters, numbers, and special characters.",
        "moderate": "🟡 This password is moderate. Consider using a longer password with a mix of letters, numbers, and special characters for better security.",
        "strong": "🟢 This password is strong. Consider using a longer password with a mix of letters, numbers, and special characters for even better security.",
        "very_strong": "🏆 This password is very strong! Great job! 🎉",
        "again": "Do you want to generate another password? (yes/no): ",
        "goodbye": "👋 Goodbye! Stay secure! 🔒",
        "ok_again": "🔄 Ok, let's generate another password!",
        "invalid_again": "🤔 Invalid input. Let's generate another password!",
    },
    "zh": {
        "welcome": "🔐 欢迎使用密码生成器！🛡️",
        "enter_length": "📏 请输入密码长度：",
        "generated": "🔑 生成的密码：{password}",
        "very_weak": "🚨 此密码非常弱，建议使用更长的密码，并混合字母、数字和特殊字符。",
        "weak": "⚠️ 此密码较弱，建议使用更长的密码，并混合字母、数字和特殊字符。",
        "moderate": "🟡 此密码强度一般，建议使用更长的密码以提高安全性。",
        "strong": "🟢 此密码较强，建议使用更长的密码以获得更高安全性。",
        "very_strong": "🏆 此密码非常强！做得好！🎉",
        "again": "您想再生成一个密码吗？(是/否)：",
        "goodbye": "👋 再见！注意安全！🔒",
        "ok_again": "🔄 好的，让我们再生成一个密码！",
        "invalid_again": "🤔 无效输入，让我们再生成一个密码！",
    }
}

t = translations[lang]

while True:
    print(t["welcome"])

    length = input(t["enter_length"])
    length = "".join([char for char in length if char.isdigit()])
    length = int(length.strip())

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    print(t["generated"].format(password=password))

    if length < 8:
        print(t["very_weak"])
    elif 8 <= length < 12:
        print(t["weak"])
    elif 12 <= length < 16:
        print(t["moderate"])
    elif 16 <= length < 20:
        print(t["strong"])
    else:
        print(t["very_strong"])

    again = input(t["again"])
    if again.lower() in ("no", "否"):
        print(t["goodbye"])
        break
    elif again.lower() in ("yes", "是"):
        print(t["ok_again"])
    else:
        print(t["invalid_again"])
