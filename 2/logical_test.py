"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def main():
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("Invalid input")
        return

    if number < 0 or number >= 10_000_000:
        print("Value out of range")
        return
    
    thai_dict = {
        "0": "ศูนย์",
        "1": "หนึ่ง",
        "2": "สอง",
        "3": "สาม",
        "4": "สี่",
        "5": "ห้า",
        "6": "หก",
        "7": "เจ็ด",
        "8": "แปด",
        "9": "เก้า",
    }

    thai_list = [
        (1_000_000, "ล้าน"),
        (100_000, "แสน"),
        (10_000, "หมื่น"),
        (1_000, "พัน"),
        (100, "ร้อย"),
        (10, "สิบ"),
        (1, ""),
    ]

    result = ""
    for value, symbol in thai_list:
        if number >= value:
            result += thai_dict[str(int(number // value))] + symbol
            number %= value

    special_case = {
        "หนึ่งสิบ": "สิบ",
        "สองสิบ": "ยี่สิบ",
        "สิบหนึ่ง": "สิบเอ็ด",
        "ร้อยหนึ่ง": "ร้อยเอ็ด",
    }
    for special in special_case:
        if special in result:
            result = result.replace(special, special_case[special])

    print(result)


if __name__ == "__main__":
    main()
