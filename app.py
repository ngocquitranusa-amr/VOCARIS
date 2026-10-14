<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>English Vocabulary - Học từ vựng</title>

<style>
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --background: #f5f7ff;
    --text: #1e293b;
    --border: #e2e8f0;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: var(--background);
    color: var(--text);
}

header {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    padding: 30px 20px;
    text-align: center;
}

header h1 {
    margin: 0 0 10px;
}

.container {
    max-width: 1000px;
    margin: 30px auto;
    padding: 0 20px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 25px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

h2 {
    margin-top: 0;
}

input {
    width: 100%;
    padding: 14px;
    margin: 8px 0;
    border: 1px solid var(--border);
    border-radius: 10px;
    font-size: 16px;
}

input:focus {
    outline: 2px solid var(--primary);
}

button {
    padding: 12px 20px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-size: 15px;
    transition: 0.2s;
}

button:hover {
    opacity: 0.85;
}

.primary {
    background: var(--primary);
    color: white;
}

.danger {
    background: #ef4444;
    color: white;
}

.edit {
    background: #f59e0b;
    color: white;
}

.secondary {
    background: #e0e7ff;
    color: #4338ca;
}

.stats {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.stat-box {
    background: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
}

.stat-box h1 {
    color: var(--primary);
    margin: 10px;
}

.word-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px;
    border-bottom: 1px solid var(--border);
    gap: 15px;
}

.word-info {
    overflow-wrap: anywhere;
}

.word-info strong {
    font-size: 18px;
    color: var(--primary-dark);
}

.word-info p {
    margin: 6px 0;
    color: #64748b;
}

.actions {
    display: flex;
    gap: 8px;
}

.flashcard {
    min-height: 220px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    cursor: pointer;
    text-align: center;
    padding: 25px;
    user-select: none;
}

.flashcard h1 {
    font-size: 32px;
    overflow-wrap: anywhere;
    max-width: 100%;
}

.flashcard p {
    opacity: 0.8;
}

.flash-controls {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 20px;
}

.message {
    margin-top: 12px;
    font-weight: bold;
}

.success {
    color: #16a34a;
}

.error {
    color: #dc2626;
}

@media(max-width: 600px) {
    .stats {
        grid-template-columns: 1fr;
    }

    .word-item {
        flex-direction: column;
        align-items: flex-start;
    }

    .actions {
        width: 100%;
    }

    .actions button {
        flex: 1;
    }
}
</style>
</head>

<body>

<header>
    <h1>📚 English Vocabulary</h1>
    <p>Ứng dụng học từ vựng tiếng Anh mỗi ngày</p>
</header>

<div class="container">

    <!-- THỐNG KÊ -->
    <div class="stats">
        <div class="stat-box">
            <h3>📖 Tổng số từ vựng</h3>
            <h1 id="totalWords">0</h1>
        </div>

        <div class="stat-box">
            <h3>🎯 Số từ cần học</h3>
            <h1 id="learningWords">0</h1>
        </div>
    </div>

    <!-- THÊM TỪ -->
    <div class="card">
        <h2>➕ Thêm từ vựng mới</h2>

        <form id="wordForm">
            <input
                type="text"
                id="english"
                placeholder="Nhập từ tiếng Anh..."
                required
            >

            <input
                type="text"
                id="vietnamese"
                placeholder="Nhập nghĩa tiếng Việt..."
                required
            >

            <button class="primary" type="submit">
                💾 Lưu từ vựng
            </button>
        </form>

        <div id="message" class="message"></div>
    </div>

    <!-- FLASHCARD -->
    <div class="card">
        <h2>🃏 Học bằng Flashcard</h2>

        <div class="flashcard" id="flashcard">
            <p>Nhấn vào thẻ để xem nghĩa</p>
            <h1 id="flashText">Chưa có từ vựng</h1>
        </div>

        <div class="flash-controls">
            <button class="secondary" onclick="previousCard()">
                ⬅ Trước
            </button>

            <button class="primary" onclick="flipCard()">
                🔄 Lật thẻ
            </button>

            <button class="secondary" onclick="nextCard()">
                Tiếp ➡
            </button>
        </div>

        <p id="cardPosition" style="text-align:center;"></p>
    </div>

    <!-- DANH SÁCH -->
    <div class="card">
        <h2>📚 Danh sách từ vựng</h2>

        <input
            type="text"
            id="search"
            placeholder="🔍 Tìm kiếm từ tiếng Anh hoặc nghĩa tiếng Việt..."
            oninput="renderWords()"
        >

        <div id="wordList"></div>
    </div>

</div>

<script>

// ===============================
// QUẢN LÝ DỮ LIỆU
// ===============================

const STORAGE_KEY = "englishVocabularyV1";

function loadWords() {
    try {
        const saved = JSON.parse(
            localStorage.getItem(STORAGE_KEY) || "[]"
        );

        if (!Array.isArray(saved)) return [];

        return saved.filter(item =>
            item &&
            typeof item.id === "string" &&
            typeof item.english === "string" &&
            typeof item.vietnamese === "string"
        );
    } catch {
        return [];
    }
}

let words = loadWords();

let currentCard = 0;
let isFlipped = false;


// ===============================
// CHUẨN HÓA TỪ VỰNG
// ===============================

function normalizeEnglish(word) {
    return word
        .trim()
        .replace(/\s+/g, " ")
        .toLocaleLowerCase("en");
}

function cleanText(text) {
    return text.trim().replace(/\s+/g, " ");
}


// ===============================
// LƯU DỮ LIỆU
// ===============================

function saveWords() {
    try {
        localStorage.setItem(
            STORAGE_KEY,
            JSON.stringify(words)
        );
        return true;
    } catch {
        showMessage(
            "Không thể lưu dữ liệu. Hãy kiểm tra bộ nhớ trình duyệt.",
            "error"
        );
        return false;
    }
}


// ===============================
// HIỂN THỊ THÔNG BÁO
// ===============================

function showMessage(text, type) {
    const message = document.getElementById("message");

    message.textContent = text;
    message.className = "message " + type;
}


// ===============================
// KIỂM TRA TRÙNG TỪ
// ===============================

function isDuplicate(english, excludeId = null) {
    const normalized = normalizeEnglish(english);

    return words.some(word =>
        normalizeEnglish(word.english) === normalized &&
        word.id !== excludeId
    );
}


// ===============================
// THÊM TỪ VỰNG
// ===============================

document.getElementById("wordForm")
    .addEventListener("submit", function(event) {

    event.preventDefault();

    const englishInput = document.getElementById("english");
    const vietnameseInput = document.getElementById("vietnamese");

    const english = cleanText(englishInput.value);
    const vietnamese = cleanText(vietnameseInput.value);

    if (!english || !vietnamese) {
        showMessage(
            "Vui lòng nhập đầy đủ từ tiếng Anh và nghĩa tiếng Việt!",
            "error"
        );
        return;
    }

    if (isDuplicate(english)) {
        showMessage(
            `❌ Từ "${english}" đã tồn tại trong danh sách!`,
            "error"
        );
        return;
    }

    const newWord = {
        id: crypto.randomUUID(),
        english: english,
        vietnamese: vietnamese,
        createdAt: new Date().toISOString()
    };

    words.push(newWord);

    if (!saveWords()) {
        words.pop();
        return;
    }

    englishInput.value = "";
    vietnameseInput.value = "";

    showMessage(
        `✅ Đã thêm từ "${english}" thành công!`,
        "success"
    );

    renderWords();
    updateStats();
    renderFlashcard();

    englishInput.focus();
});


// ===============================
// HIỂN THỊ DANH SÁCH
// ===============================

function renderWords() {

    const list = document.getElementById("wordList");

    const keyword = document.getElementById("search")
        .value
        .trim()
        .toLocaleLowerCase();

    const filtered = words.filter(word =>
        word.english.toLocaleLowerCase().includes(keyword) ||
        word.vietnamese.toLocaleLowerCase().includes(keyword)
    );

    list.innerHTML = "";

    if (filtered.length === 0) {
        const empty = document.createElement("p");
        empty.textContent = "Không tìm thấy từ vựng nào.";
        list.appendChild(empty);
        return;
    }

    filtered.forEach(word => {

        const item = document.createElement("div");
        item.className = "word-item";

        const info = document.createElement("div");
        info.className = "word-info";

        const english = document.createElement("strong");
        english.textContent = word.english;

        const vietnamese = document.createElement("p");
        vietnamese.textContent = word.vietnamese;

        info.appendChild(english);
        info.appendChild(vietnamese);

        const actions = document.createElement("div");
        actions.className = "actions";

        const editButton = document.createElement("button");
        editButton.className = "edit";
        editButton.textContent = "✏️ Sửa";
        editButton.addEventListener("click", () => editWord(word.id));

        const deleteButton = document.createElement("button");
        deleteButton.className = "danger";
        deleteButton.textContent = "🗑️ Xóa";
        deleteButton.addEventListener("click", () => deleteWord(word.id));

        actions.appendChild(editButton);
        actions.appendChild(deleteButton);

        item.appendChild(info);
        item.appendChild(actions);

        list.appendChild(item);
    });
}


// ===============================
// CHỈNH SỬA TỪ VỰNG
// ===============================

function editWord(id) {

    const word = words.find(item => item.id === id);

    if (!word) return;

    const newEnglish = prompt(
        "Chỉnh sửa từ tiếng Anh:",
        word.english
    );

    if (newEnglish === null) return;

    const english = cleanText(newEnglish);

    if (!english) {
        alert("Từ tiếng Anh không được để trống!");
        return;
    }

    if (isDuplicate(english, id)) {
        alert("Từ tiếng Anh này đã tồn tại!");
        return;
    }

    const newVietnamese = prompt(
        "Chỉnh sửa nghĩa tiếng Việt:",
        word.vietnamese
    );

    if (newVietnamese === null) return;

    const vietnamese = cleanText(newVietnamese);

    if (!vietnamese) {
        alert("Nghĩa tiếng Việt không được để trống!");
        return;
    }

    const oldEnglish = word.english;
    const oldVietnamese = word.vietnamese;

    word.english = english;
    word.vietnamese = vietnamese;

    if (!saveWords()) {
        word.english = oldEnglish;
        word.vietnamese = oldVietnamese;
        return;
    }

    renderWords();
    renderFlashcard();
    showMessage("Đã cập nhật từ vựng!", "success");
}


// ===============================
// XÓA TỪ VỰNG
// ===============================

function deleteWord(id) {

    const word = words.find(item => item.id === id);

    if (!word) return;

    if (!confirm(`Bạn có muốn xóa từ "${word.english}"?`)) {
        return;
    }

    const previousWords = words;

    words = words.filter(item => item.id !== id);

    if (!saveWords()) {
        words = previousWords;
        return;
    }

    if (currentCard >= words.length) {
        currentCard = Math.max(0, words.length - 1);
    }

    isFlipped = false;

    renderWords();
    updateStats();
    renderFlashcard();

    showMessage("Đã xóa từ vựng!", "success");
}


// ===============================
// THỐNG KÊ
// ===============================

function updateStats() {

    document.getElementById("totalWords")
        .textContent = words.length;

    document.getElementById("learningWords")
        .textContent = words.length;
}


// ===============================
// FLASHCARD
// ===============================

function renderFlashcard() {

    const flashText = document.getElementById("flashText");
    const position = document.getElementById("cardPosition");

    if (words.length === 0) {
        flashText.textContent = "Chưa có từ vựng";
        position.textContent = "0 / 0";
        return;
    }

    if (currentCard >= words.length) {
        currentCard = 0;
    }

    const word = words[currentCard];

    flashText.textContent = isFlipped
        ? word.vietnamese
        : word.english;

    position.textContent =
        `${currentCard + 1} / ${words.length}`;
}

function flipCard() {
    if (words.length === 0) return;

    isFlipped = !isFlipped;
    renderFlashcard();
}

function nextCard() {
    if (words.length === 0) return;

    currentCard = (currentCard + 1) % words.length;
    isFlipped = false;

    renderFlashcard();
}

function previousCard() {
    if (words.length === 0) return;

    currentCard =
        (currentCard - 1 + words.length) % words.length;

    isFlipped = false;

    renderFlashcard();
}

document.getElementById("flashcard")
    .addEventListener("click", flipCard);


// ===============================
// KHỞI ĐỘNG
// ===============================

renderWords();
updateStats();
renderFlashcard();

</script>

</body>
</html>
