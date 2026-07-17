import re
import os

file_path = r'c:\Users\cheou\Desktop\portfolio3-1\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the <script> tag that defines CONFIG (around line 567)
# We will replace everything from this <script> to the end of the file.
script_start_idx = content.find('<script>\n    const CONFIG = {')
if script_start_idx == -1:
    script_start_idx = content.find('<script>\r\n    const CONFIG = {')

if script_start_idx == -1:
    print("Could not find the target <script> tag.")
    exit(1)

html_top = content[:script_start_idx]

new_script = """  <script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
    import { getAuth, signInWithPopup, GoogleAuthProvider, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
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
      { name:"김수학", phone:"010-1111-2201", subject:"수학", free:["2교시","4교시"], avatar:"김" },
      { name:"박국어", phone:"010-1111-2202", subject:"국어", free:["1교시","3교시"], avatar:"박" },
      { name:"최과학", phone:"010-1111-2203", subject:"과학", free:["2교시","5교시"], avatar:"최" },
      { name:"이사회", phone:"010-1111-2204", subject:"사회", free:["3교시","4교시"], avatar:"이" },
      { name:"정영어", phone:"010-1111-2205", subject:"영어", free:["1교시","6교시"], avatar:"정" },
      { name:"한창체", phone:"010-1111-2206", subject:"창체", free:["2교시","6교시"], avatar:"한" }
    ];

    function setLogos(){
      document.getElementById("loginLogo").src = CONFIG.LOGO_URL;
      document.getElementById("brandLogo").src = CONFIG.LOGO_URL;
      document.getElementById("heroLogo").src = CONFIG.LOGO_URL;
    }

    function setLinks(){
      const repoLink = document.getElementById("repoLink");
      const deployLink = document.getElementById("deployLink");
      repoLink.href = REPO_URL;
      repoLink.textContent = REPO_URL;
      deployLink.href = CONFIG.DEPLOY_URL;
      deployLink.textContent = CONFIG.DEPLOY_URL;
    }

    window.fillDemo = function(){
      document.getElementById("loginEmail").value = "teacher@sen.go.kr";
    }

    window.login = function(){
      const provider = new GoogleAuthProvider();
      signInWithPopup(auth, provider).catch(error => {
        console.error("Login failed:", error);
      });
    }

    window.logout = function(){
      signOut(auth);
    }

    onAuthStateChanged(auth, (user) => {
      if (user) {
        currentUser = user;
        userName = user.displayName || user.email.split('@')[0];
        document.getElementById("loginScreen").classList.add("hidden");
        document.getElementById("appScreen").classList.remove("hidden");
        document.getElementById("userPill").textContent = `인증 계정: ${user.email}`;
        renderTeachers();
        renderHistory();
        initChat();
      } else {
        currentUser = null;
        document.getElementById("appScreen").classList.add("hidden");
        document.getElementById("loginScreen").classList.remove("hidden");
      }
    });

    function renderTeachers(){
      const wrap = document.getElementById("teacherGrid");
      wrap.innerHTML = TEACHERS.map(t => `
        <div class="teacher-card">
          <div class="avatar">${t.avatar}</div>
          <strong>${t.name}</strong><br>
          <span style="color:#0f766e; font-weight:700;">${t.subject}</span><br>
          <span style="color:#2563eb;">${t.phone}</span><br>
          <span style="color:#64748b; font-size:13px;">공강: ${t.free.join(", ")}</span>
        </div>
      `).join("");
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
          <div class="section-title" style="font-size:18px; margin-top:18px;">추천 보결 가능 교사</div>
          <table>
            <thead>
              <tr>
                <th>교사</th>
                <th>교과</th>
                <th>연락처</th>
                <th>공강 시간</th>
              </tr>
            </thead>
            <tbody>
              ${matches.map(t => `
                <tr>
                  <td>${t.name}</td>
                  <td>${t.subject}</td>
                  <td>${t.phone}</td>
                  <td>${t.free.join(", ")}</td>
                </tr>
              `).join("")}
            </tbody>
          </table>
        `;
      } else {
        matchArea.innerHTML = `<div class="section-title" style="font-size:18px; margin-top:18px;">추천 결과</div><p>해당 교시에 추천 가능한 교사가 없습니다.</p>`;
      }

      const guide = `[보결 수업 안내]
결강 교사: ${absentTeacher}
학급: ${className}
교시: ${period}
교과: ${subject}
단원명: ${unitName}
차시: ${lessonNo}
해야 할 활동: ${activities}
유의사항: ${cautions || "없음"}
작성자: ${userName}`;

      document.getElementById("guideText").value = guide;

      const list = getRequests();
      list.unshift({
        absentTeacher, className, period, subject, unitName, lessonNo,
        createdAt: new Date().toLocaleString("ko-KR")
      });
      saveRequests(list.slice(0, 10));
      renderHistory();

      addChat("시스템", `${absentTeacher} 선생님의 ${className} ${period} 보결 요청이 등록되었습니다. (${unitName} ${lessonNo})`);
    }

    function renderHistory(){
      const list = getRequests();
      const ul = document.getElementById("historyList");
      if(!list.length){
        ul.innerHTML = "<li>아직 보결 요청 기록이 없습니다.</li>";
        return;
      }
      ul.innerHTML = list.map(item => `
        <li>
          <strong>${item.absentTeacher}</strong> · ${item.className} · ${item.period}<br>
          ${item.subject} / ${item.unitName} / ${item.lessonNo}<br>
          <span style="color:#64748b;">${item.createdAt}</span>
        </li>
      `).join("");
    }

    window.copyGuide = function(){
      const text = document.getElementById("guideText").value.trim();
      if(!text){
        alert("먼저 보결 요청서를 작성해주세요.");
        return;
      }
      navigator.clipboard.writeText(text).then(() => {
        alert("안내문을 복사했습니다.");
      });
    }

    window.shareGuideToChat = function(){
      const text = document.getElementById("guideText").value.trim();
      if(!text){
        alert("먼저 보결 요청서를 작성해주세요.");
        return;
      }
      addChat(userName, text.replace(/\\n/g, " / "));
    }

    let chatUnsubscribe = null;
    function initChat(){
      const chatRef = query(ref(db, 'chats'), limitToLast(40));
      if (chatUnsubscribe) chatUnsubscribe();
      
      chatUnsubscribe = onValue(chatRef, (snapshot) => {
        const box = document.getElementById("chatBox");
        box.innerHTML = "";
        if (snapshot.exists()) {
          const chats = [];
          snapshot.forEach((child) => {
            chats.push(child.val());
          });
          box.innerHTML = chats.map(item => `
            <div class="chat-msg">
              <strong>${item.author}</strong><br>
              ${item.text}<br>
              <span style="font-size:12px; color:#64748b;">${item.time}</span>
            </div>
          `).join("");
          box.scrollTop = box.scrollHeight;
        }
      });
    }

    function addChat(author, text){
      push(ref(db, 'chats'), {
        author,
        text,
        time: new Date().toLocaleString("ko-KR")
      });
    }

    window.sendChat = function(){
      const input = document.getElementById("chatInput");
      const text = input.value.trim();
      if(!text) return;
      addChat(userName, text);
      input.value = "";
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
