from django.contrib import admin
from .models import FeedBack

class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'army_number', 'unitName', 'course', 'get_question1', 'get_question2', 'get_question3', 'get_question4','get_question5','get_question6', 'get_question7','get_question8', 'feedback')
    list_filter = ('army_number', 'name', 'rank','course', 'unitName', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8')  # Add any other fields you want to filter by
    
    def get_question1(self, obj):
        return "ADM side se apko kis mai improvement chaiye? " + obj.question1
    get_question1.short_description = 'Question 1'
    
    def get_question2(self, obj):
        return "Course mai Instr dwara apko sikhaya/ padaya gaya uske madhya nazar rakhte hue ap instr ko ky rating dena chahenge? " + obj.question2
    get_question2.short_description = 'Question 2'

    def get_question3(self, obj):
        return "Apke hisab se course ka Time Duration? " + obj.question3
    get_question3.short_description = 'Question 3'

    def get_question4(self, obj):
        return "Kya Course mai Tech Eqpt ki aur jarurt hai? " + obj.question4
    get_question4.short_description = 'Question 4'

    def get_question5(self, obj):
        return "Course syllabus se ap kitne santust hai? " + obj.question5
    get_question5.short_description = 'Question 5'

    def get_question6(self, obj):
        return "Apne Overall Experience ko ap kitni rating dena chahge? " + obj.question6
    get_question6.short_description = 'Question 6'

    def get_question7(self, obj):
        return " Kya apke hisab se course mai extra classes honi chaiye " + obj.question7
    get_question7.short_description = 'Question 7'

    def get_question8(self, obj):
        return " Kya Course mai apko apni practise / study karne ka sufficient time mila " + obj.question8
    get_question8.short_description = 'Question 8'

admin.site.register(FeedBack, FeedBackAdmin)
