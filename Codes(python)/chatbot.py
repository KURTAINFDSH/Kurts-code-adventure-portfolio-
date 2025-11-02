import google.generativeai as ai

#API
API_KEY = 'AIzaSyCiNoEFVzcgCN1sEUsexAK_TIkc_lIMiF8'


#building the model

model = ai.generativemodel('blaze')
chat = model.start_chat()


#starting a conversition

while True:
  messege = input('you: ')
  if chat.lower() == 'bye':
    print('chatbot: goodye')
    break
  response = chat.send_messege('messege')
  print('chatbot:', response.text )print ('hello')
