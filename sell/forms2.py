from allauth.socialaccount.forms import SignupForm
from django import forms
from captcha.fields import ReCaptchaField

class MyCustomSocialSignupForm(SignupForm):

  captcha = ReCaptchaField(label='로봇이 아닙니다')
  def save(self, request):

    # Ensure you call the parent class's save.
    # .save() returns a User object.
    user = super(MyCustomSocialSignupForm, self).save(request)
    user.save()
    # Add your own processing here.
    # You must return the original result.
    return user