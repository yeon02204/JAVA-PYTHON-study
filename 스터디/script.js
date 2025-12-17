// ==========================================
// 모드 박스 클릭 이벤트 (로그인 패널 열기/닫기)
// ==========================================
const modeItems = document.querySelectorAll('.mode-item');
const panel = document.querySelector('#studentBox');

modeItems.forEach(item => {
  item.addEventListener('click', () => {
    const isActive = item.classList.contains('active');

    // 일단 전부 active 제거
    modeItems.forEach(m => m.classList.remove('active'));

    if (isActive) {
      // 이미 선택된 걸 다시 눌렀으면 닫기
      panel.classList.add('hidden');
    } else {
      // 새로 선택된 경우: 해당 박스만 active + 패널 열기
      item.classList.add('active');
      panel.classList.remove('hidden');
    }
  });
});

// ==========================================
// 회원가입 모달 열기/닫기
// ==========================================
const overlay = document.querySelector("#overlay");
const joinBtn = document.querySelector(".join");
const btnCancel = document.querySelector("#btnCancel");

const openModal = () => {
  overlay.classList.add("open");
  document.body.style.overflow = "hidden";
};

const closeModal = () => {
  overlay.classList.remove("open");
  document.body.style.overflow = "";
};

// 회원가입 버튼 클릭 → 모달 열기
joinBtn.addEventListener("click", openModal);

// 취소 버튼 클릭 → 모달 닫기
btnCancel.addEventListener("click", closeModal);

// 모달 바깥(검은 배경) 클릭 시 닫기
overlay.addEventListener("click", (e) => {
  const box = overlay.querySelector(".modal");
  if (!box.contains(e.target)) closeModal();
});

// ESC 키로 닫기
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && overlay.classList.contains("open")) closeModal();
});