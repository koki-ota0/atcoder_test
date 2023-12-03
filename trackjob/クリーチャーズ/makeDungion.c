using System;
using System.IO;
using System.Collections.Generic;

public class MainApp
{

    static public void Main(string[] args)
    {
        var lines = GetStdin();
        int k = int.Parse(lines[0]);
        int n = 50;
        int m = 50;
        char[][] map = new char[n][];
        for (int i = 0; i < n; i++)
        {
            map[i] = new char[m]; // Create a new char array for each row
            for (int j = 0; j < m; j++)
            {
                map[i][j] = '.'; // Initialize each cell to '.'
            }
        }
        map[0][0] = 'S';

        if (k < n + m - 2) {
            int g_x = Math.Min(k, m - 1);
            int g_y = Math.Max(k - g_x, 0);
            map[g_y][g_x] = 'G';
        }
        else {
            //障害#を配置
            int row = (k / (n-1));
            int col = (k % (n-1));
            for (int i = 1; i < row; i++) {
                if (i % 2 == 0) {
                    for (int j = m-1; j > 0; j--) {
                        map[i*2-1][j] = '#';
                    }
                }
                else {
                    for (int j = 0; j < m-1; j++) {
                        map[i*2-1][j] = '#';
                    }
                }
            }
            if (row % 2 == 0){
              map[n-1][n-1-col] = 'G';
            }
            else{
              map[n-1][col] = 'G';
            }
            
        }

        string size = String.Format("{0} {1}", n, m); 
        Console.WriteLine(size);
        for (int i = 0; i < n; i++)
        {
            string output = new string(map[i]); // Create a string from the char array
            Console.WriteLine(output);
        }
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
}