class Language:
    def speak(self):
        print("Default speaking in English")


class Korean:
    def speak_korean(self):
        print("Speaking in Korean - ")


class British:
    def speak_british(self):
        print("Speaking in English - ")


class LanguageAdapter:
    def __init__(self, obj, **adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


languages = []
korean = Korean()
languages.append(LanguageAdapter(korean, speak=korean.speak_korean))
british = British()
languages.append(LanguageAdapter(british, speak=british.speak_british))

for (index, lang) in enumerate(languages):
    print(index)
    lang.speak()
