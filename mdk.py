meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SUS": "Şüpheli bir durumda kullanılır",
            "TROLL": "Şaka knk"
                }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in  meme_dict.keys():
    print("Aradığınız Kelimenin Anlamı", meme_dict[word])
else:
    print("O bende Yok Aga")
