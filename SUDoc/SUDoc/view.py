from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.mail import send_mail
from Utils import tokenGen, emailSend
from Files.models import File
import re
import json


def welcomePage(request):
    errors = []
    logout(request)
    if 'userID' in request.POST:
        userID = None
        password = None

        if request.method == 'POST':
            if not request.POST.get('userID'):
                errors.append('请输入学号')
            else:
                username = request.POST.get('userID')
            if not request.POST.get('password'):
                errors.append('请输入密码')
            else:
                password = request.POST.get('password')

            if errors:
                return HttpResponse(json.dumps(errors, ensure_ascii=False))
            if len(errors) == 0:
                user = authenticate(username = username, password = password)
                if user is None:
                    errors.append('用户名或密码错误')
                    return HttpResponse(json.dumps(errors, ensure_ascii=False))
                elif not user.is_active:
                    errors.append('您的用户不是激活状态')
                    return HttpResponse(json.dumps(errors, ensure_ascii=False))
                else:
                    auth.login(request, user)
                    return HttpResponse('success')   
#                 Another methods of login, caused by not setting AUTHENTICATION_BACKEND in settings.py
#                 userIDFlag = False
#                 userPwdFlag = False
#                 try:
#                     user = User.objects.get(username = request.POST.get('userID'))
#                     userIDFlag = True
#                 except:
#                     pass
#                 if check_password(password, user.password):
#                     userPwdFlag = True
#                 if not userPwdFlag or not userIDFlag:
#                     errors.append('用户名或密码错误')
#                     return HttpResponse(json.dumps(errors, ensure_ascii=False))
#                 elif user.is_active == False:
#                     errors.append('您的用户不是激活状态')
#                     return HttpResponse(json.dumps(errors, ensure_ascii=False))
#                 else:
#                     auth.login(request, user)
#                     return HttpResponse('success')

    elif 'userRegID' in request.POST:
        userRegID = None
        userRegLastName = None
        userRegFirstName = None
        userRegEmail = None
        userRegPassword = None

        if request.method == 'POST':
            if not request.POST.get('userRegID'):
                errors.append('请输入学号')
            elif re.match('PB[1-2][0-9]15[0-9][0-9][0-9][0-9]', request.POST.get('userRegID'), re.I) == None:
                errors.append('学号不正确')
            else:
                userRegID = request.POST.get('userRegID')
            if request.POST.get('userRegID'):
                try:
                    user = User.objects.get(username = request.POST.get('userRegID'))
                    if user:
                        errors.append('学号已注册过')
                except:
                    pass

            if not request.POST.get('userRegLastName'):
                errors.append('请输入姓')
            else:
                userRegLastName = request.POST.get('userRegLastName')

            if not request.POST.get('userRegFirstName'):
                errors.append('请输入名')
            else:
                userRegFirstName = request.POST.get('userRegFirstName')

            if not request.POST.get('userRegEmail'):
                errors.append('请输入邮箱地址')
            else:
                userRegEmail = request.POST.get('userRegEmail')
            if request.POST.get('userRegEmail'):
                try:
                    User.objects.get(email = request.POST.get('userRegEmail'))
                    errors.append('邮箱已注册过')
                except:
                    pass

            if not request.POST.get('userRegPassword'):
                errors.append('请输入密码')
            elif len(request.POST.get('userRegPassword')) < 8 or len(request.POST.get('userRegPassword')) > 20:
                errors.append('请输入长度为8-20位的密码')
            else:
                userRegPassword = request.POST.get('userRegPassword')

            if not request.POST.get('userRegConfirmPassword'):
                errors.append('请确认密码')
            if request.POST.get('userRegConfirmPassword') != request.POST.get('userRegPassword'):
                errors.append('两次输入的密码不一致')

            if errors:
                return HttpResponse(json.dumps(errors, ensure_ascii=False))

            # When authenticating, use check_password, but authenticate function did it for us
            # Create an user
            if len(errors) == 0:
                user = User.objects.create_user(username = userRegID, password = userRegPassword, email = userRegEmail)
                user.first_name = userRegFirstName
                user.last_name = userRegLastName
                user.is_active = False
                user.is_staff = False
                user.is_superuser = False
                user.save()
                randomStr = tokenGen.activateTokenGen()
#                 request.session['test'] = randomStr
                request.session[userRegID] = randomStr
                sourceEmail = settings.DEFAULT_FROM_EMAIL
                destinationEmail = []
                destinationEmail.append(userRegEmail + '@mail.ustc.edu.cn')
                emailSend.sendHtmlEmail(randomStr, sourceEmail, destinationEmail, userRegID)
                return HttpResponse('success')
                
    return render_to_response('welcomePage.html')


def activatePage(request):
    successFlag = False
    try:
        user = User.objects.get(username = request.path.split('/')[3])
        if request.path == '/activate/' + request.session.get(request.path.split('/')[3]) + '/' + request.path.split('/')[3]:
            successFlag = True
            user.is_active = True
            user.save()
    except User.DoesNotExist:
        pass
    return render_to_response('thankForRegisterPage.html', { 'successFlag' : successFlag })
#     return render_to_response('thankForRegisterPage.html', {'context' : request.path.split('/')[3]})


def fileBrowser(request):
    errors = []
    loginFlag = False
    staffFlag = False
    if request.user.is_authenticated:
        loginFlag = True
    if request.user.is_staff:
        staffFlag = True
        
    if loginFlag == True:
        print(request.POST)
        if request.POST:
            if request.method == 'POST':
                try:
                    for payload in request.data.getlist('userFile'):
                        userFile = File.objects.create(filePayload = payload)
                        userFile.fileName = userFile.name
                        userFile.uploader = request.user.last_name + request.user.first_name
                        userFile.save()
                except:
                    errors.append('请选择让要上传的文件')
                    if errors:
                        return HttpResponse(json.dumps(errors, ensure_ascii=False))
                    else:
                        return HttpResponse('success')
            else:
                return HttpResponse('not post')
#             else:
#                 return HttpResponse(json.dumps(request.POST, ensure_ascii=False))
#      else:
#          return HttpResponse('not login')
            
    return render_to_response('fileBrowser.html', {'loginFlag' : loginFlag, 'staffFlag' : staffFlag})
