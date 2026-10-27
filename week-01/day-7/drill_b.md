# Task 01.7.B - Pipeline

## Input

The file `visits.log` contains 15 visit records in this format:

```text
page=/home user=ali
```

## 1. Most popular page

Command:

```bash
awk '{print $1}' visits.log | sort | uniq -c | sort -nr | head -n 1
```

Output:

```text
      7 page=/home
```

Result: `/home` is the most popular page with 7 visits.

## 2. Count visits by sara

Command:

```bash
grep "user=sara" visits.log | wc -l
```

Output:

```text
6
```

Result: `sara` has 6 visits.

## 3. Export non-home visits

Command:

```bash
grep -v "page=/home" visits.log > others.txt
```

The generated `others.txt` contains:

```text
page=/about user=sara
page=/contact user=ali
page=/products user=reza
page=/blog user=sara
page=/login user=sara
page=/dashboard user=nima
page=/profile user=ali
page=/settings user=zohreh
```

Validation command:

```bash
diff -u others.txt <(grep -v "page=/home" visits.log)
```

The command produced no output, which confirms that `others.txt` is correct.
