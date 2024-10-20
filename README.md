# PaperManager

## Introduction

It's not easy to manager your papers in your local directory, especially when you have lots of `PDF` file. What's worse, their name often do not match with their title (because you download it from website and got `120000001.pdf`). You have to open them one after another to find the one you need.

To make paper managing easier, I wrote a simple python shell which can automatically search all of your pdf in your current directory and list them in an markdown file.

## How to use

Put the file `paper_manager.py` in your current directory, then run the following command:

``` sh
python paper_manager.py
```

Then you can see `PaperList.md` generated, all of your pdf file informations in your current directory will be list in it.

## Example

For example, your directory looks like this:

``` txt
C:.
    Inline Expansion When and How.pdf
    PaperList.md
    paper_manager.py
    123456.pdf
```

After executing the shell, you could get an markdown file looks like below:

``` markdown
# Paper List

The number of pdf file is **2**.

Last updating time is `2024-10-18 23:58:51`.

## Papers

**Title**: `Inline Expansion When and How.pdf`

filepath: Inline Expansion When and How.pdf

---

**Title**: `LNCS 2958 - To Inline or Not to Inline? Enhanced Inlining Decisions`

filepath: 123456.pdf

---
```
