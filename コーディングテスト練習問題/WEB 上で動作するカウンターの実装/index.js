// カウンターの初期値を0で設定
let counterValue = 0;

// カウンターの値を表示するための関数
function updateDisplay() {
    document.getElementById('display').textContent = counterValue;
}

// +1ボタンのクリックイベントリスナー
document.getElementById('add').addEventListener('click', function() {
    counterValue += 1;
    if (counterValue > 100) {
        counterValue = 100;
    }
    updateDisplay();
});

// -1ボタンのクリックイベントリスナー
document.getElementById('sub').addEventListener('click', function() {
    counterValue -= 1;
    if (counterValue < 0) {
        counterValue = 0;
    }
    updateDisplay();
});

// *2ボタンのクリックイベントリスナー
document.getElementById('mul').addEventListener('click', function() {
    counterValue *= 2;
    if (counterValue > 100) {
        counterValue = 100;
    }
    updateDisplay();
});

// 初期表示を行う
updateDisplay();
