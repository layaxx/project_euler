
public class MainClass {

	public static void main(String[] args) {
		int count = 0;
		Date date = new Date();
		date.nextSunday();
		while (date.getYear() < 2001) {
			if (date.getDay() == 1) {
				count++;
				date.print();
			}
			date.nextSunday();

		}
		System.out.println(
				"There were " + count + " Sundays in the twentieth Century that fell on the first of the month");
	}

}
