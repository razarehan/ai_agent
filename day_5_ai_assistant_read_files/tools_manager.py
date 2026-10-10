from tools import generate_password, get_curr_dateTime, roll_dice, read_file

def manage_tools(input_text):
    input_text = input_text.lower()
    if "date" in input_text or "time" in input_text or "clock" in input_text:
        return get_curr_dateTime()
    elif "roll" in input_text and "dice" in input_text:
        return roll_dice()
    elif "password" in input_text or "passcode" in input_text:
        return generate_password()
    elif input_text.startswith("summarize"):
        file_path = input_text.replace("summarize", "").strip()
        return read_file("data/" + file_path)
    else:
        return None