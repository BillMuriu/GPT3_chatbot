from django.shortcuts import render, redirect
import openai
from .secret_key import API_KEY
openai.api_key = API_KEY
from .models import OpenAIMessage

import json
from django.http import JsonResponse

def home(request):
    try:
        if request.method == 'POST':
            prompt = request.POST['prompt']
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=1000)
            formatted_response = response['choices'][0]['text']
            message = OpenAIMessage(prompt=prompt, response=formatted_response)
            message.save()
            data = {
              'formatted_response': formatted_response,
              'prompt': prompt,
              'openaimessage_set': OpenAIMessage.objects.all().values_list('prompt', 'response')
            }
            return JsonResponse(data) # return the data as JSON
        else:
            context = {'openaimessage_set': OpenAIMessage.objects.all()}
            return render(request, 'assistant/home.html', context)
    except:
        return redirect('error_handler')

    
def error_handler(request):
    return render(request, 'assistant/404.html')



