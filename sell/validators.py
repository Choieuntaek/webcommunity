import string
from django.core.exceptions import ValidationError

class CustomPasswordValidator():

  def __init__(self, min_length=1):
    self.min_length = min_length

  def validate(self, password, user=None):
    special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
    if not any(char.isdigit() for char in password):
      raise ValidationError(
        ('비밀번호는 최소한 %(min_length)d 자리의 숫자가 포함되어야 합니다.') % {'min_length': self.min_length})
    if not any(char.isalpha() for char in password):
      raise ValidationError(
        ('비밀번호는 최소한 %(min_length)d 자리의 문자가 포함되어야 합니다.') % {'min_length': self.min_length})
    if not any(char in special_characters for char in password):
      raise ValidationError(
        ('비밀번호는 최소한 %(min_length)d 자리의 특수문자가 포함되어야 합니다.') % {'min_length': self.min_length})

  def get_help_text(self):
    return ""