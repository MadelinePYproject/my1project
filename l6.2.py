def conver_seconds(seconds):
    if seconds < 0 or seconds > 8640000:
        return "shos pishlo ne tydu"
    seconds_per_minute = 60
    seconds_per_hour = 3600
    seconds_per_day = 86400
    days, seconds = divmod(seconds, seconds_per_day)
    hour, seconds = divmod(seconds, seconds_per_hour)
    minutes, seconds = divmod(seconds, seconds_per_minute)
    return f"{days} {'День' if days == 1 else 'Дней'},{str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
user_input = int(input("Vvedite kl-vo secund : "))
print(conver_seconds(user_input))
