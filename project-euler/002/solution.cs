using System;

namespace EvenFib
{
	internal class Program
	{
		static void Main(string[] args)
		{
			int n1;
			int n2;
			int temp;
			int total;

			n1 = 1;
			n2 = 0;
			total = 0;

			while (n1 <= 4000000) {
				if (n1 % 2 == 0) {
					total += n1;
				}
				temp = n1;
				n1 += n2;
				n2 = temp;
			}

			Console.WriteLine(total);
		}
	}
}
	
