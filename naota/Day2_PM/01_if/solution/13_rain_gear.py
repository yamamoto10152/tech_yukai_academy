is_raining = True
humidity = 85
temperature = 32

if is_raining or humidity >= 80:
    print("傘を持っていきましょう")

if temperature >= 30:
    print("水分補給を忘れずに")

if temperature < 10:
    print("上着を持っていきましょう")

if not is_raining and humidity < 80 and 10 <= temperature < 30:
    print("快適な一日を！")
