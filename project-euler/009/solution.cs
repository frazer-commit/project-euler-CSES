using System;

namespace Euclids009
{
	internal class Program
	{
		static void Main(string[] args)
		{
			int perimeter = 1000;
			int semiPerimeter = perimeter / 2;

			(int factor1, int factor2) pair = SqrtFactors(semiPerimeter);

			int m = pair.factor2;
			int n = pair.factor1 - pair.factor2;

			int m2 = m * m;
			int n2 = n * n;

			// Euclid's Formula definitions
			int sideA = m2 - n2;
			int sideB = 2 * m * n;
			int sideC = m2 + n2;
			
			int product = sideA * sideB * sideC;
			Console.WriteLine(product);
		}
		
		// Find the pair of factors closest to sqrt(n)
		public static (int factor1, int factor2) SqrtFactors(int product)
		{
			// Start with sqrt(semiperimeter / 2) lower bound as it is faster... (marginally)
			// See written proof for more detail
			int factor = (int)Math.Ceiling(Math.Sqrt(product / 2));
			int upperBound = (int)Math.Sqrt(product);

			bool found = false;

			while (!found) {
				if (factor > upperBound) {
					throw new ArgumentException($"Invalid Pythagorean triplet");
				} else if (product % factor == 0) {
					found = true;
				} else {
					factor++;
				}
			}
			
			(int factor1, int factor2) pair;
			pair.factor1 = product / factor;
			pair.factor2 = factor;

			return pair;
		}
	}
}
