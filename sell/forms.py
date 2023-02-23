from django import forms
from sell.models import Writing, Comment, User
from allauth.account.forms import SignupForm
from django.contrib.auth.hashers import check_password
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from captcha.fields import ReCaptchaField
from allauth.account.forms import ResetPasswordForm

class WritingForm(forms.ModelForm):
    captcha = ReCaptchaField(label='로봇이 아닙니다')
    class Meta:
        model = Writing
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        widgets = {
            'content': SummernoteWidget(),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'level', 'reply_id']
        labels = {
            'content': '내용',
        }


class MyCustomSignupForm(SignupForm):

  captcha = ReCaptchaField(label='로봇이 아닙니다')
  def save(self, request):

    # Ensure you call the parent class's save.
    # .save() returns a User object.
    user = super(MyCustomSignupForm, self).save(request)
    user.save()
    # Add your own processing here.
    # You must return the original result.
    return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': '유저이름',
        }


class CheckPasswordForm(forms.Form):
      password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),
                                 )

      def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

      def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
          if not check_password(password, confirm_password):
            self.add_error('password', '비밀번호가 일치하지 않습니다.')

class MyCustomResetPasswordForm(ResetPasswordForm):

    captcha = ReCaptchaField(label='로봇이 아닙니다')
    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super(MyCustomResetPasswordForm, self).save(request)

        # Add your own processing here.
        # Ensure you return the original result
        return email_address