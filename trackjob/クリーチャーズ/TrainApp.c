using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
public class MainApp
{
    static void Main(string[] args)
    {
        var lines = GetStdin();
        string[] inputs = lines[0].Split(' ');
        string R = inputs[0];
        string S = inputs[1];
        string DIR = inputs[2];
        int HH = int.Parse(inputs[3]);
        List<int> answerList = new List<int>();
        int hour;
        int minute;
        int[] next_time;
        int time;
        int[] arrive_time;

        int[] A_times = {0, 3, 5, 2, 3, 4, 3, 4, 2, 2, 3, 6, 2};
        int[] B_times = {0, 4, 3, 3, 2, 3, 0};

        int[,] A1_start_A7 = new int[6 * 17 + 1, 2];
        A1_start_A7[0, 0] = 5;
        A1_start_A7[0, 1] = 55;

        int[,] A1_start_A13 = new int[6 * 17, 2];
        A1_start_A13[0, 0] = 6;
        A1_start_A13[0, 1] = 0;

        int[,] A7_start_A1 = new int[6 * 17 + 1, 2];
        A7_start_A1[0, 0] = 6;
        A7_start_A1[0, 1] = 6;

        int[,] A7_start_A13 = new int[1, 2];
        A7_start_A13[0, 0] = 6;
        A7_start_A13[0, 1] = 10;

        int[,] A13_start_A1 = new int[6 * 17, 2];
        A13_start_A1[0, 0] = 5;
        A13_start_A1[0, 1] = 52;

        int[,] A13_start_A7 = new int[1, 2];
        A13_start_A7[0, 0] = 22;
        A13_start_A7[0, 1] = 52;

        int[,] B1_start_A7 = new int[10 * 17, 2];
        B1_start_A7[0, 0] = 6;
        B1_start_A7[0, 1] = 0;

        int[,] A7_start_B1 = new int[10 * 17, 2];
        A7_start_B1[0, 0] = 6;
        A7_start_B1[0, 1] = 11;

        for (int i = 1; i < 6 * 17 + 1; i++)
        {
            hour = A1_start_A7[i - 1, 0];
            minute = A1_start_A7[i - 1, 1];
            next_time = GetTimes(hour, minute, 10);
            A1_start_A7[i, 0] = next_time[0];
            A1_start_A7[i, 1] = next_time[1];
        }

        for (int i = 1; i < 6 * 17; i++)
        {
            hour = A1_start_A13[i - 1, 0];
            minute = A1_start_A13[i - 1, 1];
            next_time = GetTimes(hour, minute, 10);
            A1_start_A13[i, 0] = next_time[0];
            A1_start_A13[i, 1] = next_time[1];
        }

        for (int i = 1; i < 6 * 17 + 1; i++)
        {
            hour = A7_start_A1[i - 1, 0];
            minute = A7_start_A1[i - 1, 1];
            next_time = GetTimes(hour, minute, 10);
            A7_start_A1[i, 0] = next_time[0];
            A7_start_A1[i, 1] = next_time[1];
        }

        for (int i = 1; i < 6 * 17; i++)
        {
            hour = A13_start_A1[i - 1, 0];
            minute = A13_start_A1[i - 1, 1];
            next_time = GetTimes(hour, minute, 10);
            A13_start_A1[i, 0] = next_time[0];
            A13_start_A1[i, 1] = next_time[1];
        }

        for (int i = 1; i < 10 * 17; i++)
        {
            hour = B1_start_A7[i - 1, 0];
            minute = B1_start_A7[i - 1, 1];
            next_time = GetTimes(hour, minute, 6);
            B1_start_A7[i, 0] = next_time[0];
            B1_start_A7[i, 1] = next_time[1];
        }

        for (int i = 1; i < 10 * 17; i++)
        {
            hour = A7_start_B1[i - 1, 0];
            minute = A7_start_B1[i - 1, 1];
            next_time = GetTimes(hour, minute, 6);
            A7_start_B1[i, 0] = next_time[0];
            A7_start_B1[i, 1] = next_time[1];
        }

        if (R == "A")
        {
            if (DIR == "U") // '='を'=='に修正
            {
                int num = int.Parse(S[1].ToString()); // 文字列から数値に変換
                time = sum(A_times, 0, num); // sum関数の呼び出し
                if (num <= 6)
                {
                    for (int i = 0; i < 6 * 17 + 1; i++)
                    {
                        hour = A1_start_A7[i, 0];
                        minute = A1_start_A7[i, 1];
                        arrive_time = GetTimes(hour, minute, time);
                        if (arrive_time[0] == HH)
                        {
                            answerList.Add(arrive_time[1]);
                        }
                    }
                    for (int i = 0; i < 6 * 17; i++)
                    {
                        hour = A1_start_A13[i, 0];
                        minute = A1_start_A13[i, 1];
                        arrive_time = GetTimes(hour, minute, time);
                        if (arrive_time[0] == HH)
                        {
                            answerList.Add(arrive_time[1]);
                        }
                    }
                }
                else
                {
                    for (int i = 0; i < 6 * 17; i++)
                    {
                        hour = A1_start_A13[i, 0];
                        minute = A1_start_A13[i, 1];
                        arrive_time = GetTimes(hour, minute, time);
                        if (arrive_time[0] == HH)
                        {
                            answerList.Add(arrive_time[1]);
                        }
                    }
                    hour = A7_start_A13[0, 0];
                    minute = A7_start_A13[0, 1];
                    arrive_time = GetTimes(hour, minute, time - 20);
                    if (arrive_time[0] == HH)
                    {
                        answerList.Add(arrive_time[1]);
                    }
                }
            }
                       else
            {
                int num = int.Parse(S[1].ToString());
                time = sum(A_times, num, 13);
                if (num > 7)
                {
                    for (int i = 0; i < 6 * 17; i++)
                    {
                        hour = A13_start_A1[i, 0];
                        minute = A13_start_A1[i, 1];
                        arrive_time = GetTimes(hour, minute, time);
                        if (arrive_time[0] == HH)
                        {
                            answerList.Add(arrive_time[1]);
                        }
                    }
                    hour = A13_start_A7[0, 0];
                    minute = A13_start_A7[0, 1];
                    arrive_time = GetTimes(hour, minute, time);
                    if (arrive_time[0] == HH)
                    {
                        answerList.Add(arrive_time[1]);
                    }
                }
                else
                {
                    for (int i = 0; i < 6 * 17; i++)
                    {
                        hour = A13_start_A1[i, 0];
                        minute = A13_start_A1[i, 1];
                        arrive_time = GetTimes(hour, minute, time);
                        if (arrive_time[0] == HH)
                        {
                            answerList.Add(arrive_time[1]);
                        }
                    }
                    for (int i = 0; i < 6 * 17 + 1; i++)
                    {
                        hour = A7_start_A1[i, 0];
                        minute = A7_start_A1[i, 1];
                        arrive_time = GetTimes(hour, minute, time-19);
                        if (arrive_time[0] == HH)
                        {
                            answerList.Add(arrive_time[1]);
                        }
                    }
                }
            }
        }
        else
        {
            if (DIR == "U")
            {
                int num = int.Parse(S[1].ToString());
                time = sum(B_times, 0, num);
                for (int i = 0; i < 10 * 17; i++)
                {
                    hour = B1_start_A7[i, 0];
                    minute = B1_start_A7[i, 1];
                    arrive_time = GetTimes(hour, minute, time);
                    if (arrive_time[0] == HH)
                    {
                        answerList.Add(arrive_time[1]);
                    }
                }
            }
            else
            {
                int num = int.Parse(S[1].ToString());
                time = sum(B_times, num, 6);
                for (int i = 0; i < 10 * 17; i++)
                {
                    hour = A7_start_B1[i, 0];
                    minute = A7_start_B1[i, 1];
                    arrive_time = GetTimes(hour, minute, time);
                    if (arrive_time[0] == HH)
                    {
                        answerList.Add(arrive_time[1]);
                    }
                }
            }
        }

        if (answerList.Count > 0) // 条件を修正
        {
            string hh;
            if (HH < 10){
                hh = "0" + HH.ToString();
            }
            else{
                hh = HH.ToString();
            }
            string output = String.Format("{0}:", hh);
            answerList.Sort();
            for (int i = 0; i < answerList.Count; i++)
            {
                if (answerList[i] < 10){
                    output += " 0" + answerList[i].ToString();
                }                
                else{
                    output += " " + answerList[i].ToString();
                }
            }
            Console.WriteLine(output);
        }
        else
        {
            Console.WriteLine("No train");
        }
    }

    static int[] GetTimes(int hour, int minute, int time)
    {
        if (minute + time >= 60)
        {
            hour += 1;
            minute = minute + time - 60;
        }
        else
        {
            minute += time;
        }
        return new int[] { hour, minute };
    }

    static private string[] GetStdin()
    {
        var list = new List<string>();
        string line;
        while ((line = Console.ReadLine()) != null)
        {
            list.Add(line);
        }
        return list.ToArray();
    }

    static int sum(int[] arr, int start, int end)
    {
        int result = 0;
        for (int i = start; i < end; i++)
        {
            result += arr[i];
        }
        return result;
    }
}
