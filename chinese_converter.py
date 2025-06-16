def converter(texts):

    with open("ZhConversion.php", "r", encoding="utf-8") as f:
        lines = f.readlines()

    conversion_dict = {}
    check = 0
    for line in lines:
        if "$zh2Hans" in line or "$zh2CN" in line:
            check = 1

        if check and "=>" in line:
            parts = line.strip().strip(",").split("=>")
            traditional = parts[0].strip().strip("'\"")
            simplified = parts[1].strip().strip("'\"")
            conversion_dict[traditional] = simplified
        
        if "]" in line:
            check = 0

    simplified = ""
    max_len = max(len(k) for k in conversion_dict)
    text = 0
    while text < len(texts):
        match = 0
        for i in range(max_len, 0, -1):
            traditional = texts[text : text + i]
            if traditional in conversion_dict:
                simplified += conversion_dict[traditional]
                text += i
                match = 1
                break
        if match == 0:
            simplified += texts[text]
            text += 1

    return simplified