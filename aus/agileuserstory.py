from gtts import gTTS
import os

file = open("dream.txt", "r").read().replace("\n"," ") 

language = 'ja'

speech = gTTS(text = str(file), lang = language , slow = False)

speech.save("MLKDreamSpeech.mp3")

os.system("MLKDreamSpeech.mp3")

class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_name: str) -> dict:
        pass

class PdfParser(InformalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_path: str) -> dict:
        pass

class EmlParser(InformalParserInterface):

    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        pass
