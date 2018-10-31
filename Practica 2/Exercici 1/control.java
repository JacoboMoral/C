import java.util.ArrayList;
import java.util.Collections;

/**
 *
 * @author Daniel
 */

public class FiniteField
{
    static byte[] tableOfExp;
    static byte[] tableOfLog;
    static ArrayList<Byte> generators;

    public static byte GF_product_p(byte a, byte b)
    {
        byte r = 0;
        int raux, aaux, baux, xor;
        for (int i = 0; i < 8; ++i)
        {
            // If least significant bit of byte b is equal to 1, r = r ^ a
            // To do an XOR or << in Java, we can convert bytes to ints
            // using a bit mask and then convert the resulting int
            // back to a byte with a cast (byte)
            if ((b & 0x01) == 1)
            {
                raux = r & 0xFF;
                aaux = a & 0xFF;
                xor = raux ^ aaux;
                r = (byte)(xor);
            }
            // If most significant bit of byte a is equal to 0, a = a << 1
            // If most significant bit of byte a is equal to 1, a = a << 1 and a = a ^ 0x1B
            int msb = a & 0x80;
            aaux = a & 0xFF;
            aaux = aaux << 1;
            a = (byte)(aaux);
            if (msb == 128)
            {
                xor = aaux ^ 0x1B;
                a = (byte)(xor);
            }
            // b = b >> 1;
            baux = b & 0xFF;
            baux = baux >> 1;
            b = (byte)(baux);
        }
        return r;
    }

    public static byte GF_product_p_02(byte a)
    {
        // Multiply by 0x02 -> Multiply by x -> if msb of a is equal to 0, a = a << 1
        //                                   -> if msb of a is equal to 1, a = a << 1 and a = a ^ 0x1B
        int msb = a & 0x80;
        int aaux = a & 0xFF;
        aaux = aaux << 1;
        a = (byte)(aaux);
        if (msb == 128)
        {
            a = (byte)(aaux ^ 0x1B);
        }
        return a;
    }

    public static byte GF_product_p_03(byte a)
    {
        // Multiply by 0x03 -> Multiply by x + 1
        return (byte) (GF_product_p_02(a) ^ a);
    }

    public static byte GF_product_p_09(byte a)
    {
        // Multiply by 0x09 -> Multiply by x^3 + 1
        byte aaux = GF_product_p_02(a);
        aaux = GF_product_p_02(aaux);
        aaux = GF_product_p_02(aaux);
        return (byte) (aaux ^ a);
    }

    public static byte GF_product_p_0B(byte a)
    {
        // Multiply by 0x0B -> Multiply by x^3 + x + 1
        byte aaux1 = GF_product_p_09(a);
        byte aaux2 = GF_product_p_02(a);
        return (byte) (aaux1 ^ aaux2);
    }

    public static byte GF_product_p_0D(byte a)
    {
        // Multiply by 0x0D -> Multiply by x^3 + x^2 + 1
        byte aaux1 = GF_product_p_09(a);
        byte aaux2 = GF_product_p_02(a);
        aaux2 = GF_product_p_02(aaux2);
        return (byte) (aaux1 ^ aaux2);
    }

    public static byte GF_product_p_0E(byte a)
    {
        // Multiply by 0x0E -> Multiply by x^3 + x^2 + x -> Multiply by x (x^2 + x + 1)
        byte aaux1 = GF_product_p_02(a);
        aaux1 = GF_product_p_02(aaux1);
        byte aaux2 = GF_product_p_03(a);
        aaux1 = (byte) (aaux1 ^ aaux2);
        return (GF_product_p_02(aaux1));
    }

    public static void GF_tables()
    {
        tableOfExp = new byte[256];
        tableOfLog = new byte[256];
        tableOfExp[0] = (byte) 0x01;
        for (int i = 1; i < 256; ++i)
        {
            tableOfExp[i] = GF_product_p(tableOfExp[i-1], (byte) 0x03);
            tableOfLog[tableOfExp[i-1] & 0xff] = (byte) (i-1);
        }
    }

