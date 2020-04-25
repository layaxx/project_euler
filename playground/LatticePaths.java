package playground;

public class LatticePaths {
    static int limit = 3;

    public static long findPathsFrom(int posX, int posY) {
        if (posX == limit - 1 && posY == limit - 1) {
            return 1;
        } else {
            if (posX != limit - 1 && posY != limit - 1) {
                return findPathsFrom(posX + 1, posY) + findPathsFrom(posX, posY + 1);
            } else if (posX != limit - 1) {
                return findPathsFrom(posX + 1, posY);
            } else {
                return findPathsFrom(posX, posY + 1);
            }
        }
    }

    public static void main(String[] args) {
        int posX = 0;
        int posY = 0;
        System.out.println(findPathsFrom(posX, posY));
    }
}