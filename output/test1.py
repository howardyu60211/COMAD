import json


class translation_work:
    def __init__(
        self,
        outword="",
        readpath=r"system\lock_member.json",
        writepath=r"system\lock_member.json",
    ):
        print("initialization...")
        self.readpath = readpath
        self.writepath = writepath
        self.inaccount = ""
        self.inpassword = ""
        self.outword = outword
        self.readans = ""
        self.change_to_unknow = {
            "a": "!",
            "b": "]",
            "c": ")",
            "d": "@",
            "e": "[",
            "f": "-",
            "g": "#",
            "h": "7",
            "i": "2",
            "j": "*",
            "k": ";",
            "l": "~",
            "m": "&",
            "n": "6",
            "o": "`",
            "p": "$",
            "q": "|",
            "r": "%",
            "s": ":",
            "t": "-",
            "u": "{",
            "v": "'",
            "w": "^",
            "x": "(",
            "y": "?",
            "z": "}",
            "_": "_",
            ".": ".",
            "0": "<",
            "1": "9",
            "2": "+",
            "3": "/",
            "4": "=",
            "5": ">",
            "6": "0",
            "7": "8",
            "8": "3",
            "9": "1",
        }
        self.change_to_english = {
            "!": "a",
            "]": "b",
            ")": "c",
            "@": "d",
            "[": "e",
            "-": "f",
            "#": "g",
            "7": "h",
            "2": "i",
            "*": "j",
            ";": "k",
            "~": "l",
            "&": "m",
            "6": "n",
            "`": "o",
            "$": "p",
            "|": "q",
            "%": "r",
            "=": "s",
            "-": "t",
            "{": "u",
            "'": "v",
            "^": "w",
            "(": "x",
            "?": "y",
            "}": "z",
            "_": "_",
            ".": ".",
            "<": "0",
            "9": "1",
            "2": "2",
            "/": "3",
            "=": "4",
            ">": "5",
            "0": "6",
            "8": "7",
            "3": "8",
            "1": "9",
        }
        self.method = str("")
        while self.method != "r" and self.method != "w":
            self.method = input("r or w (read or write) :")
            if self.method != "r" and self.method != "w":
                print("must be r or w")
                continue

    def _do(self):
        if self.method == "w":
            if self.writepath != "":
                try:
                    with open(self.writepath, self.method) as file:
                        for word in self.outword:
                            file.write(self.change_to_unknow[word])
                except Exception as word:
                    print(word)

        if self.method == "r":
            if self.readpath != "":
                # try:
                with open(self.readpath, self.method) as file:
                    word = json.loads(file.read())
                    for word in sorted(word.keys()):
                        print(word)
                        for i in range(len(word)):
                            new_list = word[i:i + 1]
                        for k in new_list:
                            self.inaccount = self.change_to_english[k]
                            print(self.inaccount, end="")
                            print(word[k])
                            self.inpassword = self.change_to_english[word[k]]
                            print(self.inpassword)
                # except Exception as word:
                # print(word)


### 測試 1 ###

helloword = translation_work()
helloword._do()
del helloword
