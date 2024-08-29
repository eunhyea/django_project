from django.shortcuts import render
# 현재 디렉토리의 forms에서 LoginForm을 가져올거야
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def user_login(request): # 주소줄로 클라이언트의 request를 받아서,
    # 요청의 방법 확인 : POST ? GET ?
    if request.method == 'POST':
        
        # 폼에서 데이터를 받아서 유효성 검사를 함 ex)id/pw 잘 입력?
        # 화면단에서 받아온 request.POST를 받아와서 사용함
        form = LoginForm(request.POST)
        if form.is_valid(): # 유효성검사, POST이면 진행

            # 폼으로 온 데이터를 dict 형식으로 클리닝해줌
            cd = form.cleaned_data
            # 입력받은 username, password를 db와 일치하는지 확인
            user = authenticate(request, username=cd['username'], password=cd['password'])
            
            # user가 None이면 사용 불가
            if user is not None : 
                
                # 휴면계정인지 확인
                if user.is_active:
                    login(request, user) # active user라면 login 함수 불러와
                    response = HttpResponse() # Http로 response 응답 객체 생성
                    
                    # 쿠키
                    response.set_cookie('user', user) # user라는 이름으로 user를 달아서 쿠키 저장, get방식으로 보냄
                    response.set_cookie('testCookie', 'value testCookie') # user라는 이름으로 user를 달아서 쿠키 저장, get방식으로 보냄
                    response.set_cookie('testCookie2', 'value testCookie2') # user라는 이름으로 user를 달아서 쿠키 저장, get방식으로 보냄

                    # 세션
                    request.session['testSession'] = 'value session' # 서버가 관리하고 넘겨줌

                    # 출력
                    response.content = f'''로그인 되셨습니다! \n
                    {request.COOKIES.get("user"), request.COOKIES.get("testCookie")} \n
                    session: {request.session.get("testSession")}''' # cookie에서 user라는 값을 가져와서 사용
                    

                    return response # response를 전달, 로그인 되셨습니다.
                else : # 일치하지 않으면 잘못입력하셨습니다.
                    return HttpResponse('사용 불가')
            else : # 없는 사용자
                return HttpResponse('로그인 정보가 틀립니다.')
        
    else :
        form = LoginForm() # POST가 아니면 다시 돌려보냄
    return render(request, 'account/login.html', {'form': form})