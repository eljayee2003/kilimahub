from django import forms

AFRICAN_BLOCKLIST = [
    'boko haram', 'al-shabaab', 'terrorism',
    'ethnic violence', 'tribal war'
]

def check_african_content(text):
    text_lower = text.lower()
    if any(bad_word in text_lower for bad_word in AFRICAN_BLOCKLIST):
        raise forms.ValidationError("Content violates African unity policies")

    negative_words = ['hate', 'kill', 'attack']
    if sum(word in text_lower for word in negative_words) > 2:
        raise forms.ValidationError("Content appears harmful to African unity")
