# 자바에서의 형 변환

## String형 → 숫자형(int, double, float)

```java
String sNum = "1234"; 

// String → int
int i1 = Integer.parseInt(sNum);
int i2 = Integer.valueOf(sNum);

// String → double
double d = Double.valueOf(sNum);

// String → float
float f = Float.valueOf(sNum);

// String → long
long l = Long.parseLong(sNum);

// String → short
short s = Short.parseShort(sNum);
```

## 숫자형(int, double, float) → String 형

```java
// int → String
int i = 1234;
String s = String.valueOf(i);
String s = Integer.toString(i);

// float → String 
float f = 1.23;
String s = String.valuOf(f);
String s = Float.toString(f);

// double -> String
double d = 1.23;
String s = String.valueOf(d);
String s = Double.toString(d);
```