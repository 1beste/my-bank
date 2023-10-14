
public class Operators3 {

    public static void main(String[] args) {

        /* Mantıksal Operatörler:
        
        && => And operatörü : İçinde en az 1 false olursa sonuç false çıkar.
        
        || => Or operatörü : İçinde en az 1 true olursa sonuç true çıkar.
        
        ! => Not operatörü
        
         */
        System.out.println(4 == 4 && 2 < 3);
        System.out.println(5 != 5 || 8 <= 4);
        System.out.println(!true);
        System.out.println(!(!(15 > 9 && "Beste" == "Beste") || 2.1 >= 4.5));
    }
}