    public static byte GF_product_t(byte a, byte b)
    {
        int pos = (tableOfLog[a & 0xff] & 0xff) + (tableOfLog[b & 0xff] & 0xff);
        return ((pos > 255) ? tableOfExp[pos-255] : tableOfExp[pos]);
    }

    public static byte GF_product_t_02(byte a)
    {
        int pos = (tableOfLog[a & 0xff] & 0xff) + (0x19 & 0xff);
        return ((pos > 255) ? tableOfExp[pos-255] : tableOfExp[pos]);
    }

    public static byte GF_product_t_03(byte a)
    {
        int pos = (tableOfLog[a & 0xff] & 0xff) + (0x01 & 0xff);
        return ((pos > 255) ? tableOfExp[pos-255] : tableOfExp[pos]);
    }

    public static byte GF_product_t_09(byte a)
    {
        int pos = (tableOfLog[a & 0xff] & 0xff) + (0xC7 & 0xff);
        return ((pos > 255) ? tableOfExp[pos-255] : tableOfExp[pos]);
    }

    public static byte GF_product_t_0B(byte a)
    {
        int pos = (tableOfLog[a & 0xff] & 0xff) + (0x68 & 0xff);
        return ((pos > 255) ? tableOfExp[pos-255] : tableOfExp[pos]);
    }

    public static byte GF_product_t_0D(byte a)
    {
        int pos = (tableOfLog[a & 0xff] & 0xff) + (0xEE & 0xff);
        return ((pos > 255) ? tableOfExp[pos-255] : tableOfExp[pos]);
    }

    public static byte GF_product_t_0E(byte a)
    {
        int pos = (tableOfLog[a & 0xff] & 0xff) + (0xDF & 0xff);
        return ((pos > 255) ? tableOfExp[pos-255] : tableOfExp[pos]);
    }

    public static byte GF_invers(byte a)
    {
        if (a == 0x00) return 0x00;
        else return (tableOfExp[255 - tableOfLog[a & 0xff] & 0xff]);
    }

    public static void GF_generador()
    {
        // A generator is defined as an element whose successive powers take on
        // every element of the field except the zero.
        // For example, 0x03 is a generator for GF(2^8) because its powers take
        // on all 255 non-zero values of the field.
        generators = new ArrayList<Byte>();
        ArrayList<Integer> out = new ArrayList<Integer>();
        int counter;
        byte a, power;
        for (int i = 0; i < 256; ++i)
        {
            a = tableOfExp[i];
            power = a;
            counter = 1;
            while (power != (byte) 0x01)
            {
                power = GF_product_p(power, a);
                ++counter;
            }
            if (counter == 255) generators.add(a);
        }

        for (int i = 0; i < generators.size(); ++i){
            //int i2 = b & 0xFF;
            int aux = generators.get(i) & 0xFF;
            out.add(aux);
        }
        Collections.sort(out);
        System.out.println(out);
    }

