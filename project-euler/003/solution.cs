using System;

/*
This solution isn't that great since it doesn't use primes
But it still gets the solution very quickly
*/

namespace Largest_Prime
{
	internal class Program
	{
		static void Main(string[] args)
		{
			long n = 600851475143L;
			long i = 1;

			while (Math.Pow(i, 2) <= n) {
				i += 2;

				if (n % i == 0) {
					n /= i;
				}
			}
			Console.WriteLine(n);
		}
	}
}
