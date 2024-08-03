import java.util.*;

public class RPGGameQuest {
    static class Monster {
        int power;
        int bonus;

        Monster(int power, int bonus) {
            this.power = power;
            this.bonus = bonus;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int initialExperience = scanner.nextInt();

        Monster[] monsters = new Monster[n];
        for (int i = 0; i < n; i++) {
            int power = scanner.nextInt();
            monsters[i] = new Monster(power, 0);
        }
        for (int i = 0; i < n; i++) {
            int bonus = scanner.nextInt();
            monsters[i].bonus = bonus;
        }

        Arrays.sort(monsters, Comparator.comparingInt(m -> m.power));

        int defeated = 0;
        int experience = initialExperience;

        for (Monster monster : monsters) {
            if (experience >= monster.power) {
                experience += monster.bonus;
                defeated++;
            } else {
                break;
            }
        }

        System.out.println(defeated);
    }
}
