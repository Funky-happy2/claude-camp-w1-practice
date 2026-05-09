lang_choice = input("Select language / 选择语言:\n1. English\n2. 中文 (Chinese)\nChoose / 选择 (1 or 2): ").strip()
lang = "zh" if lang_choice == "2" else "en"

translations = {
    "en": {
        "welcome": "🍽️ Welcome to the Tip Calculator! 💰",
        "enter_meal": "🧾 Enter the meal cost: ",
        "enter_tip": "💸 Enter the tip percentage: ",
        "tip_amount": "🤝 Tip amount: ${tip:.2f}",
        "total_cost": "💳 Total cost: ${total:.2f}",
        "cheap": "😊 This meal is relatively cheap. Enjoy your meal! 🎉",
        "moderate": "💡 This meal is moderately expensive. Consider sharing the meal or ordering a smaller portion to save money.",
        "expensive": "😬 This meal is quite expensive. Consider sharing the meal, ordering a smaller portion, or looking for cheaper options to save money.",
        "again": "Do you want to calculate another tip? (yes/no): ",
        "goodbye": "👋 Goodbye! Enjoy your meal! 🍴",
        "ok_again": "🔄 Ok, let's calculate another tip!",
        "invalid_again": "🤔 Invalid input. Let's calculate another tip!",
    },
    "zh": {
        "welcome": "🍽️ 欢迎使用小费计算器！💰",
        "enter_meal": "🧾 请输入餐费金额：",
        "enter_tip": "💸 请输入小费百分比：",
        "tip_amount": "🤝 小费金额：${tip:.2f}",
        "total_cost": "💳 总费用：${total:.2f}",
        "cheap": "😊 这顿饭比较便宜，享用美食吧！🎉",
        "moderate": "💡 这顿饭价格适中，可以考虑与他人分享或点小份以节省费用。",
        "expensive": "😬 这顿饭相当贵，可以考虑与他人分享、点小份或寻找更便宜的选择。",
        "again": "您想再计算一次小费吗？(是/否)：",
        "goodbye": "👋 再见！祝您用餐愉快！🍴",
        "ok_again": "🔄 好的，让我们再计算一次！",
        "invalid_again": "🤔 无效输入，让我们再计算一次！",
    }
}

t = translations[lang]

while True:
    print(t["welcome"])

    meal_cost = input(t["enter_meal"])
    tip_percentage = input(t["enter_tip"])

    meal_cost = "".join([char for char in meal_cost if char.isdigit() or char == "."])
    meal_cost = eval(meal_cost.strip())

    tip_percentage = "".join([char for char in tip_percentage if char.isdigit() or char == "."])
    tip_percentage = eval(tip_percentage.strip())

    tip_amount = meal_cost * (tip_percentage / 100)
    total_cost = meal_cost + tip_amount
    print(t["tip_amount"].format(tip=tip_amount))
    print(t["total_cost"].format(total=total_cost))

    if total_cost < 20:
        print(t["cheap"])
    elif 20 <= total_cost < 50:
        print(t["moderate"])
    else:
        print(t["expensive"])

    again = input(t["again"])
    if again.lower() in ("no", "否"):
        print(t["goodbye"])
        break
    elif again.lower() in ("yes", "是"):
        print(t["ok_again"])
    else:
        print(t["invalid_again"])
