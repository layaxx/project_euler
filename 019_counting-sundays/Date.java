
public class Date {

	private int day;
	private Day weekday;
	private Month month;
	private int year;

	public Date() {
		day = 1;
		month = Month.JANUARY;
		year = 1901;
		weekday = Day.TUESDAY;
	}

	public void nextSunday() {
		this.nextDay();
		while (this.weekday != Day.SUNDAY) {
			this.nextDay();
		}
	}

	public void nextFirstOfMonth() {
		this.nextDay();
		while (this.day != 1) {
			this.nextDay();
		}
	}

	void nextDay() {
		advanceWeekDay();
		/*
		 * if (this.day < 30) { if (month != Month.FEBRUARY || day < 28) { this.day++;
		 * return; } else { if (day == 28) { if (leapyear()) { day++; } else { day = 1;
		 * month = Month.MARCH; } } else if (day == 29) { day = 0; month = Month.MARCH;
		 * } } } else if (this.day == 31) { switch (month) { case AUGUST: month =
		 * Month.SEPTEMBER; break; case DECEMBER: month = Month.JANUARY; year++; return;
		 * case JANUARY: month = Month.FEBRUARY; break; case JULY: month = Month.AUGUST;
		 * break; case MARCH: month = Month.APRIL; break; case MAY: month = Month.JUNE;
		 * break; case OKTOBER: month = Month.NOVEMBER; break; default:
		 * System.out.println("Error in month switch else if"); break; } day = 1; } else
		 * { switch (month) { case SEPTEMBER: month = Month.OKTOBER; day = 1; break;
		 * case JUNE: month = Month.JULY; day = 1; break; case APRIL: month =
		 * Month.JUNE; day = 1; break; case NOVEMBER: month = Month.DECEMBER; day = 1;
		 * break; default: day++; break; } }
		 */
		if (day < getNumberOfDays()) {
			day++;
		} else {
			day = 1;
			switch (month) {
			case APRIL:
				month = Month.MAY;
				break;
			case AUGUST:
				month = Month.SEPTEMBER;
				break;
			case DECEMBER:
				month = Month.JANUARY;
				year++;
				break;
			case FEBRUARY:
				month = Month.MARCH;
				break;
			case JANUARY:
				month = Month.FEBRUARY;
				break;
			case JULY:
				month = Month.AUGUST;
				break;
			case JUNE:
				month = Month.JULY;
				break;
			case MARCH:
				month = Month.APRIL;
				break;
			case MAY:
				month = Month.JUNE;
				break;
			case NOVEMBER:
				month = Month.DECEMBER;
				break;
			case OKTOBER:
				month = Month.NOVEMBER;
				break;
			case SEPTEMBER:
				month = Month.OKTOBER;
				break;
			default:
				System.out.println("Error in NextDay - MOnth switch - default case");
				break;

			}
		}
	}

	private int getNumberOfDays() {
		switch (month) {
		case APRIL:
			return 30;

		case AUGUST:
			return 31;

		case DECEMBER:
			return 31;

		case FEBRUARY:
			if (leapyear()) {
				return 29;
			} else {
				return 28;
			}

		case JANUARY:
			return 31;

		case JULY:
			return 31;

		case JUNE:
			return 30;

		case MARCH:
			return 31;

		case MAY:
			return 31;

		case NOVEMBER:
			return 30;

		case OKTOBER:
			return 31;

		case SEPTEMBER:
			return 30;

		default:
			System.out.println("Error in getNumberDays() - default case");
			return -1;

		}
	}

	private boolean leapyear() {
		if (year % 4 == 0) {
			if (year % 400 == 0) {
				return true;
			}
			if (year % 100 == 0) {
				return false;
			}
			return true;
		}
		return false;
	}

	private void advanceWeekDay() {
		switch (this.weekday) {
		case FRIDAY:
			this.weekday = Day.SATURDAY;
			break;
		case MONDAY:
			this.weekday = Day.TUESDAY;
			break;
		case SATURDAY:
			this.weekday = Day.SUNDAY;
			break;
		case SUNDAY:
			this.weekday = Day.MONDAY;
			break;
		case THURSDAY:
			this.weekday = Day.FRIDAY;
			break;
		case TUESDAY:
			this.weekday = Day.WEDNESDAY;
			break;
		case WEDNESDAY:
			this.weekday = Day.THURSDAY;
			break;
		default:
			System.out.println("Error in Day switch");
			break;
		}
	}

	public int getDay() {
		return day;
	}

	public Month getMonth() {
		return month;
	}

	public int getYear() {
		return year;
	}

	public String formatOutput() {
		return "Date: " + day + "." + month + "." + year + " (" + weekday + ")";
	}

	public void print() {
		System.out.println(formatOutput());
	}

	public Day getWeekDay() {
		return weekday;
	}

}
