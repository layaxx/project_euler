package p023_nonabundantsums;

import java.util.ArrayList;
import java.util.List;

public class MainClass {

	private static int limit = 28123;

	public static void main(String[] args) {
		// solveIncorrect();
		// solveNew();
		solve3();
	}

	private static void solve3() {
		int sum = 0;
		List<Integer> listOfAbundantNumbers = generateListOfAbundantNumbers();

		boolean[] isSumOfAbundantNumbers = new boolean[limit + 1];

		for (int i = 0; i < listOfAbundantNumbers.size(); i++) {
			for (int j = i; j < listOfAbundantNumbers.size(); j++) {
				if (listOfAbundantNumbers.get(i) + listOfAbundantNumbers.get(j) > limit) {
					break;
				} else {
					isSumOfAbundantNumbers[listOfAbundantNumbers.get(i) + listOfAbundantNumbers.get(j)] = true;
				}

			}
		}

		for (int i = 1; i <= limit; i++) {
			if (!isSumOfAbundantNumbers[i]) {
				sum += i;
				System.out.println(i);
			}
		}

		System.out.println(sum);

	}

	// should be working fine
	private static long sumOfDivisors(int number) {
		long sum = 0;
		for (int i = 1; i < number; i++) {
			if (number % i == 0) {
				sum += i;
			}
		}
		return sum;
	}

	private static List<Integer> generateListOfAbundantNumbers() {
		List<Integer> abundantNumbers = new ArrayList<Integer>();
		for (int i = 12; i < limit + 1; i++) {
			if (sumOfDivisors(i) > i) {
				abundantNumbers.add(i);
			}
		}
		return abundantNumbers;
	}

	// nothing really works down there
	private static void solveNew() {
		List<Integer> listOfAbundantNumbers = generateListOfAbundantNumbers();
		List<Integer> listOfSums = generateListOfSums(listOfAbundantNumbers);
		long sum = 0;
		for (int i = 0; i < limit + 1; i++) {
			if (!listOfSums.contains(i)) {
				sum += i;
			}
		}
		System.out.println(sum);
	}

	private static List<Integer> generateListOfSums(List<Integer> listOfAbundantNumbers) {
		List<Integer> result = new ArrayList<Integer>();

		for (int i = 0; i < listOfAbundantNumbers.size(); i++) {
			for (int j = 0; j < listOfAbundantNumbers.size(); j++) {
				result.add(listOfAbundantNumbers.get(i) + listOfAbundantNumbers.get(j));
			}
		}

		return result;
	}

	private static void solveIncorrect() {
		long sum = 0;
		List<Integer> list1 = generateListOfAbundantNumbers();
		for (int i = 0; i < limit + 1; i++) {
			boolean check = checkIfSum(i, list1);
			if (!check) {
				sum += i;
				System.out.println("Checking " + i + ": " + check);
			}
		}
		System.out.println(sum);
	}

	private static boolean checkIfSum(int i, List<Integer> abundantNumbers) {
		int index1 = 0;
		int index2 = 0;

		while (abundantNumbers.get(index1) <= 3 * i / 4) {
			while (abundantNumbers.get(index1) + abundantNumbers.get(index2) <= i) {
				if (abundantNumbers.get(index1) + abundantNumbers.get(index2) == i) {
					return true;
				}
				index2++;
			}
			index1++;
			index2 = 0;
		}
		return false;
	}
}
