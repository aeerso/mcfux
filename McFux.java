import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.ByteArrayOutputStream;
import java.security.SecureRandom;
import java.util.Arrays;
import java.lang.StringBuilder;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Calendar;
import java.util.*;


public class b {
    public static String a(String str, String str2) {
        try {
            byte[] bArr = new byte[8];
            new SecureRandom().nextBytes(bArr);
            byte[] encoded = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1").generateSecret(new
PBEKeySpec(str2.toCharArray(), bArr, 100, 384)).getEncoded();
            SecretKeySpec secretKeySpec = new SecretKeySpec(Arrays.copyOfRange(encoded, 0, 32), "AES");
            Cipher instance = Cipher.getInstance("AES/CBC/PKCS5Padding");
            instance.init(1, secretKeySpec, new IvParameterSpec(Arrays.copyOfRange(encoded, 32, 48)));
            byte[] doFinal = instance.doFinal(str.getBytes("UTF-8"));
            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
            byteArrayOutputStream.write(doFinal);
            byteArrayOutputStream.write(bArr);
	    return Base64.getEncoder().encodeToString(byteArrayOutputStream.toByteArray());
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args){
         String auth_key = args[0];
         SimpleDateFormat var0 = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSSSSS'Z'", Locale.US);
         var0.setTimeZone(TimeZone.getTimeZone("UTC"));
         String payload = auth_key+"|"+var0.format(new Date(Long.valueOf((new Date()).getTime()-1000*10*60)));
         String outputVal = a(payload, args[1]);
         System.out.println(outputVal.replace("\n", "").replace(" ", ""));
}
}
