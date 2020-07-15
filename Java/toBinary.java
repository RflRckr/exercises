class Main {
  public static String toBinary(int numberToconvert){
    int remainder = numberToconvert;
    String binary = "";
    while(remainder > 1){
      binary = (remainder%2) + binary;
      remainder = remainder / 2;
    }
    binary = remainder + binary;
    return binary;
  }
  
  public static void main(String[] args) {
    System.out.println(toBinary(35));
  }
}
