from django.shortcuts import render, get_object_or_404
from .models import Test, Question, Result
from django.contrib.auth.decorators import login_required



# ✅ Homepage View (DO NOT REMOVE)
def home(request):
    tests = Test.objects.all()
    return render(request, "home.html", {"tests": tests})


# ✅ Test Detail + Submit + Score View
@login_required
def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test)

    # When user submits the test
    if request.method == "POST":
        score = 0

        for q in questions:
            selected = request.POST.get(str(q.id))

            if selected == q.correct_option:
                score += 1

        # Save result in database
        Result.objects.create(
            user=request.user,
            test=test,
            score=score
        )

        return render(request, "result.html", {
            "test": test,
            "score": score,
            "total": questions.count()
        })

    return render(request, "test_detail.html", {
        "test": test,
        "questions": questions
    })
@login_required
def my_results(request):
    results = Result.objects.filter(user=request.user)

    return render(request, "my_results.html", {
        "results": results
    })

