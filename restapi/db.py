import json

class ExeptionOpenDB(Exception):
    pass

class NicksDB():
    __instance = None
    __is_exist = False
    __filepath = "db.json"

    def __new__(cls, file=__filepath):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__filepath = file
        return cls.__instance
    
    def __init__(self):
        if not self.__is_exist:
            self.__nick_list = []
            self.load()
            self.__is_exist = True

    def __str__(self):
        return " ".join(self.__nick_list)

    def add(self, nick):
        if nick and isinstance(nick, str):
            if nick in self.__nick_list:
                return False
            else:
                self.__nick_list.append(nick)
                return True

    def delete(self, nick):
        if nick in self.__nick_list:
            self.__nick_list.remove(nick)
            return True
        return False

    def load(self):
        try:
            with open(self.__filepath, "r", encoding="utf-8") as f_db:
                self.__nick_list = json.load(f_db)
                return (True, "OK")
        except FileNotFoundError:
            return {"result": True, 
                    "message": "Warning!! файла нет, список оставлен пустым"}
        except json.JSONDecodeError:
            return {"result": False,
                    "message": "Error!!! Файл не содержит структуру данных!"}
            # raise ExeptionOpenDB(f"Проверте указанный файл {self.__filepath}")
    
    def save(self):
        try:
            with open("db.json", "w", encoding="utf-8") as f_db:
                json.dump(self.__nick_list, f_db, indent=4)
            return {"result": True,
                "message": "База успешно сохранена"}
        except Exception as e:
            return {"result": False,
                    "message": str(e)}

    def check(self, nick):
        return nick in self.__nick_list


if __name__ == "__main__":
    nicks = NicksDB()
    nicks2 = NicksDB()
    print(nicks is nicks2)
    print(nicks.add("mineev"))
    print(nicks.add("KacPsi"))
    print(nicks.add("Hicatia"))
    print(nicks)
    print(nicks.delete("Федя"))
    print(nicks)
    print(nicks.save())
