# exit()
# import speech_recognition as sr
# #robot_ear = sr.Recognizer()
# # import pyttsx3

# # def text_to_speech(text:str):
# #     engine = pyttsx3.init()
# #     engine.say(text)
# #     engine.runAndWait()
# # text_to_speech("freefire never die")
# def speech_to_text()->str:
#     try:
#         with sr.Microphone()as mic:
#             print("ROBOT: I'm listening")

#             audio = robot_ear.listen(mic,timeout=2,phrase_tine_limit=2)

#             audio = robot_ear.recognize_google(audio)
#             text = text.lower()
#             # text_to_speech("I will search for music using the keyword:"+ text)
#             print(text)
#             return text
#     except sr.UnknownValueError:
#         # text_to_speech("I couldn't understand. Could you please repeat that?")
#         return ""
# speech_to_text()