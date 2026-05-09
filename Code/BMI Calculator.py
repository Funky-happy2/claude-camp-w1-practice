lang_choice = input("Select language / 选择语言:\n1. English\n2. 中文 (Chinese)\nChoose / 选择 (1 or 2): ").strip()
lang = "zh" if lang_choice == "2" else "en"

translations = {
    "en": {
        "welcome": "⚖️ Welcome to the BMI Calculator! 💪",
        "enter_height": "📏 Enter your height in cm: ",
        "enter_weight": "🏋️ Enter your weight in kg: ",
        "bmi_result": "📊 Your BMI is: {bmi:.2f}",
        "underweight": "🥗 You are underweight. You should consider gaining some weight for better health.",
        "normal": "✅ You have a normal weight. You are in good shape! Keep it up! 🌟",
        "overweight": "⚠️ You are overweight. You should consider losing some weight for better health.",
        "obese": "🚨 You are obese. You should consider losing a significant amount of weight for better health.",
        "again": "Do you want to calculate again? (yes/no): ",
        "goodbye": "👋 Goodbye! Stay healthy! 💚",
        "ok_again": "🔄 Ok, let's calculate again!",
        "invalid_again": "🤔 Invalid input. Let's calculate again!",
    },
    "zh": {
        "welcome": "⚖️ 欢迎使用 BMI 计算器！💪",
        "enter_height": "📏 请输入您的身高（厘米）：",
        "enter_weight": "🏋️ 请输入您的体重（千克）：",
        "bmi_result": "📊 您的 BMI 是：{bmi:.2f}",
        "underweight": "🥗 您的体重偏低，建议适当增重以改善健康状况。",
        "normal": "✅ 您的体重正常，状态良好！继续保持！🌟",
        "overweight": "⚠️ 您的体重偏高，建议适当减重以改善健康状况。",
        "obese": "🚨 您属于肥胖，建议大幅减重以改善健康状况。",
        "again": "您想再计算一次吗？(是/否)：",
        "goodbye": "👋 再见！保持健康！💚",
        "ok_again": "🔄 好的，让我们再计算一次！",
        "invalid_again": "🤔 无效输入，让我们再计算一次！",
    }
}

t = translations[lang]

while True:
    print(t["welcome"])

    height = input(t["enter_height"])
    weight = input(t["enter_weight"])

    hnum = "".join([char for char in height if char.isdigit() or char == "."])
    wnum = "".join([char for char in weight if char.isdigit() or char == "."])
    newh = float(hnum.strip())
    neww = float(wnum.strip())

    bmi = neww / ((newh / 100) ** 2)
    print(t["bmi_result"].format(bmi=bmi))

    if bmi < 18.5:
        print(t["underweight"])
    elif 18.5 <= bmi < 25:
        print(t["normal"])
    elif 25 <= bmi < 30:
        print(t["overweight"])
    else:
        print(t["obese"])

    again = input(t["again"])
    if again.lower() in ("no", "否"):
        print(t["goodbye"])
        break
    elif again.lower() in ("yes", "是"):
        print(t["ok_again"])
    else:
        print(t["invalid_again"])
