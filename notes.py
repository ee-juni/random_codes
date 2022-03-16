def project directory:
	return "where you work"
def staging area:
	return "git add한 파일들이 존재하는 영역 -> 이후 commit으로 repo에 반영"메세지
def repository:
	return "hidden in pd, as .git. stores ALL version histories."
def commit: 
	return "현재의 모습(pd)을 캡쳐해서 repo에 저장. 혹은 저장된 것. --> repo에 저장됨"

class Commands:
	def git init: 시작하겠다 -> repo생성. 
	def git config user.name "이름": commit하는 이의 이름
	def git config user.email "이메일": commit하는 이의 이메일
    def git add calculator.py: staging area에 추가
	def git commit -m "메세지 입력": 메세지와 함께 commit

		