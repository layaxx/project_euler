package projectEuler_31;

public class Combination {

	private int[] array;
	private int[] coins;
	private int value;
	private int limit;
	private int start;

	public Combination(int[] array) {
		this.array = array;
		this.coins = new int[] { 200, 100, 50, 20, 10, 5, 2, 1 };
		this.value = generateValue();
		this.limit = 200;
		start = determineStartValue();
	}

	private int determineStartValue() {
		for (int i = array.length - 1; i >= 0; i--) {
			if (array[i] != 0) {
				return i;
			}
		}
		return 0;
	}

	private int generateValue() {
		int result = 0;
		for (int i = 0; i < coins.length; i++) {
			result += array[i] * coins[i];
		}
		return result;
	}

	public int getValue() {
		return value;
	}

	public Combination[] createNewCombinations() {
		Combination[] result = new Combination[8];
		int freeField = 0;
		for (int i = start; i < coins.length; i++) {
			if (value + coins[i] <= limit) {
				int[] newArray = array.clone();
				array[i]++;
				result[freeField] = new Combination(newArray);
				freeField++;
			}
		}
		return result;
	}

}
