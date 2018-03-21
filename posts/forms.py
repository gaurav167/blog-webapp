from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content', 'on_post',)

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('title',)