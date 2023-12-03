package track;

import java.util.Scanner;
import java.util.ArrayList;

public class App {

  public static void main(String[] args) {
    // このコードは標準入力と標準出力を用いたサンプルコードです。
    // このコードは好きなように編集・削除してもらって構いません。
    // ---
    // This is a sample code to use stdin and stdout.
    // Edit and remove this code as you like.

    String[] lines = getStdin();
    // // nの値を抽出
    // int n, k = Integer.parseInt(line[0].split(" "));
    // // aの値を抽出
    // String[] aString = line[1].split(" ");
    // int[] a = new int[aString.length];
    // for (int i = 0; i < aString.length; i++) {
    //     a[i] = Integer.parseInt(aString[i]);
    // }
    // System.out.print(n, k , a);


  private static List<List<Integer>> findCardCombinations(int[] cards, int target) {
      List<List<Integer>> combinations = new ArrayList<>();

      // カードを昇順にソートする
      Arrays.sort(cards);

      // 3枚のカードの組み合わせを探索する
      for (int i = 0; i < cards.length - 2; i++) {
          int left = i + 1; // 左端のカードのインデックス
          int right = cards.length - 1; // 右端のカードのインデックス

          while (left < right) {
              int sum = cards[i] + cards[left] + cards[right];

              if (sum == target) {
                  combinations.add(Arrays.asList(cards[i], cards[left], cards[right]));
                  left++;
                  right--;
              } else if (sum < target) {
                  left++;
              } else {
                  right--;
              }
          }
      }

      return combinations;
  }

  private static String[] getStdin() {
    Scanner scanner = new Scanner(System.in);
    ArrayList<String> lines = new ArrayList<>();
    while (scanner.hasNext()) {
      lines.add(scanner.nextLine());
    }
    return lines.toArray(new String[lines.size()]);
  }
}
}
