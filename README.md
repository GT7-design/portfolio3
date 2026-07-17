# 서울풍납초등학교 스마트 보결 배정 시스템 (포트폴리오 3)

[![Deploy to Vercel](https://img.shields.io/badge/Deploy-Vercel-000000?style=for-the-badge&logo=vercel)](https://portfolio3-five-dusky.vercel.app/)
[![Firebase](https://img.shields.io/badge/Firebase-Backend-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **서울풍납초등학교 교사 김규태**  
> 교사 개발자 성장형 산출물 (포트폴리오 3) - 결강 및 보강 상황에서의 스마트 배정, 안내문 자동 생성, 실시간 교직원 채팅 시스템

---

## 🎯 산출물 8대 필수 조건 충족 안내

| 조건 번호 | 조건 항목 | 충족 및 구현 내용 |
| :---: | :--- | :--- |
| **01** | **소속학교·이름 표기** | 시스템 첫 화면(로그인), 상단 헤더, 메인 대시보드 카드, 하단 푸터에 **서울풍납초등학교 / 교사 김규태** 명확히 표기 |
| **02** | **개인정보처리방침** | 수집 항목(Google 계정 정보, 이름, 아바타, 업무 입력 정보 등), 이용 목적, 보관 기간, 문의처(`teacher@sen.go.kr`)를 모달 창 및 하단 링크로 상세 표기 |
| **03** | **사용약관** | 서비스 이용 조건, 책임 범위(행정 결재 절차 준수), 금지 행위(계정 도용, 품위 손상 채팅 등), 변경 안내 사항을 모달 창에 상세 표기 |
| **04** | **GitHub 레포지토리 주소** | 소스코드 공개 및 협업 이력 확인 가능한 GitHub URL(`https://github.com/GT7-design/portfolio3`) 상시 상단 및 푸터 제공 |
| **05** | **Firebase 백엔드 연동** | **Firebase Authentication**(Google 소셜 로그인 및 Anonymous fallback) + **Firebase Realtime Database**(실시간 교사 채팅 및 메시지 동기화) 안정적 처리 |
| **06** | **프론트엔드 웹주소** | 누구나 실시간 접속 가능한 배포 URL (`https://portfolio3-five-dusky.vercel.app/`) 제공 |
| **07** | **사용방법 안내** | 로그인/인증, 보결 추천 및 안내문 자동 작성, 실시간 채팅 공유 및 주의사항을 4단계 구조로 알기 쉽게 모달 및 안내 페이지로 정리 |
| **08** | **배포 완료 확인** | 웹 정상 접속, 내부/외부 링크 작동, 정책 페이지 모달 연결, Firebase 데이터 실시간 저장 및 불러오기 최종 검증 완료 ✅ |

---

## 🚀 주요 차별화 기능

### 1. Dual 인증 시스템 (Google 계정 연동 + 시연용 1초 자동 로그인)
- **Google 계정 로그인**: Firebase Authentication GoogleAuthProvider를 이용해 실제 교직원 구글 계정으로 안전하게 인증합니다.
- **🚀 시연용 계정 1초 자동 로그인**: 심사위원이나 첫 방문자가 번거로운 계정 입력 없이 `[🚀 시연용 계정 바로 1초 로그인]` 버튼 클릭만으로 즉시 시연용 교직원(`teacher@sen.go.kr` / `김시연 선생님`)으로 입장하여 모든 기능을 테스트할 수 있습니다.

### 2. 보결 가능 교사 추천 & 안내문 자동 완성
- 결강 교사, 교시, 학급, 교과, 차시 및 유의사항을 입력하면 해당 교시에 공강인 교사들을 자동으로 필터링 및 우선 순위 추천합니다.
- 클릭 한 번으로 정돈된 양식의 **보결 수업 안내서**가 자동 생성되며, 클립보드 복사 또는 채팅창 즉시 공유가 가능합니다.

### 3. 교사 아바타가 지원되는 실시간 채팅 (Firebase Realtime Database)
- 교사별 친근하고 세련된 **프로필 아바타 이미지**(DiceBear Vector Avatars 등)가 함께 표시되는 슬랙/카카오톡 형태의 실시간 메신저 UI를 구현했습니다.
- **채팅 시연 기능**: 메인 화면의 교사 카드에서 `[💬 김수학로 채팅 테스트]` 등 버튼을 누르면 해당 교사의 프로필 이미지와 이름으로 즉시 테스트 메시지가 전송됩니다.
- **간편 응답 문구 제공**: `[⚡ 보강 가능합니다!]`, `[⚡ 안내문 확인했습니다.]`, `[⚡ 자료 준비하겠습니다.]` 등 버튼 클릭만으로 빠른 업무 소통이 가능합니다.

### 4. 사용방법 및 정책 완비 (약관, 방침, 가이드 모달)
- 첫 방문자도 10초 만에 구조를 이해할 수 있도록 **[📖 사용방법 및 정책 안내]** 모달 창을 상단 및 하단 어디서나 클릭하여 열어볼 수 있습니다.

---

## 🛠️ 기술 스택 (Tech Stack)
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphic Modern UI, Responsive Design), Vanilla JavaScript (ES6+ Modules)
- **Backend & DB**: Firebase Authentication, Firebase Realtime Database
- **Deployment**: Vercel Cloud Platform

---

## 📝 이용 방법 및 문의
1. 배포 주소([https://portfolio3-five-dusky.vercel.app/](https://portfolio3-five-dusky.vercel.app/))에 접속합니다.
2. `[Google 계정 로그인]` 또는 `[🚀 시연용 계정 바로 1초 로그인]`을 클릭합니다.
3. 보결 요청서를 작성하고 추천 교사 및 안내문을 확인한 후, 실시간 채팅 방에서 교사 아바타와 함께 소통을 체험합니다.
4. **문의처**: 서울풍납초등학교 교사 김규태 (`teacher@sen.go.kr`)