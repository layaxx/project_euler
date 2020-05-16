package projectEuler_31;

public class Main {
	/*
	 * public static void main(String[] args) {
	 * 
	 * List<Combination> combinations = new ArrayList<Combination>();
	 * 
	 * int[] coins = new int[] { 1, 2, 5, 10, 20, 50, 100, 200 }; for (int i = 0; i
	 * < coins.length; i++) { int[] array = new int[8]; array[i] = 1;
	 * combinations.add(new Combination(array)); }
	 * 
	 * for (int iteration = 0; iteration < 200; iteration++) {
	 * System.out.println("Iteration: " + iteration + " current size: " +
	 * combinations.size()); List<Combination[]> c2 = new
	 * ArrayList<Combination[]>(); for (Combination c : combinations) {
	 * c2.add(c.createNewCombinations()); } combinations = new
	 * ArrayList<Combination>(); for (Combination[] cArray : c2) { for (Combination
	 * combi : cArray) { if (combi != null) { if (combinations.indexOf(combi) == -1)
	 * { combinations.add(combi); } } } }
	 * 
	 * }
	 * 
	 * System.out.println(combinations.size()); }
	 */

	public static void main(String[] args) {
		int target = 200;
		int ways = 0;

		for (int a = target; a >= 0; a -= 200) {
			for (int b = a; b >= 0; b -= 100) {
				for (int c = b; c >= 0; c -= 50) {
					for (int d = c; d >= 0; d -= 20) {
						for (int e = d; e >= 0; e -= 10) {
							for (int f = e; f >= 0; f -= 5) {
								for (int g = f; g >= 0; g -= 2) {
									ways++;
								}
							}
						}
					}
				}
			}
		}

		System.out.println(ways);
	}
}
