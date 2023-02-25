# Multiple-Document-String-Search
A simple python script that compares each line item string from a text file to see if it exist in a separate document

Requirements

```
git clone
pip install argparse
```

 **USAGE**
 ```
options:
  -h, --help     show this help message and exit
  --doc_a DOC_A  doc_a file
  --doc_b DOC_B  doc_b file
  ```
 
```
python3 string_search.py --doc_a <string file> --doc_b <check file>
```

```
python3 string_search.py --doc_a strings.txt --doc_b checkfile.txt
```

**Save the Results to a new text file**

```
python3 string_search.py --doc_a strings.txt --doc_b checkfile.txt > results.txt
```
