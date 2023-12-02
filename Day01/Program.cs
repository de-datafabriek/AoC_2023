using System.Text.RegularExpressions;
List<string> NumbersInWriting = new() { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
string SOURCE_FILE = "./Day01/input2.txt";
_ = await firstAttempt();
_ = await secondAttempt(false);
_ = await secondAttempt(true);

async Task<int> secondAttempt(bool translateWords)
{
    //this attempt will consider translation of overlapping text. eightwo will return as "82"
    List<int> nrs = new();
    var input = await File.ReadAllLinesAsync(SOURCE_FILE);
    foreach (var l in input)
    {
        string digits = "";
        for (int i = 0; i < l.Length; i++)
        {
            if (int.TryParse(l.Substring(i, 1), out int d))
                digits += d;
            if(translateWords)
            {
                int ni = 0;
                NumbersInWriting.ForEach(ns =>
                {
                    if (l.Substring(i, l.Length - i).StartsWith(ns)) digits += ni.ToString();
                    ni++;
                });
            }
        }
        nrs.Add(int.Parse($"{digits[0]}{digits[digits.Length - 1]}"));
    }
    Console.WriteLine(nrs.Sum()); //52834
    return nrs.Sum();
}

async Task<int> firstAttempt()
{
    //this attempt will not consider translation of overlapping text. eightwo will return as "8" only and not "82"
    var input = await File.ReadAllLinesAsync(SOURCE_FILE);
    var numbersInterpolated = input.Select(l =>
    {
        while (true)
        {
            var pos = NumbersInWriting.Select((s, n) => (s, n, start: l.IndexOf(s))).Where(p => p.start > -1).OrderBy(p => p.start).FirstOrDefault();
            if (pos.s is null) break;
            l = l.Replace(pos.s, pos.n.ToString());
        }
        return l;
    }).ToArray();
    var numbers = numbersInterpolated.Select(l => Regex.Replace(l, "[^0-9]", "")).ToArray();
    var numbers2 = numbers.Select(l => $"{l[0]}{l[l.Length - 1]}").ToArray();
    var numbersInt = numbers2.Select(l => int.Parse(l)).ToArray();
    var sum = numbersInt.Sum();
    Console.WriteLine(sum); //52829
    return sum;
}