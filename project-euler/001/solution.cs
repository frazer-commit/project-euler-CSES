using System;

namespace Fifteen
{
	internal class Program
	{
		static int Gaussian_Sum(int n)
		{
			int result = n*(n+1) / 2;
			return result;
		}

		static void Main(string[] args)
		{
			int n = 1000;
			n--;

			int threes = Gaussian_Sum(n / 3) * 3;
			int fives = Gaussian_Sum(n / 5) * 5;
			int fifteens = Gaussian_Sum(n / 15) * 15;

			int result = threes + fives - fifteens;
			Console.WriteLine(result);
		}
	}
}
