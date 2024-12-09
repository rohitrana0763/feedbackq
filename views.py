from django.shortcuts import render, HttpResponse
from .models import FeedBack

def index(request):
    return render(request, 'index.html')




def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        feedback_text = request.POST.get("feedback")  # Renamed to avoid confusion with model
        rank = request.POST.get("rank")
        army_number = request.POST.get("army_number")
        course=request.POST.get("course")
        unit_name = request.POST.get("unitName")  # Handle unitName
        question1 = request.POST.get("question1")  # Use distinct names for each question
        question2 = request.POST.get("question2")
        question3 = request.POST.get("question3")
        question4 = request.POST.get("question4")
        question5 = request.POST.get("question5")
        question6 = request.POST.get("question6")
        question7 = request.POST.get("question7")
        # Validate required fields (optional but recommended)
        if not all([name, feedback_text, rank, army_number, unit_name,course, question1, question2, question3, question4, question5, question6, question7]):
            return HttpResponse("<h3>Please fill out all fields.</h3>")

        # Create and save the FeedBack object
        obj = FeedBack(
            name=name,
            feedback=feedback_text,
            rank=rank,
            army_number=army_number,
            course=course,
            unitName=unit_name,  # Correct field name used
            question1=question1,
            question2=question2,
            question3=question3,
            question4=question4,
            question5=question5,
            question6=question6,
            question7=question7,
        )
        obj.save()
        # return HttpResponse("<h>Your Feedback Has Been Submitted</h>")
        # return render(request, 'thankyou.html')
    return render(request, 'feedback.html')

def thank_you(request):
    return render(request, 'thankyou.html')

    
