const calculateButton = document.getElementById('button');

calculateButton.addEventListener('click', function() {
  // 分と秒の入力値を取得
  const minutes = parseFloat(document.getElementById('min').value);
  const seconds = parseFloat(document.getElementById('sec').value);

  // 1kmの秒数を計算
  const kmTimeInSeconds = minutes * 60 + seconds;

  // フルマラソンの距離と平均ペース（秒/km）を設定
  const marathonDistance = 42.195;
  const marathonPaceInSeconds = kmTimeInSeconds * marathonDistance;

  // フルマラソンの予測タイムを計算（分と秒に変換）
  const marathonPredictedHours = Math.floor(marathonPaceInSeconds / 3600);
  const marathonPredictedMinutes = Math.floor((marathonPaceInSeconds % 3600) / 60);
  const marathonPredictedSeconds = Math.round(marathonPaceInSeconds % 60);

  // 結果を表示する要素を取得
  const resultElement = document.getElementById('result');

  // 結果を表示
  resultElement.textContent = `${marathonPredictedHours}時間${marathonPredictedMinutes}分${marathonPredictedSeconds}秒`;
});
