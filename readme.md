##Text Summarization in Tamil

###Method 1 - Sentence Weighing

[Refrence : Section 2.1](http://research.ijcaonline.org/volume75/number6/pxc3890449.pdf)

###Method 2 - Page Rank Score

[Refrence : Section 2.2](http://research.ijcaonline.org/volume75/number6/pxc3890449.pdf)


###Method 3 - Clustering Approach

[Refrence : Section 3.3](http://nlp.cic.ipn.mx/Publications/2008/Text%20Summarization%20by%20Sentence%20Extraction%20Using.pdf)


----

Test data is present in `./test/data`

----

###Design Specification

1. Move cross algorithm functions like `edit_distance`, `tf_idf`, `kmeans` to the util folder.

   (eg) Create a file util/edit_distance.py.
        Define a function edit_distance(w1, w2) which returns the numeric edit distance between 2 words.
        If you're using an external library, use a wrapper function to call the external library functions.

2. Create individual python files for each method implementation.

  Create a command-line interface for each of the methods.

  ```python
  python sentence-weighing.py 'PATH_TO_INPUT_FILE'
  # Prints the summary into STD_OUT
  ```

  Create a python API interface for each of the methods.

  ```python
  import sentence-weighing

  SentenceWeight(file_path).generate_summary()
  # Returns the summary as a string
  ```

3. Create a separate git branch for each method and open a PR.




