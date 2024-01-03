def emoji_converter(message1):
    words = message1.split(" ")  # 將每個單字區分開來
    print(words)
    emojis = {
        ":)": "😀",
        ":(": "🥲"
    }
    # 在Python中，字典{}是一種鍵值對(key-value pairs)的資料結構，其中每個鍵(key)都對應著一個值(value)。

    output = ""
    for word in words:
        print(emojis)
        output += emojis.get(word, word) + " " # get(a, b):第一個是查找對象，第二個是若找不到則返回的值，若有找到則返回對應的Value，
    return output # 最後印出的結果


message = input(">")
print(emoji_converter(message))
