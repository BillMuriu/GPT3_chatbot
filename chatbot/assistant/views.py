from django.shortcuts import render, redirect
import openai
from .secret_key import API_KEY
openai.api_key = API_KEY
from .models import OpenAIMessage

def home(request):
    try:
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=1000)
            formatted_response = response['choices'][0]['text']
            message = OpenAIMessage(prompt=prompt, response=formatted_response)
            message.save()
            context = {
                'formatted_response': formatted_response,
                'prompt': prompt,
                'openaimessage_set': OpenAIMessage.objects.all()
            }
            return render(request, 'assistant/home.html', context)
        else:
            context = {'openaimessage_set': OpenAIMessage.objects.all()}
            return render(request, 'assistant/home.html', context)
    except:
        return redirect('error_handler')
    
def error_handler(request):
    return render(request, 'assistant/error_handler.html')



