import json
import logging
import pprint
import time

account = ""
password = ""
over = False
wtime = -1
user_infomation = {
                    "name" : "",
                    "password" : "",
                    "level" : ""
                    }



while not(over) :
    wtime += 1  # 錯的次數加 1 #
    # 輸出錯誤 #
    if wtime >= 1 :
        print("wrong")
    #   ...  #

    # 錯3次，停20秒 #
    if wtime >= 3 :
        print("還有 20 秒 ...")
        for i in range(19,0,-1) :
            time.sleep(1)
            print(i,"...")
    #     ...     #

    # 輸入帳號、密碼 #
    account  = input("input account  >>>")
    password = input("input password >>>")
    #     ...     #

    try :
        with open(r'system\member.json','r') as key :
            key_dict = json.load(key)
            get_in = key_dict["getin"]
            for i,i2 in get_in:
                print(get_in)
                while not(over) :
                    if account == i :
                        if password == key[i] :
                            print("wellcome",i,"!")
                            user_infomation["name"] = i
                            user_infomation["password"] = key[i]
                            pprint.PrettyPrinter(user_infomation)
                            over = True

    except Exception as err:
        logging.error("error",err)