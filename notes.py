def project directory:
	return "where you work"
def staging area:
	return "git add한 파일들이 존재하는 영역 -> 이후 commit으로 repo에 반영"메세지
def repository:
	return "hidden in pd, as .git. stores ALL version histories."
def commit: 
	return "현재의 모습(pd)을 캡쳐해서 repo에 저장. 혹은 저장된 것. --> repo에 저장됨"

class Commands:
	def git clone <url>: 원격 저장소 로컬에 다운로드
	def git init: 시작하겠다 -> repo생성. 
	def git config user.name "이름": commit하는 이의 이름
	def git config user.email "이메일": commit하는 이의 이메일
	def git add calculator.py: staging area에 추가
	def git commit -m "메세지 입력": 메세지와 함께 commit
		msg 없이 먼저 엔터 치고 입력해도 ㅇㅋ
		i - 입력(INSERT)모드 진입
		ESC, :wq - 엔터하면 커밋msg 저장
		:q - quit
	def git commit --amend: 최신 커밋 수정해서 신규 커밋으로 만들기 
	def git status: 현재 상태 확인
	def git remote add origin <url>: 원격 저장소 지정
	def git push origin master: 원격 저장소에 저장
	# Branches
	def git branch 가지이름: 브랜치 생성
	def git checkout 가지이름: 브랜치 이동
	def git checkout -b 가지이름: 생성+이동 한꺼번에
		# add, commit, push origin 가지이름
	def git pull: 현재 브랜치 내용 가져와서 작업
	def git merge 가지이름: 브랜치 병합
	def git branch -d 가지이름: 브랜치 삭제
	# History
	def git log: 커밋 히스토리 최신순으로 보기(커밋hash,author,date,msg), q로 exit
		git log --pretty=online: 더 이쁘고 깔끔하게 한줄로 보기(hash,msg)
	def git show 커밋hash: 파일 변화 확인. hash 앞 4자리만 써도 ㅇㅋ
	def git add . 
		git commit --amend
	
"""
커밋 메시지 가이드라인

(1) 커밋 메시지의 제목과 상세 설명 사이에는 한 줄을 비워두세요.
(2) 커밋 메시지의 제목 뒤에 온점(.)을 붙이지 마세요.
(3) 커밋 메시지의 제목의 첫 번째 알파벳은 대문자로 작성하세요.
(4) 커밋 메시지의 제목은 명령조로 작성하세요.(Fix it / Fixed it / Fixes it)
(5) 커밋의 상세 내용에는 이런 걸 적으면 좋습니다.
	왜 커밋을 했는지
	어떤 문제가 있었고
	적용한 해결책이 어떤 효과를 가지는지
(6) 다른 사람들이 자신의 코드를 바로 이해할 수 있다고 가정하지 말고 최대한 친절하게 작성하세요.


커밋 가이드라인

(1) 하나의 커밋에는 하나의 수정사항, 하나의 이슈(issue)를 해결한 내용만 남기도록 하세요.
	다양하게 수정을 하고나서 하나의 커밋으로 남기는 것은 좋지 않습니다. 
	하나의 커밋이 하나의 사실만을 갖고 있어야 나중에 이해하기 쉽습니다.
(2) 현재 프로젝트 디렉토리의 상태가 그 내부의 전체 코드를 실행했을 때
	에러가 발생하지 않는 상태인 경우에만 커밋을 하도록 하세요.
	나중에 동료 개발자가 특정 커밋의 코드로 실행했을 때 
	에러가 발생한다면 혼란을 줄 수 있습니다.
	
"""
	
			
