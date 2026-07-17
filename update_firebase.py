import os

file_path = r'c:\Users\cheou\Desktop\portfolio3-1\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

script_start_idx = content.find('<script type="module">')
if script_start_idx == -1:
    script_start_idx = content.find('<script>\n    const CONFIG = {')

if script_start_idx == -1:
    print("Could not find the target <script> tag.")
    exit(1)

html_top = content[:script_start_idx]

new_script = """<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
    import { getAuth, signInWithPopup, GoogleAuthProvider, signInAnonymously, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
    import { getDatabase, ref, push, onValue, query, limitToLast } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-database.js";

    const firebaseConfig = {
      apiKey: "AIzaSyA4jbnTnwXcJVS2fBCv5B8ftxA9u95QFTg",
      authDomain: "portfolio-aca66.firebaseapp.com",
      projectId: "portfolio-aca66",
      storageBucket: "portfolio-aca66.firebasestorage.app",
      messagingSenderId: "1064758521913",
      appId: "1:1064758521913:web:e9f221d7373af3f6861de8",
      measurementId: "G-46NTXEDBZQ"
    };

    const app = initializeApp(firebaseConfig);
    const auth = getAuth(app);
    const db = getDatabase(app);

    let currentUser = null;
    let userName = "선생님";

    const CONFIG = {
      SCHOOL: "서울풍납초등학교",
      AUTHOR: "교사 김규태",
      LOGO_URL: "https://images.wrks.ai/dalle/gnShJUSiEOpgut4YKCDQa7SBTtjlbc4ylN3xc9Cz.png",
      GITHUB_USER: "GT7-design",
      REPO_NAME: "portfolio3",
      DEPLOY_URL: "https://portfolio3-five-dusky.vercel.app/",
      ALLOWED_DOMAINS: ["gmail.com", "sen.go.kr", "school.kr", "edu.sen.go.kr"]
    };

    const REPO_URL = `https://github.com/${CONFIG.GITHUB_USER}/${CONFIG.REPO_NAME}`;
    const REQUEST_KEY = "pungnap_portfolio3_requests";

    const TEACHERS = [
      { name:"김수학", phone:"010-1111-2201", subject:"수학", free:["2교시","4교시"], avatar:"김", avatarUrl:"https://api.dicebear.com/7.x/avataaars/svg?seed=TeacherMathKim&backgroundColor=b6e3f4" },
      { name:"박국어", phone:"010-1111-2202", subject:"국어", free:["1교시","3교시"], avatar:"박", avatarUrl:"https://api.dicebear.com/7.x/avataaars/svg?seed=TeacherKoreanPark&backgroundColor=c0aede" },
      { name:"최과학", phone:"010-1111-2203", subject:"과학", free:["2교시","5교시"], avatar:"최", avatarUrl:"https://api.dicebear.com/7.x/avataaars/svg?seed=TeacherScienceChoi&backgroundColor=d1d4f9" },
      { name:"이사회", phone:"010-1111-2204", subject:"사회", free:["3교시","4교시"], avatar:"이", avatarUrl:"https://api.dicebear.com/7.x/avataaars/svg?seed=TeacherSocialLee&backgroundColor=ffd5dc" },
      { name:"정영어", phone:"010-1111-2205", subject:"영어", free:["1교시","6교시"], avatar:"정", avatarUrl:"https://api.dicebear.com/7.x/avataaars/svg?seed=TeacherEnglishJung&backgroundColor=ffdfbf" },
      { name:"한창체", phone:"010-1111-2206", subject:"창체", free:["2교시","6교시"], avatar:"한", avatarUrl:"https://api.dicebear.com/7.x/avataaars/svg?seed=TeacherCreativeHan&backgroundColor=c6f6d5" }
    ];

    function setLogos(){
      const l1 = document.getElementById("loginLogo");
      const l2 = document.getElementById("brandLogo");
      const l3 = document.getElementById("heroLogo");
      if(l1) l1.src = CONFIG.LOGO_URL;
      if(l2) l2.src = CONFIG.LOGO_URL;
      if(l3) l3.src = CONFIG.LOGO_URL;
    }

    function setLinks(){
      const repoLink = document.getElementById("repoLink");
      const deployLink = document.getElementById("deployLink");
      if(repoLink){
        repoLink.href = REPO_URL;
        repoLink.textContent = REPO_URL;
      }
      if(deployLink){
        deployLink.href = CONFIG.DEPLOY_URL;
        deployLink.textContent = CONFIG.DEPLOY_URL;
      }
    }

    window.loginWithGoogle = function(){
      const provider = new GoogleAuthProvider();
      signInWithPopup(auth, provider).catch(error => {
        console.error("Google Login failed:", error);
        alert("Google 계정 인증이 취소되었거나 오류가 발생했습니다.\\n간편하게 '🚀 시연용 계정 바로 1초 로그인'을 이용해 보세요!");
      });
    }

    window.login = window.loginWithGoogle;

    window.loginWithDemo = async function(){
      const emailInput = document.getElementById("loginEmail");
      const nameInput = document.getElementById("loginName");
      
      const email = (emailInput?.value.trim()) || "teacher@sen.go.kr";
      const name = (nameInput?.value.trim()) || "김시연 선생님 (시연용)";

      try {
        await signInAnonymously(auth);
      } catch(e) {
        console.log("Firebase Anonymous auth fallback or local demo mode:", e);
      }

      currentUser = {
        uid: "demo-" + Date.now(),
        email: email,
        displayName: name,
        photoURL: `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(name)}&backgroundColor=b6e3f4`,
        isDemo: true
      };
      userName = name;

      document.getElementById("loginScreen").classList.add("hidden");
      document.getElementById("appScreen").classList.remove("hidden");
      document.getElementById("userPill").innerHTML = `<span class="pill-badge pill-demo">🚀 시연용 계정</span> <strong>${userName}</strong> (${email})`;
      
      renderTeachers();
      renderHistory();
      initChat();

      addChat("시스템", `🎉 [${userName}]님이 시연용 계정으로 로그인하였습니다. (보결 추천 및 실시간 채팅 가능)`);
    }

    window.logout = function(){
      signOut(auth).catch(() => {});
      currentUser = null;
      document.getElementById("appScreen").classList.add("hidden");
      document.getElementById("loginScreen").classList.remove("hidden");
    }

    onAuthStateChanged(auth, (user) => {
      if (user) {
        if (user.isAnonymous && currentUser && currentUser.isDemo) {
          return;
        }
        if (!user.isAnonymous) {
          currentUser = user;
          userName = user.displayName || user.email.split('@')[0];
          document.getElementById("loginScreen").classList.add("hidden");
          document.getElementById("appScreen").classList.remove("hidden");
          document.getElementById("userPill").innerHTML = `<span class="pill-badge pill-google">🌐 Google 인증</span> <strong>${userName}</strong> (${user.email})`;
          renderTeachers();
          renderHistory();
          initChat();
        }
      } else {
        if (!currentUser || !currentUser.isDemo) {
          currentUser = null;
          document.getElementById("appScreen").classList.add("hidden");
          document.getElementById("loginScreen").classList.remove("hidden");
        }
      }
    });

    function renderTeachers(){
      const wrap = document.getElementById("teacherGrid");
      if(!wrap) return;
      wrap.innerHTML = TEACHERS.map(t => `
        <div class="teacher-card">
          <div class="teacher-avatar-wrap">
            <img src="${t.avatarUrl}" class="teacher-avatar-img" alt="${t.name}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex'">
            <div class="avatar" style="display:none;">${t.avatar}</div>
          </div>
          <strong>${t.name}</strong><br>
          <span style="color:#0f766e; font-weight:800; font-size:14px;">${t.subject}</span><br>
          <span style="color:#2563eb; font-size:13px;">${t.phone}</span><br>
          <span style="color:#64748b; font-size:12px; display:block; margin:6px 0;">공강: ${t.free.join(", ")}</span>
          <button class="btn-teacher-chat" onclick="sendChatAsTeacher('${t.name}')">💬 ${t.name}로 채팅 테스트</button>
        </div>
      `).join("");
    }

    window.sendChatAsTeacher = function(teacherName){
      const t = TEACHERS.find(item => item.name === teacherName);
      if(!t) return;
      const presets = [
        `안녕하세요, ${t.subject} 담당 ${t.name}입니다. 보강 가능합니다!`,
        `네, 안내문 확인했습니다. ${t.free[0]} 수업 들어가겠습니다.`,
        `${t.subject} 교과서 및 실습자료 교실에 준비해두겠습니다.`,
        `잠시 후 교무실로 내려가서 상세 사항 상의드리겠습니다.`
      ];
      const randomMsg = presets[Math.floor(Math.random() * presets.length)];
      addChat(t.name, randomMsg, t.avatarUrl);
    }

    function getRequests(){
      return JSON.parse(localStorage.getItem(REQUEST_KEY) || "[]");
    }

    function saveRequests(list){
      localStorage.setItem(REQUEST_KEY, JSON.stringify(list));
    }

    function recommendTeachers(subject, period){
      return TEACHERS
        .filter(t => t.free.includes(period))
        .sort((a,b) => {
          const aScore = a.subject === subject ? 1 : 0;
          const bScore = b.subject === subject ? 1 : 0;
          return bScore - aScore;
        });
    }

    window.submitRequest = function(){
      const absentTeacher = document.getElementById("absentTeacher").value.trim();
      const period = document.getElementById("period").value;
      const className = document.getElementById("className").value.trim();
      const subject = document.getElementById("subject").value.trim();
      const unitName = document.getElementById("unitName").value.trim();
      const lessonNo = document.getElementById("lessonNo").value.trim();
      const activities = document.getElementById("activities").value.trim();
      const cautions = document.getElementById("cautions").value.trim();

      if(!absentTeacher || !className || !subject || !unitName || !lessonNo || !activities){
        alert("필수 항목을 모두 입력해주세요.");
        return;
      }

      const matches = recommendTeachers(subject, period);
      const matchArea = document.getElementById("matchArea");

      if(matches.length){
        matchArea.innerHTML = `
          <div class="section-title" style="font-size:18px; margin-top:20px;"><span>✅ 추천 보결 가능 교사</span></div>
          <table>
            <thead>
              <tr>
                <th>아바타</th>
                <th>교사명</th>
                <th>담당 교과</th>
                <th>연락처</th>
                <th>공강 시간</th>
              </tr>
            </thead>
            <tbody>
              ${matches.map(t => `
                <tr>
                  <td style="width:50px;"><img src="${t.avatarUrl}" style="width:36px;height:36px;border-radius:10px;object-fit:cover;border:1px solid #c9f6f0;" alt="${t.name}"></td>
                  <td style="font-weight:800;">${t.name}</td>
                  <td style="color:var(--primary); font-weight:700;">${t.subject}</td>
                  <td>${t.phone}</td>
                  <td>${t.free.join(", ")}</td>
                </tr>
              `).join("")}
            </tbody>
          </table>
        `;
      } else {
        matchArea.innerHTML = `<div class="section-title" style="font-size:18px; margin-top:20px;"><span>💡 추천 결과</span></div><p>해당 교시에 공강인 추천 가능 교사가 없습니다.</p>`;
      }

      const guide = `[서울풍납초 보결 수업 안내서]
• 결강 교사: ${absentTeacher} 선생님
• 학급 및 교시: ${className} / ${period}
• 교과 및 단원: ${subject} (${unitName})
• 차시: ${lessonNo}
• 해야 할 활동: ${activities}
• 유의사항: ${cautions || "없음"}
• 작성자: ${userName}`;

      document.getElementById("guideText").value = guide;

      const list = getRequests();
      list.unshift({
        absentTeacher, className, period, subject, unitName, lessonNo,
        createdAt: new Date().toLocaleString("ko-KR")
      });
      saveRequests(list.slice(0, 10));
      renderHistory();

      addChat("시스템", `📌 [${absentTeacher} 선생님] ${className} ${period} 보결 요청이 등록되었습니다. (${unitName} ${lessonNo})`);
    }

    function renderHistory(){
      const list = getRequests();
      const ul = document.getElementById("historyList");
      if(!ul) return;
      if(!list.length){
        ul.innerHTML = "<li style='color:var(--muted);'>아직 작성된 보결 요청 기록이 없습니다.</li>";
        return;
      }
      ul.innerHTML = list.map(item => `
        <li>
          <strong>${item.absentTeacher}</strong> · ${item.className} · ${item.period}<br>
          <span style="color:var(--primary); font-weight:700;">${item.subject}</span> / ${item.unitName} / ${item.lessonNo}<br>
          <span style="color:#94a3b8; font-size:12px;">${item.createdAt}</span>
        </li>
      `).join("");
    }

    window.copyGuide = function(){
      const text = document.getElementById("guideText").value.trim();
      if(!text){
        alert("먼저 보결 요청서를 작성하여 안내문을 생성해주세요.");
        return;
      }
      navigator.clipboard.writeText(text).then(() => {
        alert("수업 안내문이 클립보드에 복사되었습니다.");
      });
    }

    window.shareGuideToChat = function(){
      const text = document.getElementById("guideText").value.trim();
      if(!text){
        alert("먼저 보결 요청서를 작성하여 안내문을 생성해주세요.");
        return;
      }
      addChat(userName, text);
    }

    function getAvatarForUser(authorName) {
      if (!authorName) return `https://api.dicebear.com/7.x/avataaars/svg?seed=User&backgroundColor=e6fffb`;
      const t = TEACHERS.find(item => item.name === authorName || authorName.includes(item.name));
      if (t) return t.avatarUrl;
      if (currentUser && (currentUser.displayName === authorName || authorName === userName) && currentUser.photoURL) {
        return currentUser.photoURL;
      }
      if (authorName === "시스템") {
        return `https://api.dicebear.com/7.x/bottts/svg?seed=System&backgroundColor=d8ece8`;
      }
      return `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(authorName)}&backgroundColor=e6fffb`;
    }

    let chatUnsubscribe = null;
    function initChat(){
      const chatRef = query(ref(db, 'chats'), limitToLast(50));
      if (chatUnsubscribe) chatUnsubscribe();
      
      chatUnsubscribe = onValue(chatRef, (snapshot) => {
        const box = document.getElementById("chatBox");
        if(!box) return;
        box.innerHTML = "";
        if (snapshot.exists()) {
          const chats = [];
          snapshot.forEach((child) => {
            chats.push(child.val());
          });
          box.innerHTML = chats.map(item => {
            const isMe = (item.author === userName) || (currentUser && item.author === currentUser.displayName);
            const isSystem = item.author === "시스템";
            const avatar = item.avatarUrl || getAvatarForUser(item.author);
            if (isSystem) {
              return `
                <div style="text-align:center; margin:10px 0; font-size:12px; color:#64748b; background:#f1f5f9; padding:6px 12px; border-radius:99px; align-self:center;">
                  🤖 ${item.text} <span style="font-size:10px; color:#94a3b8;">(${item.time || ''})</span>
                </div>
              `;
            }
            return `
            <div class="chat-msg-row ${isMe ? 'chat-me' : 'chat-other'}">
              <img src="${avatar}" class="chat-avatar" alt="${item.author}" onerror="this.src='https://api.dicebear.com/7.x/avataaars/svg?seed=Teacher&backgroundColor=e6fffb'">
              <div class="chat-bubble-wrap">
                <div class="chat-author">${item.author} ${isMe ? '<span class="chat-badge-me">나</span>' : ''}</div>
                <div class="chat-bubble">${item.text}</div>
                <div class="chat-time">${item.time || ''}</div>
              </div>
            </div>
            `;
          }).join("");
          box.scrollTop = box.scrollHeight;
        } else {
          box.innerHTML = `<div style="text-align:center; color:var(--muted); padding:40px 0;">첫 번째 채팅 메시지를 남겨보세요!</div>`;
        }
      });
    }

    function addChat(author, text, customAvatar = null){
      const avatarUrl = customAvatar || getAvatarForUser(author);
      push(ref(db, 'chats'), {
        author,
        text,
        avatarUrl,
        time: new Date().toLocaleTimeString("ko-KR", { hour: '2-digit', minute: '2-digit' }),
        fullTime: new Date().toLocaleString("ko-KR")
      });
    }

    window.sendChat = function(){
      const input = document.getElementById("chatInput");
      const text = input?.value.trim();
      if(!text) return;
      addChat(userName, text);
      input.value = "";
    }

    window.sendQuickChat = function(text){
      if(!text) return;
      addChat(userName, text);
    }

    // Modal Control Functions
    window.openPolicyModal = function(tabName = 'guide'){
      const modal = document.getElementById("policyModal");
      if(!modal) return;
      modal.classList.remove("hidden");
      switchPolicyTab(tabName);
    }

    window.closePolicyModal = function(){
      const modal = document.getElementById("policyModal");
      if(modal) modal.classList.add("hidden");
    }

    window.switchPolicyTab = function(tabName){
      document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
      document.querySelectorAll(".tab-pane").forEach(pane => pane.classList.add("hidden"));
      
      const targetBtn = document.getElementById(`tabBtn_${tabName}`);
      const targetPane = document.getElementById(`tabPane_${tabName}`);
      if(targetBtn && targetPane){
        targetBtn.classList.add("active");
        targetPane.classList.remove("hidden");
      }
    }

    setLogos();
    setLinks();

  </script>
</body>
</html>
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html_top + new_script)

print("index.html successfully updated.")
