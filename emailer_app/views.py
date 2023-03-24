from django.shortcuts import render
from django.core.mail import send_mail


def emailer_view(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }

        message = '''
        New Message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', [
                  'tommyemailtester69@gmail.com'])

    return render(request, 'index.html', {})