    public static void main(String[] args)
    {
        GF_tables();
        GF_generador();
        long t1, t2;
        t1 = System.nanoTime();
        for (int i = 0; i < 390625; ++i)
            for (int j = 0; j < 256; ++j)
                GF_product_p(tableOfExp[i%tableOfExp.length], tableOfExp[j]);
        t2 = System.nanoTime();
        System.out.println("GF_product_p -> " + (t2-t1));

        t1 = System.nanoTime();
        for (int i = 0; i < 390625; ++i)
            for (int j = 0; j < 256; ++j)
                GF_product_t(tableOfExp[i%tableOfExp.length], tableOfExp[j]);
        t2 = System.nanoTime();
        System.out.println("GF_product_t -> " + (t2-t1));

        // GF_product_p_02 VS GF_product_t_02
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p_02(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_p_02 -> " + (t2-t1));

        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t_02(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_t_02 -> " + (t2-t1));

        // GF_product_p_03 VS GF_product_t_03
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p_03(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_p_03 -> " + (t2-t1));

        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t_03(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_t_03 -> " + (t2-t1));

        // GF_product_p_09 VS GF_product_t_09
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p_09(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_p_09 -> " + (t2-t1));

        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t_09(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_t_09 -> " + (t2-t1));

        // GF_product_p_0B VS GF_product_t_0B
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p_0B(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_p_0B -> " + (t2-t1));

        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t_0B(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_t_0B -> " + (t2-t1));

        // GF_product_p_0D VS GF_product_t_0D
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p_0D(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_p_0D -> " + (t2-t1));

        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t_0D(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_t_0D -> " + (t2-t1));

        // GF_product_p_0E VS GF_product_t_0E
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p_0E(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_p_0E -> " + (t2-t1));

        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t_0E(tableOfExp[i%tableOfExp.length]);
        t2 = System.nanoTime();
        System.out.println("GF_product_t_0E -> " + (t2-t1));

        // GF_product_p(a,0x02) vs GF_product_p_02(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p(tableOfExp[i%tableOfExp.length], (byte) 0x02);
        t2 = System.nanoTime();
        System.out.println("GF_product_p(a,0x02) -> " + (t2-t1));

        // GF_product_p(a,0x03) vs GF_product_p_03(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p(tableOfExp[i%tableOfExp.length], (byte) 0x03);
        t2 = System.nanoTime();
        System.out.println("GF_product_p(a,0x03) -> " + (t2-t1));

        // GF_product_p(a,0x09) vs GF_product_p_09(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p(tableOfExp[i%tableOfExp.length], (byte) 0x09);
        t2 = System.nanoTime();
        System.out.println("GF_product_p(a,0x09) -> " + (t2-t1));

        // GF_product_p(a,0x0B) vs GF_product_p_0B(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p(tableOfExp[i%tableOfExp.length], (byte) 0x0B);
        t2 = System.nanoTime();
        System.out.println("GF_product_p(a,0x0B) -> " + (t2-t1));

        // GF_product_p(a,0x0D) vs GF_product_p_0D(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p(tableOfExp[i%tableOfExp.length], (byte) 0x0D);
        t2 = System.nanoTime();
        System.out.println("GF_product_p(a,0x0D) -> " + (t2-t1));

        // GF_product_p(a,0x0E) vs GF_product_p_0E(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_p(tableOfExp[i%tableOfExp.length], (byte) 0x0E);
        t2 = System.nanoTime();
        System.out.println("GF_product_p(a,0x0E) -> " + (t2-t1));

        // GF_product_t(a,0x02) vs GF_product_t_02(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t(tableOfExp[i%tableOfExp.length], (byte) 0x02);
        t2 = System.nanoTime();
        System.out.println("GF_product_t(a,0x02) -> " + (t2-t1));

        // GF_product_t(a,0x03) vs GF_product_t_03(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t(tableOfExp[i%tableOfExp.length], (byte) 0x03);
        t2 = System.nanoTime();
        System.out.println("GF_product_t(a,0x03) -> " + (t2-t1));

        // GF_product_t(a,0x09) vs GF_product_t_09(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t(tableOfExp[i%tableOfExp.length], (byte) 0x09);
        t2 = System.nanoTime();
        System.out.println("GF_product_t(a,0x09) -> " + (t2-t1));

        // GF_product_t(a,0x0B) vs GF_product_t_0B(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t(tableOfExp[i%tableOfExp.length], (byte) 0x0B);
        t2 = System.nanoTime();
        System.out.println("GF_product_t(a,0x0B) -> " + (t2-t1));

        // GF_product_t(a,0x0D) vs GF_product_t_0D(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t(tableOfExp[i%tableOfExp.length], (byte) 0x0D);
        t2 = System.nanoTime();
        System.out.println("GF_product_t(a,0x0D) -> " + (t2-t1));

        // GF_product_t(a,0x0E) vs GF_product_t_0E(a)
        t1 = System.nanoTime();
        for (int i = 0; i < 100000000; ++i) GF_product_t(tableOfExp[i%tableOfExp.length], (byte) 0x0E);
        t2 = System.nanoTime();
        System.out.println("GF_product_t(a,0x0E) -> " + (t2-t1));
    }

}
