using System;
using System.IO;
using System.Collections.Generic;

public class MainApp
{

    static public void Main(string[] args)
    {
        var lines = GetStdin();
        string[] T = lines[0].Split(' ');
        float[] t = T.Select(float.Parse).ToArray();
        string[] S = lines[1].Split(' ');
        float[] s = S.Select(float.Parse).ToArray();
        string[] VX = lines[2].Split(' ');
        float[] vx = VX.Select(float.Parse).ToArray();
        string[] VY = lines[3].Split(' ');
        float[] vy = VY.Select(float.Parse).ToArray();
        string[] VZ = lines[4].Split(' ');
        float[] vz = VZ.Select(float.Parse).ToArray();
        float[] ans = new float[3];
        for (int i = 0; i < 3; i++)
        {
            ans[i] = s[i] + t[0] * vx[i] + t[1] * vy[i] + t[2] * vz[i];
        }
        Console.WriteLine(string.Join(" ", ans));
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

