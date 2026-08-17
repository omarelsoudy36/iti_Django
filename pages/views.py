from django.shortcuts import render
import random

def rps_game(request):
    user_choice = request.GET.get('choice') # بيجيب اختيار المستخدم من الزرار
    comp_choice = None
    result = None

    if user_choice:
        choices = ['Rock', 'Paper', 'Scissors']
        comp_choice = random.choice(choices) # الكمبيوتر بيختار عشوائي

        # مقارنة النتيجة بالذكاء البسيط
        if user_choice == comp_choice:
            result = "It's a Tie! (تعادل)"
        elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
             (user_choice == 'Paper' and comp_choice == 'Rock') or \
             (user_choice == 'Scissors' and comp_choice == 'Paper'):
            result = "You Win! (أنت كسبت 🎉)"
        else:
            result = "You Lose! (الكمبيوتر كسب 🤖)"

    context = {
        'user': user_choice,
        'comp': comp_choice,
        'result': result
    }
    return render(request, 'pages/rps.html', context)


