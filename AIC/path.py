# import os
# import json
#
# # RISHI ABSOLUTE PATH
# QUESTION_GENERATION_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\question_generation'
# ONE_QUE_TO_MANY_QUE_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\OneQueToManyQues'
# STATIC__AIC_APP_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP\\static\\AIC_APP'
# TRAINING_FOLDER_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP\\training'
# MAIN_AIC_FOLDER_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC'
# MAIN_AIC_APP_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP'
# MODEL_DATA_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP\\training\\modelData'
#
#
#
# # SIDDHI ABSOLUTE PATH
# # QUESTION_GENERATION_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\question_generation'
# # ONE_QUE_TO_MANY_QUE_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\OneQueToManyQues'
# # STATIC__AIC_APP_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP\\static\\AIC_APP'
# # TRAINING_FOLDER_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP\\training'
# # MAIN_AIC_FOLDER_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC'
# # MAIN_AIC_APP_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP'
#
#
# # HARSHIL ABSOULUTE PATH
# # QUESTION_GENERATION_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\question_generation'
# # ONE_QUE_TO_MANY_QUE_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\OneQueToManyQues'
# # STATIC__AIC_APP_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP\\static\\AIC_APP'
# # TRAINING_FOLDER_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP\\training'
# # MAIN_AIC_FOLDER_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC'
# # MAIN_AIC_APP_PATH = r'C:\\Users\\patel\\PycharmProjects\\AIChatBot\\AIC\\AIC_APP'
#
# def find_file_name(filename, dir):
#     files_in_folder = os.listdir(dir)
#     if filename in files_in_folder:
#         return str(os.path.abspath(os.path.join(dir, filename)))
#
# # HOW TO USE
# pathfinder = find_file_name('runnow.py', QUESTION_GENERATION_PATH)
# print(pathfinder)
# pathfinder = find_file_name('intents.json', MAIN_AIC_FOLDER_PATH)
# print(pathfinder)
# intents = json.loads(open(find_file_name('intents.json', TRAINING_FOLDER_PATH)).read())
# print(intents)
# intents = json.loads(open(find_file_name('intents.json', MAIN_AIC_FOLDER_PATH)).read())
# print(intents)
#
